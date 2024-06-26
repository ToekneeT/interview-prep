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
Combine the secret key with the count variable with string concatenate, find
the current hash of that, and if it doesn't lead with 5 zeroes, loop again.

I also didn't understand the problem at first. I was confused as to how the
answer was found, and what it was doing to get it. I had looked up an online
string to MD5 converter and played with that for a bit. Putting in the strings
that the problem gave me until I put in the right combination and got the answer
that it was looking for.

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
	# It's what the final answer should be, added to the end of
	# the key, whichever number gets starts with a leading 5 0s is the answer.
	nonce = 1
	# slice off just the first five characters to check if it's
	# leading with 5 zeroes.
	while True:
		# concatenate the secret key and the iterable then encodes it
		# to be turned into an md5 hash.
		str2hash = (h + str(nonce)).encode()
		# gets the md5 hash, then converts it into a readable string.
		target_hash = hashlib.md5(str2hash).hexdigest()

		if target_hash.startswith("00000"):
			return nonce

		nonce += 1

'''
 ----- Thoughts on part 1 after completing it. -----
This one was a bit tricky. I understood it conceptually, but I didn't know
how to put it in code as easily since I didn't know how the hashlib and md5
worked. It took a bit of trial and error, but understanding it conceptually
made coding it a bit easier, I think.
Since it must go through numbers by iteration, it can take a good amount of time
find the right string that leads with 5 zeroes.
If I really wanted to improve this, I could probably do something similar to my
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
This is done by getting cpu time using the time library and using process_time()
'''

# This function can completely replace the part 1 version.
# Works the exact same way as the first one, default is 5 leading zeroes.
# can just do find_hash_p2(h) and it'll look for 5 leading,
# but you can pass it a different amount of leading zeroes to look for
# and it will look for that instead.
def find_hash_p2(h: str, leading=5) -> int:
	target_hash = "0"
	nonce = 1
	# another adjustment, since it's now a different amount
	# of leading zeroes, we're going to slice off the amount
	# of leading we want instead of a set 5.
	# then we're going to multiply the 0s by the amount of leading
	# we want.
	# Breaks if leading is passed a 0.
	while True: #target_hash[:leading] != leading * "0":
		str2hash = (h + str(nonce)).encode()
		target_hash = hashlib.md5(str2hash).hexdigest()

		if target_hash.startswith("0" * leading):
			return nonce

		nonce += 1

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

# Time Complexity: O(n) in terms of the nonce counter.

class Test(unittest.TestCase):
	def test_find_hash(self):
		self.assertEqual(find_hash("abcdef"), 609043)
		self.assertEqual(find_hash("pqrstuv"), 1048970)

if __name__ == "__main__":
	unittest.main()