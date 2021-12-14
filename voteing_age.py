"""For the big election on February 27, 2007, the government has commissioned an electronic voting system, and you have been hired as a sub-subcontractor for this very grand programming project.

Your task is to write the system that determines whether a given person is old enough to vote. The voting age is 18, so given someone's birthday, you must determine whether that person will be 18 years of age on the day of the election.

Input Specification
The input will consist of a number  () on a single line, indicating the number of birthdays to evaluate. Then, each of the following  lines, will be of the form y m d, where  is the year of a potential voter's birth (),  () is the month of birth, and  () is the day. It is assured that each birthday is a correct and valid date.

Output Specification
For each date in the input, output a line with either Yes if the voter is eligible to vote, or No otherwise."""
from datetime import date


# Driver code

def age(birthdate):
    today = date(2007, 2, 27)
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age

voters = int(input())
tyear = int(2007)
tmonth = int(2)
tday = int(27)
    
for i in range(voters):
    birth = (input())
    byear = int(birth.split(' ')[0])
    bmonth = int(birth.split(' ')[1])
    bday = int(birth.split(' ')[2])
    
   # age(date(byear, bmonth, bday))
       
    print(age)
    
    # if years > 18:
    #     print('Yes')
    # elif years < 18:
    #     print('No')
    # else:
    #     if tmonth > bmonth:
    #         print('Yes')
    #     if tmonth < bmonth:
    #         print('No')
    #     else:
    #         if tday >= bday:
    #             print('Yes')
    #         else:
    #             print('No')
