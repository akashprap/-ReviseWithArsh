#Leetcode 1227
#https://leetcode.com/problems/airplane-seat-assignment-probability/description/
class Solution:
    def nthPersonGetsNthSeat(self, n: int) -> float:
        return 0.5 if n!=1 else 1