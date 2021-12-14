"""Mr. Prezens is a very generous man. To show his generosity for his
neighbourhood, he has decided to give each of N trick-or-treaters M
candy bars.

If Mr. Prezens has C candy bars, how many candy bars will he have
leftover for himself after giving each trick-or-treater  candy bars?

Input Specification
The first line will contain an integer, 0 - 100_000, the number of trick-or-treaters he has.

The second line will contain an integer, 0 - 100_000 , the number of
candy bars he gives to each trick-or-treater.

The third line will contain an integer, C , the number of candy bars
he has.

Note: Mr. Prezens will always have at least enough candy bars for
all trick-or-treaters.

Output Specification
Output the number of candy bars he will have left."""

N = int(input())
M = int(input())
C = int(input())
O = C - (N * M)
print(O)
