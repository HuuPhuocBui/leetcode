class Solution(object):
    def singleNumber(self, nums):
        result = 0
        for num in nums:
            result ^= num
        return result

# Ví dụ sử dụng
sol = Solution()
print(sol.singleNumber([2, 2, 3]))  # Output: 1
# phép xor