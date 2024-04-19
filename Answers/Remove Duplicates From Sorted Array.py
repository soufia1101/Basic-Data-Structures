def remove_duplicates(nums):
    if not nums:
        return 0
    write_index = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            nums[write_index] = nums[i]
            write_index += 1
    return write_index

input_nums = input("Enter the sorted numbers separated by spaces: ").split()
input_nums = [int(num) for num in input_nums]
new_length = remove_duplicates(input_nums)
print("New length after removing duplicates:", new_length)
