from the_sum_of_its_parts import order_of_steps, time_to_complete_steps

test_data = ["Step C must be finished before step A can begin.",
             "Step C must be finished before step F can begin.",
             "Step A must be finished before step B can begin.",
             "Step A must be finished before step D can begin.",
             "Step B must be finished before step E can begin.",
             "Step D must be finished before step E can begin.",
             "Step F must be finished before step E can begin."]


def test_order_of_steps():
    assert order_of_steps(test_data) == "CABDFE"


def test_time_to_complete_steps():
    assert time_to_complete_steps(test_data, 2, True) == 15
