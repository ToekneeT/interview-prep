import unittest

'''
 ----- Part 1 -----
Given an input of strings separated by newlines, figure out how many of the strings are nice.
A string is defined as nice when it has at least 3 vowels, a character that appears twice in a row, i.e.
aa, dd, bb, etc.
And does not contain the strings ab, cd, pq, or xy.
Since there are only 4 strings that we need to make sure are not in the string, we can put that into
a list and use a loop that checks the input string if it finds that particular sequence, if it does, move onto
the next string.
Can have a count variable that resets every new string. Count variable will check how many vowels are in the string.
Put the vowels in a list, check each string character by character, if the character is in the vowel list, increment
the count.
We can also have a boolean variable that defaults to false every new string. While it's parsing the string char by char,
if it finds a double letter, change to true.
If there isn't an ab, cd, pq, or xy, vowel count is greater than 3, and double_char is true, add one to nice strings
variable.
'''


with open("aoc_2015_d5_input.txt") as file:
	content = [line.rstrip("\n") for line in file]


def nice_string(str_list: list) -> int:
	nice_strings = 0
	for s in str_list:
		double_char = False
		vowel_count = 0
		vowels = ['a', 'e', 'i', 'o', 'u']
		# Decided to do this instead of a list that contains the banned strings because
		# it'd require a nested loop and a variable. This way I can just continue the current loop.
		if "ab" in s or "cd" in s or "pq" in s or "xy" in s:
			continue

		for i in range(len(s) - 1):
			if i < len(s)and s[i + 1] == s[i]:
				double_char = True
		for i in range(len(s)):
			if s[i] in vowels:
				vowel_count += 1
		if double_char and vowel_count >= 3:
			nice_strings += 1

	return nice_strings


'''
 ----- Part 2 -----
Completely different rules.
Still needs double characters, but they can't overlap.
xyxy works, (xy) but aaa doesn't.
One letter which repeats with one letter in between. xyx, abcdefeghi (efe), or aaa

While the changes are small, they're significant enough to vastly change the core function.
To find the double characters that don't overlap, we can use find and rfind.
If the values that they return are the same, continue on to the next string.
The value of rfind has to be greater than find by at least 2, that way they don't overlap.
Use a boolean variable to track.
Then, the one character in between, we can just look ahead two characters while making sure 
we don't go over the length of the string.
'''

def nice_string_2(str_list: list) -> int:
	nice_strings = 0
	for s in str_list:
		char_sandwich = False
		occur_twice = False
		for i in range(len(s)):
			# Checks the current char and the char two indices ahead to see if they're the same char.
			# makes sure that the index doesn't go over the length of the string, and we're checking up by 2.
			if i < len(s) - 2 and s[i + 2] == s[i]:
				char_sandwich = True
			# Checks if the current char and the char ahead exists twice in the string but doen't overlap.
			# find gets the first index it finds, rfind gets the last one it finds.
			# as long as they're different and at least 2 indices apart, it's valid.
			# could do in one line instead of a nested conditional, but I didn't want a long horizontal.
			if i < len(s) - 1:
				occur_one = s.find(s[i] + s[i + 1])
				occur_two = s.rfind(s[i] + s[i + 1])
				if occur_two >= occur_one + 2:
					occur_twice = True
			if occur_twice and char_sandwich:
				nice_strings += 1
				break

	return nice_strings


class Test(unittest.TestCase):
	def test_part_one(self):
		self.assertEqual(nice_string(["ugknbfddgicrmopn"]), 1)
		self.assertEqual(nice_string(["aaa"]), 1)
		self.assertEqual(nice_string(["jchzalrnumimnmhp", "haegwjzuvuyypxyu", "dvszwmarrgswjxmb"]), 0)
		self.assertEqual(nice_string(["aaa", "ugknbfddgicrmopn"]), 2)

	def test_part_two(self):
		self.assertEqual(nice_string_2(["xyxy"]), 1)
		self.assertEqual(nice_string_2(["qjhvhtzxzqqjkmpb"]), 1)
		self.assertEqual(nice_string_2(["qjhvhtzxzqqjkmpb", "xyxy"]), 2)
		self.assertEqual(nice_string_2(["uurcxstgmygtbstg"]), 0)
		self.assertEqual(nice_string_2(["ieodomkazucvgmuy"]), 0)
		self.assertEqual(nice_string_2(["ieodomkazucvgmuy", "xyxy"]), 1)

if __name__ == "__main__":
	unittest.main()