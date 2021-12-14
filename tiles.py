"""One day Mr. Sidhu's students are talking too much (as usual) and so
he decides to give them a task that might quiet them down for a bit.

He tells them the width and length of the classroom (first line of input)
as well as the side length of a standard square tile (second line of input).
None of these dimensions will be less than 1 or greater than 1000.

You may assume that they are of the same unit. What is the maximum
number of entire tiles that can fit within the classroom's surface?
The tiles can only be axially aligned (sides parallel to the sides
of the room)."""

x = input()
tile = int(input())
dimensions = x.split()
columns = int(dimensions[0]) // tile
rows = int(dimensions[1]) // tile
num_tiles = 0

for row in range(rows):
    for i in range(columns):
        num_tiles += 1
rows -= 1

print(num_tiles)



# import sys

# l, w = map(int, sys.stdin.readline().split())
# d = int(sys.stdin.readline())

# print((l // d) * (w // d))