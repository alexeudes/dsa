def selection_sort(nums:list):
    new_array = []

    for i in range(len(nums)):
        lowest = find_lower_value(nums)
        new_array.append(nums.pop(lowest))
    return new_array

def find_lower_value(nums):
    lower = nums[0]
    lower_index = 0

    for i in range(1, len(nums)):
        if nums[i] < lower:
            lower = nums[i]
            lower_index = i
    return lower_index
