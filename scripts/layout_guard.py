#!/usr/bin/env python3
"""Small geometry guard for PNG infographic renderers.

Use this from PIL/canvas-style render scripts to register readable text and
collision-relevant graphic bounds. A finished render should call
``guard.assert_clear()`` before saving/presenting the PNG.
"""
from __future__ import annotations

from dataclasses import dataclass
import math
from typing import Iterable, List, Optional, Sequence, Tuple


Rect = Tuple[float, float, float, float]
Point = Tuple[float, float]


@dataclass
class Box:
    kind: str
    name: str
    rect: Rect
    role: str = "forbidden"

    def padded(self, pad: float) -> "Box":
        x0, y0, x1, y1 = self.rect
        return Box(self.kind, self.name, (x0 - pad, y0 - pad, x1 + pad, y1 + pad), self.role)


def intersects(a: Rect, b: Rect) -> bool:
    ax0, ay0, ax1, ay1 = a
    bx0, by0, bx1, by1 = b
    return ax0 < bx1 and ax1 > bx0 and ay0 < by1 and ay1 > by0


def contains(outer: Rect, inner: Rect, pad: float = 0) -> bool:
    ox0, oy0, ox1, oy1 = outer
    ix0, iy0, ix1, iy1 = inner
    return ix0 >= ox0 + pad and iy0 >= oy0 + pad and ix1 <= ox1 - pad and iy1 <= oy1 - pad


def point_in_rect(point: Point, rect: Rect) -> bool:
    x, y = point
    x0, y0, x1, y1 = rect
    return x0 <= x <= x1 and y0 <= y <= y1


def _orientation(a: Point, b: Point, c: Point) -> float:
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def _segments_intersect(a: Point, b: Point, c: Point, d: Point) -> bool:
    def on_segment(p: Point, q: Point, r: Point) -> bool:
        return (
            min(p[0], r[0]) <= q[0] <= max(p[0], r[0])
            and min(p[1], r[1]) <= q[1] <= max(p[1], r[1])
        )

    o1 = _orientation(a, b, c)
    o2 = _orientation(a, b, d)
    o3 = _orientation(c, d, a)
    o4 = _orientation(c, d, b)
    if (o1 > 0) != (o2 > 0) and (o3 > 0) != (o4 > 0):
        return True
    eps = 1e-9
    return (
        abs(o1) < eps and on_segment(a, c, b)
        or abs(o2) < eps and on_segment(a, d, b)
        or abs(o3) < eps and on_segment(c, a, d)
        or abs(o4) < eps and on_segment(c, b, d)
    )


def segment_intersects_rect(a: Point, b: Point, rect: Rect) -> bool:
    if point_in_rect(a, rect) or point_in_rect(b, rect):
        return True
    x0, y0, x1, y1 = rect
    edges = [
        ((x0, y0), (x1, y0)),
        ((x1, y0), (x1, y1)),
        ((x1, y1), (x0, y1)),
        ((x0, y1), (x0, y0)),
    ]
    return any(_segments_intersect(a, b, c, d) for c, d in edges)


def rect_from_points(points: Sequence[Point], pad: float = 0) -> Rect:
    return (
        min(p[0] for p in points) - pad,
        min(p[1] for p in points) - pad,
        max(p[0] for p in points) + pad,
        max(p[1] for p in points) + pad,
    )


def expand_rect(rect: Rect, pad: float) -> Rect:
    x0, y0, x1, y1 = rect
    return (x0 - pad, y0 - pad, x1 + pad, y1 + pad)


def point_rect_distance(point: Point, rect: Rect) -> float:
    x, y = point
    x0, y0, x1, y1 = rect
    dx = max(x0 - x, 0, x - x1)
    dy = max(y0 - y, 0, y - y1)
    return math.hypot(dx, dy)


