from chronal_calibration import resulting_frequency, repeated_frequency

test_data = freq = [5, 1, -1, -5, 10]


def test_resulting_frequency():
    assert resulting_frequency(test_data) == 10


def test_repeated_frequency():
    assert repeated_frequency(test_data) == 5
