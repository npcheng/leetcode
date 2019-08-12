class Solution(object):
    def twoSum(self, nums, target: int):
        tSum = {}
        for index, num in enumerate(nums):
            if tSum.get(target - num) is not None:
                return  [index, tSum[target-num]]
            else:
                tSum[num] = index
    
if __name__ == "__main__":
    nums_list = [2,3,4,5,6,7]
    t = 12
    s = Solution()
    print(s.twoSum(nums_list, t))