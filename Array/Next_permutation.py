class Solution(object):
    def nextPermutation(self, nums):
        i = len(nums) - 2
        while i > 0 and nums[i] > nums[i+1]:
            i -= 1

        if i >= 0:
            j = len(nums) - 1
            while nums[j] < nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]

        left, right = i+1, len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
# sol = Solution()
# print(sol.nextPermutation([1,3,5,4,2]))
nums = [1,3,5,4,2]
sol = Solution()
sol.nextPermutation(nums)
print(nums)  # ✅ In ra kết quả sau khi hoán vị
