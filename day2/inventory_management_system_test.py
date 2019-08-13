from inventory_management_system import calculate_checksum, common_letters


def test_calculate_checksum():
    box_ids = ["abcdef", "bababc", "abbcde", "abcccd", "aabcdd", "abcdee", "ababab"]
    assert calculate_checksum(box_ids) == 12


def test_common_letters():
    box_ids = ["abcde", "fghij", "pqrst", "fguij", "axcye", "wvxyz"]
    assert common_letters(box_ids) == "fgij"