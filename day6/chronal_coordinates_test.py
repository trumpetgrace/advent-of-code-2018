from chronal_coordinates import largest_area, largest_region_within_distance

test_data = ["1, 1", "1, 6", "8, 3", "3, 4", "5, 5", "8, 9"]


def test_largest_area():
    assert largest_area(test_data) == 17


def test_largest_region_within_distance():
    distance = 32
    assert largest_region_within_distance(test_data, distance) == 16
