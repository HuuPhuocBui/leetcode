class Solution(object):
    def threeSum(self, nums):
        res = []
        nums.sort()  # Bước 1: Sắp xếp mảng

        for i in range(len(nums)):
            # Bỏ qua các phần tử trùng nhau để tránh kết quả trùng
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Dùng kỹ thuật hai con trỏ
            left, right = i + 1, len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total < 0:
                    left += 1  # Cần tăng tổng => tăng left
                elif total > 0:
                    right -= 1  # Cần giảm tổng => giảm right
                else:
                    # Tổng bằng 0 => lưu kết quả
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    # Bỏ qua trùng lặp ở left và right
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

        return res
sol = Solution()
print(sol.threeSum([-1, 0, 1, 2, -1, -4]))
# Output: [[-1, -1, 2], [-1, 0, 1]]
