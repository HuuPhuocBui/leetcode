class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        
        k = 1  # Con trỏ k bắt đầu từ 1 vì phần tử đầu tiên luôn là duy nhất
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:  # Nếu phần tử hiện tại khác phần tử trước đó
                nums[k] = nums[i]       # Di chuyển phần tử duy nhất đến vị trí k
                k += 1                  # Tăng k lên 1
        return k
sol = Solution()
print(sol.removeDuplicates([1,1,2,3,4,4,5]))
