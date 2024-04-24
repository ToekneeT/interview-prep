import unittest
'''
 ----- Part 1 -----
This is an interesting one.
Given a secret key, or an input of strings.
Find the first number that doesn't lead with 0, that would
produce a MD5 hash that starts leads with 5 zeros.
If abcdef is your secret key, the answer would be
609043 as combining that number with your secret key would
be the first MD5 hash that leads with 5 zeroes.
abcdef609043 -> 000001dbbfa...

Step one is to figure out how to convert a string to a MD5 Hash.
Then, it's as simple as looping until it finds the first hash that 
has 5 leading zeroes. But since the number that is combined with 
the secret key can't have a leading zero itself, we can just use a count
variable that goes each loop.
Combine the secret key with the count variable with string concate, find
the current hash of that, and if it doesn't lead with 5 zeroes, loop again.

So looking it up, Python has a built-in called hashlib that can
convert a string into an MD5 hash.
'''
import hashlib
import time # used to get execution time.

with open("aoc_2015_d4_input.txt") as file:
	h = file.read()


def find_hash(h: str) -> int:
	# set target hash to 0 for now. placeholder so that the
	# while loop can run once. Could compensate by doing a 
	# do while instead of this.
	target_hash = "0"
	# the iterable number that will get added to the string.
	# starts at 0 but gets added right away in the while loop
	# so that it truly starts at 1.
	find_hash = 0
	# slice off just the first five characters to check if it's
	# leading with 5 zeroes.
	while target_hash[:5] != "00000":
		# Starts at 1 since the answer can't start with a leading
		# zero. And by adding the number first, we then perform the
		# calculations, so that once the next loop starts, if the
		# previous hash started with 5 zeroes, the next loop wouldn't
		# run, thereby not adding one to the find_hash.
		find_hash += 1
		# concate the secret key and the iterable then encodes it
		# to be turned into an md5 hash.
		str2hash = (h + str(find_hash)).encode()
		# gets the md5 hash, then converts it into a readable string.
		target_hash = hashlib.md5(str2hash).hexdigest()

	return find_hash

'''
 ----- Thoughts on part 1 after completing it. -----
This one was a bit tricky. I understood it conceptually, but I didn't know
how to put it in code as easily since I didn't know how the hashlib and md5
worked. It took a bit of trial and error, but understanding it conceptually
made coding it a bit easier, I think.
Since it must go through numbers by iteration, it can take a good amount of time
find the right string that leads with 5 zeroes.
If I really wanted to improvet this, I could probably do something similar to my
java mega millions program and have it multithreaded with each loop going through
say 999_999 numbers. e.x. thread 1 does 1 to 100_000, thread 2 does 1_000_000 to
1_999_999 numbers. But that's micro-optimization, since there's no guarantee it'd
be a number that high. For example, my secret key had an answer that was quite low.
'''

'''
 ----- Part 2 -----
Part 2 is the same thing, just finding one that starts with six zeroes
instead of five. Seeing this, I can now see that my thought on multi-threading
would be more helpful as finding one with six leading zeroes would take much
more time.
Part 2 would be the same code as part 1, just changing the while conditional.
So to take it a step further, I'll just add another parameter to the function.
and set the while loop to use that.

Knowing that this will take longer, I have decided to go back in both
part 2 and part 1 to get execution time.
This is done by importing time and getting cpu time using the time
library and using process_time()
'''

# This function can completely replace the part 1 version.
# Works the exact same way as the first one, default is 5 leading zeroes.
# can just do find_hash_p2(h) and it'll look for 5 leading,
# but you can pass it a different amount of leading zeroes to look for
# and it will look for that instead.
def find_hash_p2(h: str, leading=5) -> int:
	target_hash = "0"
	find_hash = 0
	# another adjustment, since it's now a different amount
	# of leading zeroes, we're going to slice off the amount
	# of leading we want instead of a set 5.
	# then we're going to multiply the 0s by the amount of leading
	# we want
	while target_hash[:leading] != leading * "0":
		find_hash += 1
		str2hash = (h + str(find_hash)).encode()
		target_hash = hashlib.md5(str2hash).hexdigest()

	return find_hash

st = time.process_time()
print(find_hash(h))
et = time.process_time()
print(f'5 Leading zeroes\n')
print(f'Execution Time: {et - st} seconds\n')
# My secret key took 0.25 seconds.

st = time.process_time()
print(find_hash_p2(h, 6))
et = time.process_time()
print(f'6 Leading zeroes\n')
print(f'Execution Time: {et - st} seconds\n')
# My secret key took 1.01 seconds.

# Aaaand after running it, maybe you don't need to multi-thread it,
# it's quite fast anyway.

# Not entirely sure how to figure out the time complexity of this,
# since the number could theoretically be infinite(?).

class Test(unittest.TestCase):
	def test_find_hash(self):
		self.assertEqual(find_hash("abcdef"), 609043)
		self.assertEqual(find_hash("pqrstuv"), 1048970)

if __name__ == "__main__":
	unittest.main()