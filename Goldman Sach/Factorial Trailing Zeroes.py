#https://leetcode.com/problems/factorial-trailing-zeroes/
class Solution:
    def trailingZeroes(self, n: int) -> int:
        ans=0
        i=1
        temp=5
        while temp<=n:
            ans+=(n//temp)
            i+=1
            temp=5**i
        return ans