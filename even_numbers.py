# Print even numbers between 1 and 10 without using step operator
# My solution
even = 0
for i in range(1, 10):
    if (i % 2) == 0:
        print(i)
        i +=1
        even +=1
    else:         # didn't need this else statement
        i += 1
print(f"We have {even} even numbers")


# Class solution
count = 0
for number in range(1, 10):
    if number %2 == 0:
        count += 1
        print(number)
print(f"We have {count} even numbers")