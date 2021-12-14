
for number in range(3):
    print("Attempt", number +1, (number +1 ) * ".")

for number in range(1, 4):
    print("Attempt", number, (number ) * ".")

for number in range(1, 10, 2):
     print("Attempt", number, number  * ".")

successful = True
for number in range(3):
    print("Attempt")
    if successful:
        print("Successful")
        break

successful = False
for number in range(3):
    print("Attempt")
    if successful:
        print("Successful")
        break
else:
    print("Attempted 3 times and failed")

# Nested loops
for x in range(5):
    for y in range(3):
        print(f"({x}, {y})")