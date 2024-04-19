def merge_sorted_array(nums1, nums2):
    nums1.extend(nums2)
    nums1.sort()

nums1 = input("Enter the first sorted array separated by spaces: ").split()
nums1 = [int(num) for num in nums1]
nums2 = input("Enter the second sorted array separated by spaces: ").split()
nums2 = [int(num) for num in nums2]
merge_sorted_array(nums1, nums2)
print("Merged and sorted array:", nums1)
