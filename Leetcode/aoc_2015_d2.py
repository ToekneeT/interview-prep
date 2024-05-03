import unittest
'''
 ----- Part 1 -----
Given dimensions of a rectangular square, get the total surface area
with some additional slack which is determined by the area of the smallest
side of all the dimensions given.
e.x.
2x3x4
1x1x10
expected output: 101
surface area: 2*l*w + 2*w*h + 2*h*l
dimensions 2x3x4
l = 2, w = 3, h = 4
2 *  6    + 2 *  12   + 2  * 8    = 52
2 (2 * 3) + 2 (3 * 4) + 2 (4 * 2) = 52
additional 6 ft of slack
52 + 6 = 58

The slack is found by getting the area of the smallest side.
3 * 2 = 6


The input gives us each package dimension in the format of
LxWxH separated by a newline.
To start off, we take in an input separated by lines and put
it into a list.
That way each line should look like:
LxWxH
LxWxH
Then we'll further split the input by the xs so that only the numbers remain
From there, it's just a matter of peforming the formula of
2(l * w) + 2(w * h) + 2(l * h) + slack
Putting the calculations for slack in a separate function makes it cleaner
and easier to read.
'''

# Reads the input, splits it by lines, removes the newline,
# removes the x's, leaving only numbers in a list.
# converts those numbers from a string to an int.
# so now packages is a 2D list.
# e.x. 2x3x4 = [[2, 3, 4]]
with open("aoc_2015_d2_input.txt") as file:
	lines = file.readlines()
	packages = [[int(x) for x in line.rstrip('\n').split('x')] for line in lines]


# Sort the package list as the slack is the area of the smallest side.
# Time complexity: Small portion of the input, doesn't add anything on its own.
# however, due to the fact that it'll be run each time. Also sorts it. Should make it overall O(3n) -> O(n).
def needed_slack(package: list[list[int, int, int]]) -> int:
	sorted_package = sorted(package)
	return sorted_package[0] * sorted_package[1]

# Time Complexity: Goes through the input at least once. O(n), runs the needed_slack. But that's a constant, so O(n) still.
def needed_paper(packages: list[list]) -> int:
	total = 0
	for p in packages:
		surface_area = 2 * (p[0] * p[1]) + 2 * (p[1] * p[2]) + 2 * (p[0] * p[2])
		total += surface_area + needed_slack(p)
	return total

'''
 ----- Part 2 -----
Now we wrap the presents with a ribbon.
Ribbon is determined by shortest distance around the package's side,
or the smallest perimeter of any face.
Feet of ribbon is required to be equal to the cubic feet of volume of a present.
2x3x4 -> 2+2+3+3 == 10 + 2*3*4 == 24 for a total of 34 (24 + 10).

Seems to be simple math.
We get the smallest sides again, which is the same done in needed_slack.
l * 2 + w * 2
Then we add the result of that to the result of:
l * w * h

The problem wants the total amount of ribbon needed.
It can be integrated with the previous functions to improve
time complexity, but since we only need the ribbon, we can
make a separate function and only handle that.
Meaning, the input of needed_ribbon is going to be the entire
list of package dimensions, i.e. a nested list.
'''

# Time Complexity, similar to needed_slack. Would be a constant, so O(n)
def needed_ribbon(packages: list[list[int, int, int]]) -> int:
	total = 0
	for p in packages:
		# again, we sort it so that we know the first two elements are the smallest.
		sorted_package = sorted(p)
		smallest_peri = p[0] * 2 + p[1] * 2
		volume = p[0] * p[1] * p[2]
		total += smallest_peri + volume
	return total

# Overall Time Complexity: If I were to add needed_ribbon within the needed_paper. I *think*
# it'd be O(n) as they're just constants. As long as we're ignoring the reading input and list comprehension
# to get it to be a nested list of integers.

class Test(unittest.TestCase):
	def test_slack(self):
		self.assertEqual(needed_slack([2, 3, 4]), 6)
		self.assertEqual(needed_slack([1, 1, 10]), 1)
		self.assertEqual(needed_slack([5, 2, 2]), 4)
	def test_part_one(self):
		self.assertEqual(needed_paper([[2, 3, 4]]), 58)
		self.assertEqual(needed_paper([[1, 1, 10]]), 43)
		self.assertEqual(needed_paper([[1, 1, 10], [2, 3, 4]]), 101)
	def test_ribbon(self):
		self.assertEqual(needed_ribbon([[2, 3, 4]]), 34)
		self.assertEqual(needed_ribbon([[1, 1, 10]]), 14)
		self.assertEqual(needed_ribbon([[2, 3, 4], [1, 1, 10]]), 48)

if __name__ == "__main__":
	unittest.main()