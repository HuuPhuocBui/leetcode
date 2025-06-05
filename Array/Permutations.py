class Solution(object):
    def permute(self, nums):
        result = []
        
        def backtrack(start):
            if start == len(nums):
                result.append(nums[:])  # tạo bản sao của mảng hiện tại
                return
            for i in range(start, len(nums)):
                nums[start], nums[i] = nums[i], nums[start]  # hoán đổi
                backtrack(start + 1)
                nums[start], nums[i] = nums[i], nums[start]  # hoàn tác (backtrack)

        backtrack(0)
        return result

# Ví dụ sử dụng
sol = Solution()
print(sol.permute([1, 2, 3]))
