class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        left_pointer = 0
        char_set = set()
        current_max = 0
        
        for right_pointer in range(0, len(s)):
            if s[right_pointer] not in char_set:
                char_set.update(s[right_pointer])
        
                current_max = max(current_max, len(char_set))
            else:
                while(s[right_pointer] in char_set):
                    char_set.remove(s[left_pointer])
                    left_pointer += 1
                char_set.update(s[right_pointer])
                    
        return current_max


                
        