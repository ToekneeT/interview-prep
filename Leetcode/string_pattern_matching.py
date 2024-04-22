import unittest
# Given two strings, a pattern and a target, compare them and make sure that
# the pattern can be found within target, return true if it does, false otherwise.
# There can be special cases where a character will change the functionality
# of the problem. e.x. a ? means that the character in that position in target can be
# replaced with anything.
def match(pattern: str, target: str) -> bool:
	# When there's an asterisks, the target can be of any length.
	# When there's an exclamation point, the length should be at least
	# one extra character in the target, but can have more.
	if pattern.find("*") == -1 and pattern.find("!") == -1 and len(pattern) != len(target):
		return False

	for i in range(len(pattern)):
		# If the pattern has an exclamation point, then the following character has to match.
		# This means that the next character can be one of the special cases, i.e. *, ?,
		# but, it wont actually do that special case, only making sure that the characters match.
		# This can mean that the length of pattern can be larger than target.
		# e.x. pattern = h!ello, target = hello
		# Because we're checking the next character, there can be a case where the exclamation is at
		# the very end of input, so we must make sure i + 1 is never over the length of pattern.
		# Similar to how the special case for the asterisks is done, after checking the character
		# after the exclamation, we can ignore all the previous characters. This is done by truncating
		# the character that we matched and all of the previous characters before that.
		if i + 1 < len(pattern) and pattern[i] == "!" and pattern[i + 1] == target[i]:
			if match(pattern[i + 2:], target[i + 1:]):
				return True
			return False
		elif pattern[i] == "*":
			# Slice off the portion before the asterisks in the pattern as the beginning
			# portion no longer matters. We want to make sure that everything
			# after the asterisks can be ignored until it finds the pattern
			# at the end of the target.
			remain_pattern = pattern[i + 1:]
			# The loop starts where the asterisks is found and ends once
			# the loop has checked the remaining string of the target.
			# This is done by slowly truncating the start of the string until it's at the end.
			# Meaning the pattern should be found at the end of the target, otherwise, it's
			# invalid because the string is different.
			for j in range(i, len(target)):
				if match(remain_pattern, target[j:]):
					return True
			return False

		if pattern[i] != target[i] and pattern[i] != "?":
			return False

	return True


class Test(unittest.TestCase):
	def test_normal_str(self):
		self.assertTrue(match("foobar", "foobar"))
		self.assertFalse(match("foobar", "foo"))
		self.assertFalse(match("foobar", "FOOBAR"))
		self.assertFalse(match("foobar", "this"))

	def test_question_wildcard(self):
		self.assertTrue(match("h?llo", "hello"))
		self.assertTrue(match("h?llo", "hallo"))
		self.assertFalse(match("h?llo", "yello"))

	def test_star_wildcard(self):
		self.assertTrue(match("h*llo", "hllo"))
		self.assertTrue(match("h*llo", "hzllo"))
		self.assertTrue(match("h*llo", "habba dabba doo llo"))
		self.assertTrue(match("h*llo", "h?????llo"))
		self.assertFalse(match("h*llo", "hllop"))
		self.assertTrue(match("h*llo w?rld", "hallo warld"))
		self.assertFalse(match("h*llo w?rld", "hallo aorld"))

	def test_exclamation_wildcard(self):
		self.assertFalse(match(r"h!?llo", "hello"))
		self.assertTrue(match(r"h!?llo", "h?llo"))
		self.assertFalse(match("h!*llo", "hello"))
		self.assertTrue(match("h!*llo", "h*llo"))
		self.assertFalse(match("h!*llo", "h***llo"))
		self.assertTrue(match("h!ello", "hello"))
		self.assertFalse(match("h!ello", "hollo"))
		self.assertTrue(match("h!!llo", "h!llo"))
		self.assertFalse(match("h!!llo", "hollo"))
		self.assertFalse(match("h!!llo", "hullo"))

if __name__ == '__main__':
	unittest.main()