import unittest
'''
----- Part 1 -----
Look-and-say.
Given an input, such as 21, create an output that looks like this:
1211. You get this by one 2, two 1s.
The objective is to do this 40 times on an input that is given.
So after 21, you then get 1211, so you do the same thing with 1211, 
which would give you: 111221.

This seems doable with recursion. Base case being the amount of times it'll run.
So if we run it 40 times, we will decrease it by one until we get down to 0.

In order to generate the look and see, it needs to check how many of the same character
in a sequence there are.
So, parse through the input, look ahead one, if it's not the same number, then generate the current
sequence, and then repeat.
'''

with open("aoc_2015_d10_input.txt") as file:
	puzz_input: str = file.readline()


def look_say(seq: str, times: int) -> int:
	# Base case, once we hit 0 on times, we'll return the length of the sequence.
	if times == 0:
		return len(seq)

	# Current number we'll be looking ahead of to see if it's the same number or not.
	current_num: str = seq[0]
	# Originally a counter, but instead I just concatenated the number to it.
	current_seq: str = seq[0]
	new_seq: str = ""
	# Goes through the current sequence, will check which numbers are the same by looking ahead one,
	# and then if it's not the same, it'll add the current sequence to a new sequence and its current number.
	for i in range(len(seq) - 1):
		if seq[i+1] == current_num:
			current_seq = current_seq + seq[i]
		else:
			new_seq = new_seq + str(len(current_seq)) + current_num
			current_num = seq[i+1]
			current_seq = seq[i+1]

	# The loop skips past the last number in the sequence, so it needs to take care of that by reading
	# the last item in the sequence.
	new_seq = new_seq + str(len(current_seq)) + seq[-1]

	return look_say(new_seq, times - 1)

'''
----- Part 2 -----
I had a feeling part 2 would be something like this.
Part 2 is just what the length of the sequence would be if it's run 50 times instead of 40.
The issue is, my current solution takes a very long time, doing 40 took a good amount of time.
So 50 would take even longer.
So now I want to get execution time, again.

--------------------

My thoughts after completing this:
Midway through, I wasn't getting the results I wanted. For a bit, I couldn't figure out why.
And I almost wanted to start over without recursion, because I thought the recursion was complicating things.
But I kept at, and then boom, it was completed.
It wasn't actually the recursion that was the issue. I kept up with the idea that as long as my base case is
correct, I just needed to make sure the rest made sense. Once that lined up, it worked properly.

Overall, I think recursion isn't that difficult. I find myself looking at a problem, and then my mind will
go "it doable with recursion." Even if it's not the most efficient way to do it, it just feels interesting to do
in recursion as well as possibly good practice.

Time Complexity: We obviously have the amount of times it'll loop, but that's the smaller portion of the problem.
I don't actually know how much it increases by, sometimes the length doesn't increase, but often times it does.
E.x. 1 -> 11 -> 21
11 -> 21 didn't go up at all.
Running my input 40 times gave me a length in the 200,000s, but running it 50 times gave it a length of 3.5 million.
So, overall Time Compexity, O(mn) where n is the times it'll loop and m is the length of the sequence ?
'''
import time

# Took 2.66 seconds
st = time.process_time()
print(look_say(puzz_input, 40))
et = time.process_time()
print(f'40 times\n')
print(f'Execution Time: {et - st} seconds\n')

# Took 2329.05 seconds, aka 38.8 minutes.
st = time.process_time()
print(look_say(puzz_input, 50))
et = time.process_time()
print(f'50 times\n')
print(f'Execution Time: {et - st} seconds\n')

# So for part 2, I think my goal is to make a more efficient way of running it.

class Test(unittest.TestCase):
	def test_part_one(self):
		self.assertEqual(look_say("1", 5), 6)
		self.assertEqual(look_say("11", 1), 2)

if __name__ == "__main__":
	unittest.main()