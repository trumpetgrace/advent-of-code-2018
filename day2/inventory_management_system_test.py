from inventory_management_system import calculate_checksum, common_letters


def test_calculate_checksum():
    test_data = ["abcdef", "bababc", "abbcde", "abcccd", "aabcdd", "abcdee", "ababab"]
    assert calculate_checksum(test_data) == 12


def test_common_letters():
    test_data = ["abcde", "fghij", "pqrst", "fguij", "axcye", "wvxyz"]
    assert common_letters(test_data) == "fgij"
