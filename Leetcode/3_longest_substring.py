# https://leetcode.com/problems/longest-substring-without-repeating-characters/
def lengthOfLongestSubstring(s):
    longest_sub = 0
    seen = set()
    # First letter of the sequence.
    for i in range(len(s)):
        # Clears the set for a new group of seen letters.
        seen.clear()
        next_index = i
        # Will move to the next letter until it sees one
        # that has already been added to the set.
        while next_index < len(s):
            # If the letter has already been seen, then
            #it'll break out and start a new sequence.
            if s[next_index] in seen:
                break
            seen.add(s[next_index])
            next_index += 1

        # After breaking, it'll check if the previous
        # longest sequence is less than the current
        # one. next_index - i should be the length
        # of the current sequence.
        if longest_sub < next_index - i:
            longest_sub = next_index - i
    return longest_sub

print(lengthOfLongestSubstring("au")) # 2
print(lengthOfLongestSubstring("")) # 0
print(lengthOfLongestSubstring(" ")) # 1
print(lengthOfLongestSubstring("abcabcbb")) # 3
print(lengthOfLongestSubstring("bbbbb")) # 1
print(lengthOfLongestSubstring('pwwkew')) # 3