"""For Valentine's day, AQT wants to give a letter to his valentine.
He currently has a string S of 5 lowercase letters and wants to give 
one to his valentine that isn't present in the string. 
Help him find one!

Constraints
S = 5
S consists only of the letters abcdefghijklmnopqrstuvwxyz 
(lowercase English alphabet).

Input Specification
The first line contains the string S.

Output Specification
Output a letter that AQT does not have.
Note: If there are multiple letters that meet this criterion, 
output the one with lowest alphabetical order. 
See sample explanation for more details.
"""

SYMBOLS = 'abcdefghijklmnopqrstuvwxzy'
chars = input()
Result = SYMBOLS
for char in chars:
    Result = Result.replace(char, '')
print(Result[0])