def rotate_array(nums, k):
    n = len(nums)
    k = k % n
    nums[:] = nums[-k:] + nums[:-k]

input_nums = input("Enter the numbers separated by spaces: ").split()
input_nums = [int(num) for num in input_nums]
k = int(input("Enter the number of positions to rotate: "))
rotate_array(input_nums, k)
print("Rotated array:", input_nums)
