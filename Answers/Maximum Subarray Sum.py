def max_subarray_sum(nums):
    max_sum = current_sum = nums[0]
    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum

input_nums = input("Enter the numbers separated by spaces: ").split()
input_nums = [int(num) for num in input_nums]
print("Maximum subarray sum:", max_subarray_sum(input_nums))
