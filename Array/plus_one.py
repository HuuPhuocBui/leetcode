class Solution(object):
    def plusOne(self, digits):
        n = len(digits)
        
        for i in range(n - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits  # ✅ không cần xử lý thêm
            digits[i] = 0  # reset và tiếp tục cộng lên trên
        
        # Nếu tất cả đều là 9 → cần thêm 1 ở đầu
        return [1] + digits
sol = Solution()
print(sol.plusOne([9,9,8]))