from main import (
    pairs_only,
    sum_array,
    max_number,
    smallest_pair,
    remove_duplicates,
    average_array,
    reverse_array,
)


def test_pairs_only():
    assert pairs_only([1, 2, 3, 4, 5, 6]) == [2, 4, 6]
    assert pairs_only([]) == []
    assert pairs_only([1, 3, 5]) == []


def test_sum_array():
    assert sum_array([1, 2, 3, 4]) == 10
    assert sum_array([]) == 0
    assert sum_array([-1, 1]) == 0


def test_max_number():
    assert max_number([[1, 2], [3, 4]]) == 4
    assert max_number([[1]]) == 1
    assert max_number([[]]) == 0


def test_smallest_pair():
    assert smallest_pair([[1, 2], [3, 4]]) == 2
    assert smallest_pair([[1, 3], [5, 7]]) == 0
    assert smallest_pair([[]]) == 0


def test_remove_duplicates():
    assert sorted(remove_duplicates([1, 2, 2, 3, 3, 4])) == [1, 2, 3, 4]
    assert remove_duplicates([1, 1, 1]) == [1]
    assert remove_duplicates([]) == []


def test_average_array():
    assert average_array([1, 2, 3, 4]) == 2.5
    assert average_array([]) == 0.0
    assert average_array([5]) == 5.0


def test_reverse_array():
    assert reverse_array([1, 2, 3]) == [3, 2, 1]
    assert reverse_array([]) == []
    assert reverse_array([1]) == [1]
