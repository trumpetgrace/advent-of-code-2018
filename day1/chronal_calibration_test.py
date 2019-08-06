from chronal_calibration import resulting_frequency, repeated_frequency


def test_resulting_frequency():
    freq = [5, -5, 10, -4, 9]
    assert resulting_frequency(freq) == 15


def test_repeated_frequency():
    freq = [5, 1, -1, -5, 10]
    assert repeated_frequency(freq) == 5
