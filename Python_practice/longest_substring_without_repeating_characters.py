from collections import defaultdict
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        dict_str_possibilities = defaultdict(list)

        while(True):
        for ind, str_len in enumerate(range(1, len(str))):
            substr = s[ind:ind+len]
            print(substr)

        return len_substr
        
def main():
    og_string = input('Enter the string')
    
    sol = Solution()
    sol.lengthOfLongestSubstring(og_string)