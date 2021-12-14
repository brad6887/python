"""Deal or No Deal™ is a game show on NBC.

In the CCC version of the game, there are  possible dollar amounts:
$100, $500, $1000, $5000, $10000, $25000, $50000, $500000, $100000,
$1000000 sealed in imaginary briefcases. These dollar amounts are
numbered 1 - 10 (i.e. 1 --> 100, 1 --> 500,). Before the game starts
the contestant will have chosen one of the briefcases as his/hers to
possibly keep. During the game, some of the ten possible dollar
amounts have been eliminated from the game because the contestant
has selected some of the other briefcases and revealed the amounts
inside.

At some point, the contestant will stop opening briefcases, and
a "Banker" will offer the contestant cash in exchange for what
might be contained in his/her chosen briefcase. Then the contestant
is asked: "Deal or No Deal?".

Write a program that helps a player decide if he/she should choose
"deal" or "no deal", by calculating the average of the remaining
amounts (i.e., all unopened briefcases, including his/her
"own" briefcase), and comparing that value to the "Banker's" offer.
If the offer is higher than the average, then the player should "deal".
Otherwise, the player should say "no deal".

Input Specification
The user must input a number  (1 - 10) which indicates how many cases
have been opened so far, followed by a list of integers between 1 and 10
representing the values in the game that have been eliminated,
followed by the "Banker's" offer. For example: 3 2 5 10 300 indicates
that briefcases containing $500, $10000, and $1000000 have been
eliminated and the Banker's offer is $300 . You may assume that no
duplicate case numbers are entered for the eliminated values,
and you may assume that the "Banker's" offer is an integer greater
than 10.

Output Specification
The program will print out one of two statements: deal or no deal."""

cases = [0, 100, 500, 1000, 5000, 10000, 25000, 50000, 100000, 500000, 1000000]

opened = int(input())

for i in range(opened):
    eliminated = int(input())
    cases[eliminated] = 0

offer = int(input())

value = 0
for j in (cases):
    value += j

average = value / (10 - opened)

if offer > average:
    print('deal')
else:
    print('no deal')
    