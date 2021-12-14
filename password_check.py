"""Woburn Challenge 2017-18 Round 3 

You'd like to register an account on an extremely entertaining website.
You've already selected a username, but it seems that the requirements
for choosing a password are quite strict, in order to completely protect
your account from being hacked into. The password must be a string between 
8 and 12 characters long (inclusive), such that every character is either
a lowercase letter (a … z), uppercase letter (A … Z), or digit (0 … 9).
Furthermore, it must contain at least three lowercase letters, at least 
two uppercase letters, and at least one digit.

You've got a potential password in mind, a non-empty string made up of at most  
100 characters, each of which is a lowercase letter, uppercase letter, or digit.
Rather than entering the password into the site and risking rejection, you'd like
to determine for yourself whether or not your password would validly satisfy all of the rules.

Input Specification
The first and only line of input consists of a single string, the password.

Output Specification
Output a single string, either Valid if the password is valid, or Invalid otherwise."""

password = input()
upper = 0
lower = 0
number = 0
str = 0


for i in password:
    str += 1
    if i.isupper():
        upper = upper + 1
    if i.islower():
        lower = lower + 1
    if i.isnumeric():
        number = number + 1

    
if (str >= 8) and (str <=12) and (upper >= 2) and (lower >= 3) and (number >= 1):
    print('Valid')
else:
    print('Invalid')