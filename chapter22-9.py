class Solution:
    def removeElement(self, nums, val) -> int:
        """
        type nums: List[int]
        type val : int
        """
        while val in nums:
            nums.remove(val)
        return

if __name__ == "__main__":
    s = Solution()
    num = [0, 1, 2, 2, 3, 0, 4, 2]
    val = 2
    print(s.removeElement(num, val))
    print(num)


