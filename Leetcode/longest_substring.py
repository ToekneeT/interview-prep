# https://leetcode.com/problems/longest-substring-without-repeating-characters/
def lengthOfLongestSubstring(s):
    longest_sub = 0
    seen = set()
    for i in range(len(s)):
        seen.clear()
        next_index = i
        while next_index < len(s):
            if s[next_index] in seen:
                break
            seen.add(s[next_index])
            next_index += 1
        longest_sub = max(longest_sub, next_index - i)
    return longest_sub

print(lengthOfLongestSubstring("au")) # 2
print(lengthOfLongestSubstring("")) # 0
print(lengthOfLongestSubstring(" ")) # 1
print(lengthOfLongestSubstring("abcabcbb")) # 3
print(lengthOfLongestSubstring("bbbbb")) # 1
print(lengthOfLongestSubstring('pwwkew')) # 3