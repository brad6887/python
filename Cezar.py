"""Little Caesar likes card games. Every time he comes to Zagreb, 
he plays blackjack, the famous card game, with his friends.

In this game, the player draws cards while the sum of the cards in 
his hand is less than or equal to 21 or until he says DOSTA 
(Croatian for "STOP").

At the beginning of the game, there are 52 cards in the deck, 
thirteen ranks of each of the four suits. The card ranks are two, 
three, …, ten, Jack, Queen, King and Ace. The card values are the 
following: 
the cards with numbers on them are worth that number (e.g., "nine" is 9),
the cards with pictures (Jack, Queen, and King) are worth 10, whereas 
the Ace is worth 11.

Caesar has found himself in an interesting situation. During the game, 
he already drew N cards whose sum is less than or equal to 21 and is
now having second thoughts about drawing one more card or not. 
Let's assume X is the difference from the sum of the cards so far to 12. 
Everybody knows that you don't draw a card if the number of the 
remaining cards in the deck whose value is greater than X is greater than
or equal to the number of the remaining cards in the deck whose value
is less than or equal to X.

Since Caesar is having a difficult time calculating whether he needs to
draw another card or not, he's asking you to do it for him.

Input Specification
The first line of input contains the positive integer  N, the number of
cards Caesar has drawn so far.

Each of the following N lines contains a single positive integer,
the value of the ith card Caesar drew.

Output Specification
If Caesar should draw another card, output VUCI (Croatian for "DRAW"),
otherwise output DOSTA (Croatian for "STOP")."""

N = int(input())

cards = [ ]
for i in range(1, 5):
    for rank in range(2, 10):
        cards.append(rank) 
    for face in range(1, 5):
        cards.append(10)
    cards.append(11)

total = 0
for i in range(N):
    value = (int(input()))
    total += value
    cards.remove(value)
    
X = 21 - total
lower = 0
upper = 0
for i in cards:
    if i < X:
        lower += 1
    if i >= X:
        upper += 1

if upper >= lower:
    print('DOSTA')
else:
    print('VUCI')


