from code_challenges.two_sum import two_sum
# pytest tests/two_sum_tests.py


def test_target_1():
    nums = [1, 3, 5]
    target = 6

    actual = two_sum(nums, target)
    expected = [2, 0]

    assert expected == actual


def test_target_2():
    nums = [1, 2, 3]
    target = 3

    actual = two_sum(nums, target)
    expected = [0, 1]

    assert expected == actual


def test_target_3():
    nums = [40, 100, 68, 34]
    target = 74

    actual = two_sum(nums, target)
    expected = [0, 3]

    assert expected == actual
