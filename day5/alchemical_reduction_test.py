from alchemical_reduction import units_after_reaction, shortest_polymer

test_data = "dabAcCaCBAcCcaDA"


def test_units_after_reaction():
    assert units_after_reaction(test_data) == 10


def test_shortest_polymer():
    assert shortest_polymer(test_data) == 4
