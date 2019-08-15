from no_matter_how_you_slice_it import overlapping_claims, intact_claim


def test_overlapping_claims():
    claims = ["#1 @ 1,3: 4x4", "#2 @ 3,1: 4x4", "#3 @ 5,5: 2x2"]
    assert overlapping_claims(claims) == 4


def test_intact_claim():
    claims = ["#1 @ 1,3: 4x4", "#2 @ 3,1: 4x4", "#3 @ 5,5: 2x2"]
    assert intact_claim(claims) == 3
