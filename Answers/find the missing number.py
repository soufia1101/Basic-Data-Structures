def find_missing_number(nums):
    n = len(nums)
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum

input_nums = input("Enter the numbers separated by spaces: ").split()
input_nums = [int(num) for num in input_nums]
print("Missing number is:", find_missing_number(input_nums))
