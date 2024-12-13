def two_sum(nums, target):
    indexlar = []
    for i in range(len(nums)):
        print(nums[i])
        for j in range(len(nums)):
            if i != j:
                if (nums[i] + nums[j]) == target:
                    indexlar.extend([i, j])
                    return indexlar
print(two_sum([3,3],6))
