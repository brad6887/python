times = int(input())
for time in range(times):
    num = int(input())
    score = 0
    for i in range(1, num - 1):
        if num % i == 0:
            score += i
    if score < num:
        print(f'{num} is a deficient number.')
    elif score == num:
        print(f'{num} is a perfect number.')
    else:
        if score > num:
            print(f'{num} is an abundant number.')
