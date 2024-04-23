# https://leetcode.com/problems/longest-common-prefix/description/

# Time Complexity: O(n^2)
def longestCommonPrefix(strs: List[str]) -> str:
	# Sets the prefix as the entire first word
	# as the end will slowly get chopped off
	# until it finds a prefix that matches.
    prefix = strs[0]
    # Only need to check the prefix of two of the items in the list
    # as it wants to find the common for all items in the list.
    # So by comparing just two words, we can find the longest prefix.
    for s in strs[1:]:
        # using the find method, returning a negative would mean there's no common prefix.
        # chops off the end if it doesn't find a prefix.
        # 0 would mean the first letters are the same as it's returning the first index it finds
        # that matches.
        while s.find(prefix) != 0:
            prefix = prefix[:-1]
    return prefix