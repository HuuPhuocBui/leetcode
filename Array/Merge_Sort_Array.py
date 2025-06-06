class Solution(object):
    def merge(self, nums1, m, nums2, n):
        i = m - 1
        j = n - 1
        k = m + n - 1

        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1
sol = Solution()
nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
sol.merge(nums1, 1, nums2, 3)
print(nums1)  # Output: [1,2,2,3,5,6]