class LayoutGuard:
    """Register layout boxes and fail if readable text collides with graphics."""

    def __init__(self, canvas_size: Tuple[int, int], default_gap: float = 8):
        self.canvas_size = canvas_size
        self.default_gap = default_gap
        self.text_boxes: List[Box] = []
        self.graphic_boxes: List[Box] = []
        self.allowed_backgrounds: List[Box] = []
        self.no_cross_boxes: List[Box] = []
        self.connector_paths: List[Tuple[str, List[Point], float]] = []
        self.connector_bindings: List[Tuple[str, List[Point], Rect, Rect, float]] = []
        self.connector_endpoint_gaps: List[Tuple[str, Point, Rect, float, Optional[float], str]] = []
        self.required_zones: List[Tuple[str, Rect, Rect, float]] = []
        self.semantic_modules: dict[str, Rect] = {}
        self.semantic_placements: List[Tuple[str, str, Rect, float]] = []
        self.vertical_gap_requirements: List[Tuple[str, Rect, Rect, float]] = []
        self.centering_requirements: List[Tuple[str, Rect, Rect, float, float]] = []
        self.inline_centerline_requirements: List[Tuple[str, List[Rect], float]] = []
        self.x_alignment_requirements: List[Tuple[str, List[float], float]] = []

    def add_text_box(self, name: str, rect: Rect, pad: Optional[float] = None) -> Box:
        box = Box("text", name, rect, "text").padded(self.default_gap if pad is None else pad)
        self.text_boxes.append(box)
        return box

    def add_graphic_box(self, name: str, rect: Rect, role: str = "forbidden", pad: float = 0) -> Box:
        box = Box("graphic", name, rect, role).padded(pad)
        if role == "allowed_background":
            self.allowed_backgrounds.append(box)
        else:
            self.graphic_boxes.append(box)
        return box

    def add_panel_edge(self, name: str, rect: Rect, edge_gap: float) -> None:
        x0, y0, x1, y1 = rect
        self.add_graphic_box(f"{name}:left-edge", (x0, y0, x0 + edge_gap, y1))
        self.add_graphic_box(f"{name}:right-edge", (x1 - edge_gap, y0, x1, y1))
        self.add_graphic_box(f"{name}:top-edge", (x0, y0, x1, y0 + edge_gap))
        self.add_graphic_box(f"{name}:bottom-edge", (x0, y1 - edge_gap, x1, y1))

    def add_no_cross_zone(self, name: str, rect: Rect, pad: float = 0) -> Box:
        """Register an image/subject region that connector paths must not cross."""
        box = Box("no_cross", name, rect, "no_cross").padded(pad)
        self.no_cross_boxes.append(box)
        return box

    def add_connector_path(self, name: str, points: Sequence[Point], width: float = 2, pad: float = 6) -> Box:
        """Register a leader/callout path so it can be checked against text and subjects."""
        if len(points) < 2:
            raise ValueError("connector path requires at least two points")
        path = [(float(x), float(y)) for x, y in points]
        clearance = width / 2 + pad
        self.connector_paths.append((name, path, clearance))
        return Box("connector", name, rect_from_points(path, clearance), "connector_path")

    def add_bound_connector_path(
        self,
        name: str,
        points: Sequence[Point],
        label_anchor_zone: Rect,
        target_anchor_zone: Rect,
        width: float = 2,
        pad: float = 6,
        label_keepout_rect: Optional[Rect] = None,
        target_keepout_rect: Optional[Rect] = None,
        min_endpoint_gap: float = 0,
        max_endpoint_gap: Optional[float] = None,
    ) -> Box:
        """Register a connector and verify that it starts/ends in semantic anchor zones.

        Use this for leader lines that must visually connect a label group to a data mark.
        A local legend dot beside a label should not pass this check unless the target
        data mark is genuinely in that same anchor zone. When keepout rects are supplied,
        the connector must stop short of the readable label/target graphic by
        ``min_endpoint_gap`` and remain no farther than ``max_endpoint_gap`` from those
        real endpoint boxes, so it guides without touching or floating away.
        """
        box = self.add_connector_path(name, points, width=width, pad=pad)
        path = [(float(x), float(y)) for x, y in points]
        self.connector_bindings.append((name, path, label_anchor_zone, target_anchor_zone, width / 2 + pad))
        if min_endpoint_gap > 0 and label_keepout_rect is not None:
            self.connector_endpoint_gaps.append((name, path[0], label_keepout_rect, min_endpoint_gap, max_endpoint_gap, "label"))
        if min_endpoint_gap > 0 and target_keepout_rect is not None:
            self.connector_endpoint_gaps.append((name, path[-1], target_keepout_rect, min_endpoint_gap, max_endpoint_gap, "target"))
        return box

    def add_measured_connector_path(
        self,
        name: str,
        points: Sequence[Point],
        label_rect: Rect,
        target_mark_rect: Rect,
        width: float = 2,
        pad: float = 6,
        min_endpoint_gap: float = 8,
        max_endpoint_gap: float = 28,
    ) -> Box:
        """Register a connector using real measured data and mark rectangles.

        Prefer this over hand-authored anchor zones when a connector links a readable
        label/value to a visible graphic mark. The first point must sit near the measured
        label rectangle; the final point must sit near the target mark rectangle. Both
        must be detached by at least ``min_endpoint_gap`` and no farther than
        ``max_endpoint_gap``.
        """
        return self.add_bound_connector_path(
            name=name,
            points=points,
            label_anchor_zone=expand_rect(label_rect, max_endpoint_gap),
            target_anchor_zone=expand_rect(target_mark_rect, max_endpoint_gap),
            width=width,
            pad=pad,
            label_keepout_rect=label_rect,
            target_keepout_rect=target_mark_rect,
            min_endpoint_gap=min_endpoint_gap,
            max_endpoint_gap=max_endpoint_gap,
        )

    def text_bbox(self, draw, xy: Tuple[float, float], text: str, font, anchor: str = "la") -> Rect:
        return draw.textbbox(xy, text, font=font, anchor=anchor)

    def add_text(self, draw, name: str, xy: Tuple[float, float], text: str, font, anchor: str = "la",
                 pad: Optional[float] = None) -> Box:
        return self.add_text_box(name, self.text_bbox(draw, xy, text, font, anchor), pad)

    def assert_inside(self, name: str, outer: Rect, inner: Rect, pad: float) -> None:
        if not contains(outer, inner, pad):
            raise ValueError(f"layout overflow: {name} is outside its reserved zone")

    def require_inside(self, name: str, outer: Rect, inner: Rect, pad: float = 0) -> None:
        self.required_zones.append((name, outer, inner, pad))

    def add_semantic_module(self, name: str, rect: Rect) -> None:
        """Declare the visual territory for a data/story module.

        Use this when geometry alone is not enough: formulas, context notes, source
        phrases, and annotations must belong to the correct parent/child module.
        """
        self.semantic_modules[name] = rect

    def require_semantic_owner(self, item_name: str, module_name: str, item_rect: Rect, pad: float = 0) -> None:
        """Require a text/graphic item to sit inside its declared semantic owner module."""
        if module_name not in self.semantic_modules:
            raise ValueError(f"unknown semantic module: {module_name}")
        self.semantic_placements.append((item_name, module_name, item_rect, pad))

    def require_vertical_gap(self, name: str, upper_rect: Rect, lower_rect: Rect, min_gap: float) -> None:
        """Require measured vertical breathing room between two stacked text blocks."""
        self.vertical_gap_requirements.append((name, upper_rect, lower_rect, min_gap))

    def require_centered_in(
        self,
        name: str,
        container_rect: Rect,
        item_rect: Rect,
        tolerance_x: float = 4,
        tolerance_y: float = 4,
    ) -> None:
        """Require an item bbox to be visually centered in its container bbox."""
        self.centering_requirements.append((name, container_rect, item_rect, tolerance_x, tolerance_y))

    def require_inline_centerline(self, name: str, token_rects: Sequence[Rect], tolerance_y: float = 2) -> None:
        """Require inline formula/mixed-font tokens to share one visual centerline."""
        self.inline_centerline_requirements.append((name, list(token_rects), tolerance_y))

    def require_x_alignment(self, name: str, xs: Sequence[float], tolerance_x: float = 2) -> None:
        """Require several x coordinates to share one declared alignment lane."""
        self.x_alignment_requirements.append((name, list(xs), tolerance_x))

    def require_all_text_inside_canvas(self, pad: float) -> None:
        w, h = self.canvas_size
        canvas = (0, 0, w, h)
        for box in self.text_boxes:
            self.require_inside(f"{box.name} inside canvas", canvas, box.rect, pad)

    def assert_clear(self, extra_forbidden: Sequence[Box] = ()) -> None:
        failures = []
        for name, outer, inner, pad in self.required_zones:
            if not contains(outer, inner, pad):
                failures.append(f"{name} overflows reserved zone")
        for item_name, module_name, item_rect, pad in self.semantic_placements:
            module_rect = self.semantic_modules[module_name]
            if not contains(module_rect, item_rect, pad):
                failures.append(f"{item_name} is outside semantic module {module_name}")
        for name, upper_rect, lower_rect, min_gap in self.vertical_gap_requirements:
            gap = lower_rect[1] - upper_rect[3]
            if gap < min_gap:
                failures.append(f"{name} vertical gap is {gap:.1f}px, below required {min_gap}px")
        for name, container_rect, item_rect, tolerance_x, tolerance_y in self.centering_requirements:
            cx = (container_rect[0] + container_rect[2]) / 2
            cy = (container_rect[1] + container_rect[3]) / 2
            ix = (item_rect[0] + item_rect[2]) / 2
            iy = (item_rect[1] + item_rect[3]) / 2
            if abs(ix - cx) > tolerance_x or abs(iy - cy) > tolerance_y:
                failures.append(
                    f"{name} center offset is ({ix - cx:.1f}px, {iy - cy:.1f}px), "
                    f"beyond tolerance ({tolerance_x}px, {tolerance_y}px)"
                )
        for name, token_rects, tolerance_y in self.inline_centerline_requirements:
            if token_rects:
                centers = [(rect[1] + rect[3]) / 2 for rect in token_rects]
                target = sum(centers) / len(centers)
                for i, center in enumerate(centers):
                    if abs(center - target) > tolerance_y:
                        failures.append(
                            f"{name} token {i} centerline offset is {center - target:.1f}px, "
                            f"beyond tolerance {tolerance_y}px"
                        )
        for name, xs, tolerance_x in self.x_alignment_requirements:
            if xs:
                target = xs[0]
                for i, x in enumerate(xs):
                    if abs(x - target) > tolerance_x:
                        failures.append(
                            f"{name} x lane {i} offset is {x - target:.1f}px, "
                            f"beyond tolerance {tolerance_x}px"
                        )
        forbidden = [*self.graphic_boxes, *extra_forbidden]
        for text_box in self.text_boxes:
            for graphic_box in forbidden:
                if intersects(text_box.rect, graphic_box.rect):
                    failures.append(f"{text_box.name} overlaps {graphic_box.name}")
        for connector_name, points, clearance in self.connector_paths:
            for start, end in zip(points, points[1:]):
                for text_box in self.text_boxes:
                    if segment_intersects_rect(start, end, text_box.padded(clearance).rect):
                        failures.append(f"{connector_name} crosses text {text_box.name}")
                for no_cross in self.no_cross_boxes:
                    if segment_intersects_rect(start, end, no_cross.padded(clearance).rect):
                        failures.append(f"{connector_name} crosses no-cross zone {no_cross.name}")
        for connector_name, points, label_zone, target_zone, clearance in self.connector_bindings:
            if not point_in_rect(points[0], label_zone):
                failures.append(f"{connector_name} does not start in its label anchor zone")
            if not point_in_rect(points[-1], target_zone):
                failures.append(f"{connector_name} does not end in its target anchor zone")
            if contains(label_zone, target_zone) or contains(target_zone, label_zone):
                failures.append(f"{connector_name} label and target zones collapse into one local marker")
        for connector_name, point, keepout, min_gap, max_gap, endpoint_name in self.connector_endpoint_gaps:
            distance = point_rect_distance(point, keepout)
            if distance < min_gap:
                failures.append(
                    f"{connector_name} {endpoint_name} endpoint is closer than {min_gap}px to its keepout zone"
                )
            if max_gap is not None and distance > max_gap:
                failures.append(
                    f"{connector_name} {endpoint_name} endpoint is farther than {max_gap}px from its keepout zone"
                )
        if failures:
            joined = "\n".join(f"  - {f}" for f in failures)
            raise ValueError("layout collision check failed:\n" + joined)


def union_rect(rects: Iterable[Rect]) -> Rect:
    rects = list(rects)
    if not rects:
        raise ValueError("union_rect requires at least one rect")
    return (
        min(r[0] for r in rects),
        min(r[1] for r in rects),
        max(r[2] for r in rects),
        max(r[3] for r in rects),
    )
