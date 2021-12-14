problems = int(input())
output = []
for i in range(problems):
    numbers = input()
    for j in numbers:
        s = int(numbers[0]) + int(numbers[-1])
    output.append(s)
print(*output, sep = "\n")