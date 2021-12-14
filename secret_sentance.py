"""Luka is fooling around in chemistry class again! Instead of balancing
equations he is writing coded sentences on a piece of paper.
Luka modifies every word in a sentence by adding, after each vowel
(letters a, e, i, o and u), the letter p and then that same vowel again.

For example, the word kemija becomes kepemipijapa and the word paprika
becomes papapripikapa. The teacher took Luka's paper with the coded sentences
and wants to decode them.

Write a program that decodes Luka's sentence.

Input Specification
The coded sentence will be given on a single line. 
The sentence consists only of lowercase letters of the English alphabet and spaces.
The words will be separated by exactly one space and there will be no leading or trailing spaces.
The total number of characters will be at most 100.

Output Specification
Output the decoded sentence on a single line."""

sentance = input()

result = ''
i = 0

while i < len(sentance):
    result = result + sentance[i]
    if sentance[i] in 'aeiou':
        i += 3
    else:
        i += 1
        
print(result)