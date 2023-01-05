#Leetcode 2344
#https://leetcode.com/problems/minimum-deletions-to-make-array-divisible/description/
class Solution:
    def minOperations(self, nums: List[int], numsDivide: List[int]) -> int:
        gcd=numsDivide[0]
        for i in numsDivide[1:]:
            gcd=math.gcd(gcd,i)
        nums.sort()
       # print(nums,gcd)
        for i in range(len(nums)):
            if gcd%nums[i]==0:
                return i
            elif nums[i]>gcd:
                return -1
            continue
        return -1
        # if gcd not in nums:
        #     return -1
        # return bisect.bisect_left(nums,gcd)