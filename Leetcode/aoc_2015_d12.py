import unittest, json
'''
It's an interesting problem.
I read it a few days ago, and was sitting in the back of my mind with only
a slight thought occasionally.
My current thought is to do a DFS on it as I don't know how many nested items there are.
But I'm not entirely sure how I should go about figuring out what is nested, a dict, or a list.

 ----- Part 1 -----
'''

# Probably not all that useful as it seems all the parent keys are just letters.
def get_all_keys(d):
    for key, value in d.items():
        yield key
        if isinstance(value, dict):
            yield from get_all_keys(value)


def get_all_values(d):
	if isinstance(d, dict):
		for value in d.values():
			# nabs all the dictionaries and lists
			if isinstance(value, (dict, list)):
				yield from get_all_values(value)
			# if there are no dictionaries or lists, then just nab the value.
			else:
				yield value

	elif isinstance(d, list):
		for item in d:
			if isinstance(item, (dict, list)):
				yield from get_all_values(item)
			else:
				yield item

# Honestly, I don't exactly know how the functions above work.
# I looked it up. But I think I understand it better. More in the comments below.

with open("aoc_2015_d12_input.json") as file:
	puzz_input: dict = json.load(file)


def count_all_numbers(puzz_input: dict) -> int:
	total_sum: int = 0

	# For this, I originally thought to use regex to figure out if it was a number or not.
	# I was getting an error that it expected a string, but was receiving a number,
	# so I went and looked for a way to see if you can check types in Python, which led to this.
	# However, I saw that there was also a way to check types using isinstance, so I think think I understand
	# how the functions above work now. Basically if the item its checking is either a list or a dict, then grab it.
	for key in get_all_keys(puzz_input):
		if type(key) is int:
			total_sum += key

	for value in get_all_values(puzz_input):
		if type(value) is int:
			total_sum += value

	return total_sum


'''
 ----- Part 2 -----
Now part 2 is interesting, because any dictionary that contains "red" in it gets ignored, but if it's in a list, it's
still counted.
'''

def get_all_values_no_red(d):
	if isinstance(d, dict):
		# If it finds the term red in the values, it'll skip the dictionary
		# and move onto the next one.
		if "red" in d.values():
			return
		for value in d.values():
			if isinstance(value, (dict, list)):
				yield from get_all_values_no_red(value)
			else:
				yield value

	elif isinstance(d, list):
		for item in d:
			if isinstance(item, (dict, list)):
				yield from get_all_values_no_red(item)
			else:
				yield item


def count_all_numbers_without_red(puzz_input: dict) -> int:
	total_sum: int = 0
	for value in get_all_values_no_red(puzz_input):
		if type(value) is int:
			total_sum += value

	return total_sum


class Test(unittest.TestCase):
	def test_count_all_numbers(self):
		self.assertEqual(count_all_numbers({"a": 2, 2: "b"}), 4)


if __name__ == '__main__':
	unittest.main()