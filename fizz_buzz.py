# FizzBuzz algorithm
# if input div by 3 = buzz
# if input div by 5 = buzz
# if input div by 3 and 5 = fizz buzz
# anything else returns input
# My Solution

# def fizz_buzz(input):
#     for number in input:
#         if number % 3 == 0 and number % 5 == 0:
#             print(f"{number} is FizzBuzz")
#         if number % 3 == 0 and number %5 !=0:
#             print(f"{number} is Fizz")
#         if number % 5 == 0 and number %3 != 0:
#             print(f"{number} is Buzz")
#         if number % 3 != 0 and number % 5 != 0:
#             print(f"{number}")   
    

# print(fizz_buzz(range(1, 31)))    
    
    
# Instructor Solution
# def fizz_buzz(input):
#         if (input % 3 == 0) and (input % 5 == 0):  
#             return "FizzBuzz"
#         if input % 3 == 0:
#             return "Fizz"
#         if input % 5 == 0:
#             return "Buzz"
#         return input

# print(fizz_buzz(7))

# My analysis, I created mine to loop through a range of numbers so 
# a little more complicated than it could have been. I could have avoided
# multiple test on some lines by putting FizzBuzz test first.
# 
# My revise code with looping:

def fizz_buzz(input):
    for number in input:
        if (number % 3 == 0) and (number % 5 == 0):  
            print(f"{number} FizzBuzz")
        elif number % 3 == 0:
            print(f"{number} Fizz")
        elif number% 5 == 0:
            print(f"{number} Buzz")
        else:
            print(number)


print(fizz_buzz(range(1, 333)))