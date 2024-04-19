def find_missing_number(nums):
    n = len(nums)
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum


input_nums = input("Enter the numbers separated by spaces: ").split()
input_nums = [int(num) for num in input_nums]
print("Missing number is:", find_missing_number(input_nums))

def rotate_array(nums, k):
    n = len(nums)
    k = k % n
    nums[:] = nums[-k:] + nums[:-k]

input_nums = input("Enter the numbers separated by spaces: ").split()
input_nums = [int(num) for num in input_nums]
k = int(input("Enter the number of positions to rotate: "))
rotate_array(input_nums, k)
print("Rotated array:", input_nums)

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

def merge_sorted_array(nums1, nums2):
    nums1.extend(nums2)
    nums1.sort()
nums1 = input("Enter the first sorted array separated by spaces: ").split()
nums1 = [int(num) for num in nums1]
nums2 = input("Enter the second sorted array separated by spaces: ").split()
nums2 = [int(num) for num in nums2]
merge_sorted_array(nums1, nums2)
print("Merged and sorted array:", nums1)

def max_subarray_sum(nums):
    max_sum = current_sum = nums[0]
    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum
input_nums = input("Enter the numbers separated by spaces: ").split()
input_nums = [int(num) for num in input_nums]
print("Maximum subarray sum:", max_subarray_sum(input_nums))

class SparseMatrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def transpose(self):
        rows, cols = len(self.matrix), len(self.matrix[0])
        transposed = [[self.matrix[j][i] for j in range(rows)] for i in range(cols)]
        self.matrix = transposed

    def change_element(self, row, col, value):
        self.matrix[row][col] = value

rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))
matrix = []
for i in range(rows):
    row = input(f"Enter the elements of row {i+1} separated by spaces: ").split()
    matrix.append([int(x) for x in row])

sparse = SparseMatrix(matrix)
row, col, value = map(int, input("Enter row, column, and new value to change an element (separated by spaces): ").split())
sparse.change_element(row, col, value)
sparse.transpose()
print("Transposed matrix with changed element:", sparse.matrix)

