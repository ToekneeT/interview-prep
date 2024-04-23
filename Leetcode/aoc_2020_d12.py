# Interview exercise: Driving a boat

# You are trying to pilot an RC boat. You're given a set of instructions that determine how the boat should move:

# 	Action N means to move north by the given value.
# 	Action S means to move south by the given value.
# 	Action E means to move east by the given value.
# 	Action W means to move west by the given value.
# 	Action L means to turn left the given number of degrees.
# 	Action R means to turn right the given number of degrees.
# 	Action F means to move forward by the given value in the direction the ship is currently facing.

# The ship starts by facing east. Only the L and R actions change the direction the ship is facing. (That is, if the ship is facing east and the next instruction is N10, the ship would move north 10 units, but would still move east if the following action were F.)

# For example:

# 	F10
# 	N3
# 	F7
# 	R90
# 	F11

# These instructions would be handled as follows:

# F10 would move the ship 10 units east (because the ship starts by facing east) to east 10, north 0.
# N3 would move the ship 3 units north to east 10, north 3.
# F7 would move the ship another 7 units east (because the ship is still facing east) to east 17, north 3.
# R90 would cause the ship to turn right by 90 degrees and face south; it remains at east 17, north 3.
# F11 would move the ship 11 units south to east 17, south 8.
# At the end of these instructions, the ship's Manhattan distance (sum of the absolute values of its east/west position and its north/south position) from its starting position is 17 + 8 = 25.

# Manhattan Distance: https://en.wikipedia.org/wiki/Taxicab_geometry

# Figure out where the navigation instructions lead. What is the Manhattan distance between that location and the ship's starting position?


input_file = open("test_input.txt", "r")
directions = []
for line in input_file:
  line = line.replace("\n", "")
  directions.append(line)

# Starting direction of the RC is east.
# North starting degree is 0, east is 90, south is 180, and west is 270.
facing_direction = 90
#facing_direction = "E"
north_south = 0
west_east = 0

for move in directions:
  # Directions given can have either a forward movement or a cordinal direction, or a rotation.
  # If it's not a rotation, the RC should move in a given direction.
  # Due to corindal directions having opposites, we'll use negative and positive numbers to 
  # represent the direction it's facing.
  if move[0] in ["F", "N", "S", "W", "E"]:
    if move[0] == "F":
      if facing_direction == 0:
        north_south += int(move[1:])
      elif facing_direction == 90:
        west_east += int(move[1:])
      elif facing_direction == 180:
        north_south -= int(move[1:])
      elif facing_direction == 270:
        west_east -= int(move[1:])
      continue
    if move[0] == "N":
      north_south += int(move[1:])
      '''
      print(f"Moved North {move[1:]}")
      print(north_south)
      print(west_east)
      '''
    elif move[0] == "S":
      north_south -= int(move[1:])
      '''
      print(f"Moved South {move[1:]}")
      print(north_south)
      print(west_east)
      '''
    elif move[0] == "E":
      west_east += int(move[1:])
      '''
      print(f"Moved East {move[1:]}")
      print(north_south)
      print(west_east)
      '''
    elif move[0] == "W":
      west_east -= int(move[1:])
      '''
      print(f"Moved West {move[1:]}")
      print(north_south)
      print(west_east)
      '''
  elif move[0] == "R":
    # Changes the direction the RC faces by adding the degree it's facing. 
    # The degrees can go over 360, so in order to keep it within 360, we get the remainder of it.
    facing_direction = (facing_direction + int(move[1:])) % 360
  elif move[0] == "L":
    facing_direction = (facing_direction - int(move[1:])) % 360

manhattan_distance = abs(north_south) + abs(west_east)
print(manhattan_distance)