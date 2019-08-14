class Solution:
    def twoSum(self, nums: [int], target: int) -> [int]:
        list = []
        temp_range = len(nums)
        for i in range(temp_range):
            target_value = target - nums[i]
            for j in range(temp_range):
                if j == i:
                    continue
                if target_value == nums[j]:
                    list.append(i)
                    list.append(j)
                    return list

if __name__ == "__main__":
    sol = Solution()
    list = [-1, -2, -3, -4, -5]
    print(sol.twoSum(list, -8))
