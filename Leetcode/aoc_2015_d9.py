import unittest
import re
from pprint import pprint
from itertools import permutations
'''
 ----- Part 1 -----
Funny that I got this problem after doing the Imbue OA.
Given locations and their distances, find the shortest possible route
when only visiting a location once.

So given an input that looks like this:
London to Dublin = 464
London to Belfast = 518
Dublin to Belfast = 141

The possible routes can look like this:
Dublin -> London -> Belfast = 982
London -> Dublin -> Belfast = 605
London -> Belfast -> Dublin = 659
Dublin -> Belfast -> London = 659
Belfast -> Dublin -> London = 605
Belfast -> London -> Dublin = 982

The shortest route would be:
London -> Dublin -> Belfast = 605

So my idea for this is to create a map using a dictionary.
Keys being a tuple, (starting, ending), and the value being the distance.
To split the input, I'll be using regex, each location in its own group and distance being the other.

In a way, this seems similar to Day 7, kinda a circuit that needs to be connected.
So, find a way that these locations connect, then add the distance between them.

So, since there's a lot of possible routes, we'll need to grab the permutations of them.
Add all locations to a set, so no duplicates, and then find how many unique locations there are, and get
the permutations of all locations against the amount of unique locations there are.
'''

with open("aoc_2015_d9_input.txt") as file:
	locations: list[str] = [l.strip() for l in file]


# Create a dictionary that has the distance between two points.
# The key is a tuple of the two locations, the value is the distance.
# Uses regex to grab the locations and the values.
def build_dist_map(loc: list[str]) -> dict:
	dist_map = {}
	pattern = r'([a-zA-Z]+) to ([a-zA-Z]+) = (\d+)'
	for instruc in loc:
		match = re.search(pattern, instruc)
		if match:
			st_ed = (match.group(1), match.group(2))
			dist_map[st_ed] = int(match.group(3))

	return dist_map


# Grabs all possible routes with the locations.
def poss_routes(loc: list[str]): # no clue what the type it's returning is, permutations object? -> 
	pattern = r'([a-zA-Z]+) to ([a-zA-Z]+) = (\d+)'
	# Puts all locations into a set so that there are only unique locations.
	poss_loc = set()

	for instruc in loc:
		match = re.search(pattern, instruc)
		if match:
			poss_loc.add(match.group(1))
			poss_loc.add(match.group(2))

	# Returns all possible routes that can be done if visiting every location at least once.
	return permutations(poss_loc, len(poss_loc))


# Creates a dictionary of all the possible routes as keys and the total distance as their values.
def get_route_dist(routes, dist_map: dict) -> dict:
	route_distances = {}

	for route in routes:
		# Total distance sum of the current route.
		curr_route_dist = 0
		# Since we're going from one point to another, the last location in the route won't point anywhere.
		# So we'll go through the route looking ahead one, but not looking ahead of the last location.
		for i in range(len(route) - 1):
			# Probably a better way to do this, but due to the way I setup the dist_map, I need to check it this way.
			# I pondered the idea of if a set could be key in a dictionary, but it makes sense that it can't since
			# sets are mutable.
			st_ed = (route[i], route[i+1])
			if st_ed in dist_map:
				distance = dist_map[st_ed]
			else:
				distance = dist_map[(route[i+1], route[i])]

			curr_route_dist += distance
		# current route as key, value is total distance.
		route_distances[route] = curr_route_dist
	
	return route_distances


# Grabs the shortest route out of all the routes.
def shortest_route(locations: list[str]) -> int:
	distances = build_dist_map(locations)
	routes = poss_routes(locations)
	route_distance = get_route_dist(routes, distances)
	
	return(min(route_distance.values()))


'''
 ----- Part 2 -----
It's the same, but reversed, We just want to get the longest distance instead.
So, we just do the opposite of the shortest_route() function.
'''


def longest_route(locations: list[str]) -> int:
	distances = build_dist_map(locations)
	routes = poss_routes(locations)
	route_distance = get_route_dist(routes, distances)

	return(max(route_distance.values()))


class Test(unittest.TestCase):
	def test_part_one(self):
		self.assertEqual(shortest_route(["London to Dublin = 464", "London to Belfast = 518",
			"Dublin to Belfast = 141"]), 605)

	def test_part_two(self):
		self.assertEqual(longest_route(["London to Dublin = 464", "London to Belfast = 518",
			"Dublin to Belfast = 141"]), 982)


if __name__ == '__main__':
	unittest.main()