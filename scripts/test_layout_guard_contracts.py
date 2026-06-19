#!/usr/bin/env python3
from __future__ import annotations

from layout_guard import LayoutGuard


def expect_failure(name: str, fn) -> None:
    try:
        fn()
    except ValueError as exc:
        print(f"PASS {name}: {str(exc).splitlines()[0]}")
        return
    raise AssertionError(f"expected failure did not occur: {name}")


def test_footer_distance_guard() -> None:
    guard = LayoutGuard((2400, 1350))
    guard.require_bottom_distance("bad footer", (120, 1260, 640, 1295), distance=50, tolerance=1)
    expect_failure("footer distance", guard.assert_clear)


def test_connector_edge_gap_guard() -> None:
    guard = LayoutGuard((2400, 1350))
    guard.require_connector_edge_gap_group(
        "bad leader edge gaps",
        [
            ((100, 88), (100, 100)),
            ((200, 170), (200, 200)),
        ],
        expected_gap=12,
        tolerance=1,
        equal_tolerance=1,
    )
    expect_failure("connector edge gap", guard.assert_clear)


def test_peer_treatment_guard() -> None:
    guard = LayoutGuard((2400, 1350))
    guard.require_peer_treatment_group("bad peer treatment", ["label_rail", "label_rail", "badge"])
    expect_failure("peer treatment", guard.assert_clear)


def main() -> None:
    test_footer_distance_guard()
    test_connector_edge_gap_guard()
    test_peer_treatment_guard()
    print("layout guard contract tests passed")


if __name__ == "__main__":
    main()
