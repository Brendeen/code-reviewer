
def two_sum(nums, target):
    if not nums:
        return "empty list"

    for i1, n1 in enumerate(nums):
        for i2 in range(len(nums) - 1):
            if i1 == i2:
                continue
            if n1 + nums[i2] == target:
                return [i1, i2]
            # print([i1, i2])

