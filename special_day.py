"""Canadian Computing Competition: 2015 Stage 1, Junior #1
February 18 is a special date for the CCC this year.

Write a program that asks the user for a numerical month and numerical day of the month and then determines 
whether that date occurs before, after, or on February 18.

If the date occurs before February 18, output the word Before.
If the date occurs after February 18, output the word After.
If the date is February 18, output the word Special."""
month = int(input())
day = int(input())

if (month == 2 and day == 18):
    print('Special')
elif (month == 2 and day < 18) or (month < 2):
    print('Before')
else:
    print('After')
    