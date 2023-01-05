#Leetcode 1358
#https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/description/
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        a = b = c = 0                        # counter for letter a/b/c
        ans, i, n = 0, 0, len(s)             # i: slow pointer
        for j, letter in enumerate(s):       # j: fast pointer
            if letter == 'a': a += 1         
            elif letter == 'b': b += 1
            else: c += 1
            while a > 0 and b > 0 and c > 0: 
                ans += n-j                   
                if s[i] == 'a': a -= 1       
                elif s[i] == 'b': b -= 1
                else: c -= 1
                i += 1
            
                                       
        return ans    