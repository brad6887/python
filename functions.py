# def greet(first_name, last_mane):
#     print(f"Hi {first_name} {last_mane} ")
#     print("Welcome aboard")


# greet("Brad", "Cooke")


# def get_greeting(name):
#     return f"Hi {name}"


# # message = get_greeting("Clyde")
# # print(message)

# # print(get_greeting("Eugene"))

# # # Keyword arguments
# # def increment(number, by):
# #     return number + by


# # print(increment(2, by=1))

# # Optional parameter
# def increment2(number, by=1):
#     return number + by

# print(increment2(2))
# print(increment2(2, 5))

# xargs - variable number of arguments

def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total

print(multiply(2, 3, 4, 5))

# xxargs - pass multiple keyword pairs (dictionary)
def save_user(**user):
    print(user)
    print(user["name"])

save_user(id=1, name="Ringo", age=21)
