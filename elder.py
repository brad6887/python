"""After having watched all eight Harry Potter movies in a week,
Nikola finally realized how the famous Elder Wand changes the 
wizard it obeys. If wizard A, whom the wand is currently obeying, 
is defeated by wizard B in a duel, then the wand will start obeying 
the wizard B.

Nikola is now wondering what would happen if 26 wizards labeled 
with uppercase letters of the English alphabet from A to Z began 
fighting in duels for the fondness of the Elder Wand. If we know 
the label of the wizard that the wand had obeyed before all duels 
and the outcomes of all  duels that were held one after another, 
answer the following questions:

Which wizard did the wand obey after all  duels?
How many different wizards did the wand obey?

Input
The first line contains an uppercase letter of the English alphabet, 
the label of the wizard that the wand obeyed at the beginning.

The second line contains an integer number N , the number of duels 
from the text of the task.

In the next N rows there are two different uppercase letters of the 
English alphabet  and  separated by a space, whereas the wizard with 
the label Z1 defeated the wizard with the label Z2 in the ith duel.

Output
In the first line print an uppercase letter of the English alphabet, 
answer to the first question from the task description.

In the second line print an integer number, answer to the second 
question from the task description."""


obeys = input()
n = int(input())

obeyed = obeys
total_obeys = 1

for i in range(n):
    line = input()
    winner = line[0]
    loser = line[2]
    if obeys == loser:
        obeys = winner
        if not winner in obeyed:
            total_obeys = total_obeys + 1
            obeyed = obeyed + winner

print(obeys)
print(total_obeys)