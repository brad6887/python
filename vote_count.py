"""Input Specification
The input will be two lines. The first line will contain  V,
the total number of votes. The second line of input will be
a sequence of  characters, each of which will be A or B,
representing the votes for a particular singer.

Output Specification
The output will be one of three possibilities:

A, if there are more A votes than B votes;
B, if there are more B votes than A votes;
Tie, if there are an equal number of A votes and B votes."""

V = int(input())
votes = (input())
a_votes = votes.count('A')
b_votes = votes.count('B')
if a_votes > b_votes:
    print('A')
elif a_votes < b_votes:
    print('B')
else:
    print('Tie')

