class Solution(object):
    def removeElement(self, nums, val):
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k
sol = Solution()
print(sol.removeElement([0,1,2,2,3,0,4,2],2))