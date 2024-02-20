numbers = [1, 2, 4]
targ = 5
temp = 100


def two_sum(nums, target):
    if nums == []:
        return "Empty list"
    for num in nums:
        current_index = nums.index(num)  # records current integer number
        for i in range(current_index + 1, len(nums)):
            if nums.index(i) == current_index:
                continue
            elif current_index + i == target:
                return [current_index, i]
    return "Empty list"


two_sum(numbers, targ)
