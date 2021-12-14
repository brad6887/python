# Handling Exceptions
# try:
#     age = int(input("Age: "))
# except ValueError as ex:
#     print("You didn't enter a valid age.")
#     print(ex)
#     print(type(ex))
# else:
#     print("No exceptions were thrown")
# print("Execution Continues.")

#Handling different exceptoions
# try:
#     file = open("app.py")
#     age = int(input("Age: "))
#     xfactor = 10 / age
# except (ValueError, ZeroDivisionError):
#     print("You didn't enter a valid age.")
# else:
#     print("No exceptions were thrown")
# finally:
#     file.close()
    
    
# # The with statement, sometimes works instead of using finally. If object
# # support context management protocol (enter and exit "__exit")
# try:
#     with open("app.py") as file:
#         file("opened.")
#     age = int(input("Age: "))
#     xfactor = 10 / age
# except (ValueError, ZeroDivisionError):
#     print("You didn't enter a valid age.")
# else:
#     print("No exceptions were thrown")
    
    
# Raising exceptions
from timeit import timeit

code1 = """
def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be 0 or less")
    return 10 / age

try:
    calculate_xfactor(-1)
except ValueError as error:
    pass
    """


code2 = """
def calculate_xfactor(age):
    if age <= 0:
        return None
    return 10 / age


xfactor = calculate_xfactor(-1)
if xfactor == None:
    pass
    """
print("first code", timeit(code1, number=10000))
print("second code", timeit(code2, number=10000))