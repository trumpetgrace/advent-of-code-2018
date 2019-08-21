from no_matter_how_you_slice_it import overlapping_claims, intact_claim

test_data = ["#1 @ 1,3: 4x4", "#2 @ 3,1: 4x4", "#3 @ 5,5: 2x2"]


def test_overlapping_claims():
    assert overlapping_claims(test_data) == 4


def test_intact_claim():
    assert intact_claim(test_data) == 3
