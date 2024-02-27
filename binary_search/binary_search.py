def binary_search(nums,target):
    lower = 0
    higher = len(nums) - 1

    while lower <= higher:
        middle = (lower + higher) // 2
        guess = nums[middle]

        if guess == target:
            return middle
        elif guess > target:
            higher = middle - 1
        else:
            lower = middle + 1
    return None
