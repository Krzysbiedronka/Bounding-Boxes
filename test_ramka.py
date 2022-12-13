from ramka import BoundingBox
from pytest import raises, approx


def test_create_typical_bounding_box():
    frame = BoundingBox((0, 0), (10, 10))
    assert frame.bottom_left == (0, 0)
    assert frame.upper_right == (10, 10)


def test_create_invalid_bounding_box():
    with raises(ValueError):
        BoundingBox((0, 0), (10, -10))


def test_create_to_large_bounding_box():
    with raises(ValueError):
        BoundingBox((0, 0), (2000, 10))


def test_area():
    frame = BoundingBox((0, 0), (10, 10))
    assert frame.area() == 100


def test_area_different_frame():
    frame = BoundingBox((20, 20), (0, 0))
    assert frame.area() == 400


def test_intersection_area_typical():
    frame1 = BoundingBox((0, 0), (10, 10))
    frame2 = BoundingBox((0, 1), (10, 11))
    assert frame1.intersection_area(frame2) == 90


def test_intersection_area_same_frame():
    frame1 = BoundingBox((0, 0), (10, 10))
    frame2 = BoundingBox((0, 0), (10, 10))
    assert frame1.intersection_area(frame2) == 100


def test_intersection_area_frame_in_frame():
    frame1 = BoundingBox((0, 0), (10, 10))
    frame2 = BoundingBox((2, 2), (5, 5))
    assert frame1.intersection_area(frame2) == 9


def test_intersection_area_frame_outside_frame():
    frame1 = BoundingBox((0, 0), (4, 4))
    frame2 = BoundingBox((5, 0), (9, 4))
    assert frame1.intersection_area(frame2) == 0


def test_intersection_area_frame_outside_frame_another():
    frame1 = BoundingBox((5, 5), (9, 9))
    frame2 = BoundingBox((0, 0), (4, 4))
    assert frame1.intersection_area(frame2) == 0


def test_intersection_area_frame_touching_frame_by_side():
    frame1 = BoundingBox((1, 1), (3, 3))
    frame2 = BoundingBox((3, 1), (5, 3))
    assert frame1.intersection_area(frame2) == 0


def test_intersection_area_frame_touching_frame_by_top():
    frame1 = BoundingBox((1, 1), (3, 3))
    frame2 = BoundingBox((3, 0), (4, 1))
    assert frame1.intersection_area(frame2) == 0


def test_union_area_typical():
    frame1 = BoundingBox((0, 0), (10, 10))
    frame2 = BoundingBox((0, 1), (10, 11))
    assert frame1.union_area(frame2) == 110


def test_union_area_frame_outside_frame():
    frame1 = BoundingBox((1, 3), (3, 5))
    frame2 = BoundingBox((4, 1), (5, 2))
    assert frame1.union_area(frame2) == 5


def test_union_area_frame_inside_frame():
    frame1 = BoundingBox((1, 3), (3, 5))
    frame2 = BoundingBox((1, 3), (2, 4))
    assert frame1.union_area(frame2) == 4


def test_ratio_typical():
    frame1 = BoundingBox((0, 0), (10, 10))
    frame2 = BoundingBox((0, 1), (10, 11))
    assert frame1.intersection_to_union_ratio(frame2) == approx(0.8182, 0.0001)


def test_ratio_when_interestion_equals_zero():
    frame1 = BoundingBox((1, 1), (3, 3))
    frame2 = BoundingBox((3, 3), (4, 4))
    assert frame1.intersection_to_union_ratio(frame2) == 0


def test_ratio_when_union_equals_zeio():
    frame1 = BoundingBox((1, 1), (1, 1))
    frame2 = BoundingBox((3, 3), (3, 3))
    with raises(ZeroDivisionError):
        frame1.intersection_to_union_ratio(frame2)


def test_f1():
    frame1 = BoundingBox((0, 0), (10, 10))
    frame2 = BoundingBox((0, 1), (10, 11))
    assert frame1.f1_coefficient(frame2) == 0.9


def test_str():
    frame1 = BoundingBox((0, 0), (10, 10))
    assert str(frame1) == 'x1: 0, y1: 0, x2: 0, y2: 10, x3: 10, y3: 10, x4: 10, y4: 0'
