class Solution:
    def removeDuplicates(self, nums) -> int:
        temp_nums = list(set(nums))
        temp_nums.sort()
        nums.clear()
        for i in temp_nums:
            nums.append(i)
        return len(nums)

if __name__ == "__main__":
    s = Solution()
    num = [1, 1, 2, 3, 3, 4, 4, 5]
    print(s.removeDuplicates(num))
    print(num)
