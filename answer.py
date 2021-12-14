"""Here at the Concerned Citizens of Commerce (CCC), we have noted that telemarketers like to use seven-digit phone numbers
where the last four digits have three properties. Looking just at the last four digits, these properties are:

the first of these four digits is an 8 or 9;
the last digit is an 8 or 9;
the second and third digits are the same.
For example, if the last four digits of the telephone number are 8229, 8338, or 9008, these are telemarketer numbers.

Write a program to decide if a telephone number is a telemarketer number or not, based on the last four digits. 
If the number is not a telemarketer number, we should answer the phone, and otherwise, we should ignore """

n1 = int(input())
n2 = int(input())
n3 = int(input())
n4 = int(input())

if ((n1 == 8 or n1 == 9)
    and (n4 == 8 or n4 == 9)
    and (n2 == n3)):
    print('ignore')
else:
    print('answer')