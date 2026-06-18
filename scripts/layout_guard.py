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


def rects_clear(a: Rect, b: Rect, min_gap: float = 0) -> bool:
    """Return True when two rects do not touch and keep a minimum clear gap."""
    return not intersects(expand_rect(a, min_gap), b)


def _interval_overlap(a0: float, a1: float, b0: float, b1: float) -> float:
    return max(0.0, min(a1, b1) - max(a0, b0))


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
        self.rect_clearance_requirements: List[Tuple[str, Rect, Rect, float]] = []
        self.soft_grouping_fields: List[Box] = []
        self.divider_lines: List[Tuple[str, Point, Point, float, str, float]] = []
        self.text_containers: dict[str, Tuple[Rect, float]] = {}

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

    def add_soft_grouping_field(self, name: str, rect: Rect, pad: float = 0) -> Box:
        """Register a soft color/texture/whitespace field that already separates content.

        Use this for alternating row bands, soft section fields, image crop regions, and
        pale module backgrounds. Decorative separator lines drawn across or along these
        fields are treated as redundant unless the line has a distinct semantic role.
        """
        box = Box("soft_grouping_field", name, rect, "soft_grouping_field").padded(pad)
        self.soft_grouping_fields.append(box)
        return box

    def add_text_container(
        self,
        name: str,
        rect: Rect,
        min_padding: float,
        soft_grouping: bool = True,
    ) -> Box:
        """Register a container that owns readable text.

        Unlike a soft grouping field, this creates an explicit text-safe area. Renderers
        should pair it with ``require_text_stack_inside_container`` for every header,
        row label, value cell, badge, pill, or table cell that contains readable text.
        """
        self.text_containers[name] = (rect, min_padding)
        if soft_grouping:
            return self.add_soft_grouping_field(name, rect)
        return Box("text_container", name, rect, "text_container")

    def require_text_stack_inside_container(
        self,
        name: str,
        container_name: str,
        text_rects: Sequence[Rect],
        pad: Optional[float] = None,
    ) -> None:
        """Require a measured group of text boxes to stay inside an owned container."""
        if container_name not in self.text_containers:
            raise ValueError(f"unknown text container: {container_name}")
        rects = list(text_rects)
        if not rects:
            raise ValueError("text stack requires at least one rect")
        container_rect, default_pad = self.text_containers[container_name]
        self.require_inside(name, container_rect, union_rect(rects), default_pad if pad is None else pad)

    def add_divider_line(
        self,
        name: str,
        start: Point,
        end: Point,
        width: float = 1,
        semantic_role: str = "decorative",
        boundary_tolerance: float = 6,
    ) -> Box:
        """Register a visible divider/rule line for redundancy checks.

        ``semantic_role`` should describe why the line exists. Roles such as ``axis``,
        ``zero_axis``, ``benchmark``, ``threshold``, ``measurement_reference``, and
        ``connector`` are allowed to cross soft fields. Decorative row rules, panel
        dividers, and separator strokes are rejected when a registered soft field already
        provides the grouping.
        """
        p0 = (float(start[0]), float(start[1]))
        p1 = (float(end[0]), float(end[1]))
        self.divider_lines.append((name, p0, p1, width, semantic_role, boundary_tolerance))
        return Box("divider_line", name, rect_from_points([p0, p1], width / 2), semantic_role)

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

    def require_rect_clearance(self, name: str, rect_a: Rect, rect_b: Rect, min_gap: float = 0) -> None:
        """Require two arbitrary rects to stay apart by a minimum clear gap.

        Use this for neighboring row backgrounds, card surfaces, value cells, text stacks,
        and soft color bands that should not touch even when they do not overlap a chart
        mark. This catches edge-kissing between pale containers and adjacent text.
        """
        self.rect_clearance_requirements.append((name, rect_a, rect_b, min_gap))

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
        for name, rect_a, rect_b, min_gap in self.rect_clearance_requirements:
            if not rects_clear(rect_a, rect_b, min_gap):
                failures.append(f"{name} clearance is below required {min_gap}px")
        for container_name, (container_rect, min_padding) in self.text_containers.items():
            for text_box in self.text_boxes:
                if intersects(text_box.rect, container_rect) and not contains(container_rect, text_box.rect, min_padding):
                    failures.append(
                        f"{text_box.name} is inside text container {container_name} "
                        f"without required {min_padding}px padding"
                    )
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
        semantic_line_roles = {
            "axis",
            "zero_axis",
            "benchmark",
            "threshold",
            "measurement_reference",
            "callout",
            "connector",
            "leader",
            "semantic",
        }
        for line_name, start, end, width, semantic_role, tolerance in self.divider_lines:
            if semantic_role in semantic_line_roles:
                continue
            x0, y0 = start
            x1, y1 = end
            is_horizontal = abs(y0 - y1) <= max(1.0, width)
            is_vertical = abs(x0 - x1) <= max(1.0, width)
            if not is_horizontal and not is_vertical:
                continue
            line_length = math.hypot(x1 - x0, y1 - y0)
            if line_length <= 0:
                continue
            for field in self.soft_grouping_fields:
                fx0, fy0, fx1, fy1 = field.rect
                if is_horizontal:
                    lx0, lx1 = sorted((x0, x1))
                    overlap = _interval_overlap(lx0, lx1, fx0, fx1)
                    enough_overlap = overlap >= min(line_length, fx1 - fx0) * 0.45
                    line_y = (y0 + y1) / 2
                    crosses_field = fy0 - tolerance <= line_y <= fy1 + tolerance
                    if enough_overlap and crosses_field:
                        failures.append(
                            f"{line_name} is a redundant horizontal divider over soft grouping field {field.name}"
                        )
                if is_vertical:
                    ly0, ly1 = sorted((y0, y1))
                    overlap = _interval_overlap(ly0, ly1, fy0, fy1)
                    enough_overlap = overlap >= min(line_length, fy1 - fy0) * 0.45
                    line_x = (x0 + x1) / 2
                    crosses_field = fx0 - tolerance <= line_x <= fx1 + tolerance
                    if enough_overlap and crosses_field:
                        failures.append(
                            f"{line_name} is a redundant vertical divider over soft grouping field {field.name}"
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
