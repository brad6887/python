"""Canadian Computing Competition: 2000 Stage 1, Junior #3, Senior #1
Martha takes a jar of quarters to the casino with the intention of becoming rich.
She plays three machines in turn. Unknown to her, the machines are entirely predictable.
Each play costs one quarter. The first machine pays 30 quarters every 35th time it is played;
the second machine pays 60 quarters every 100th time it is played; the third pays 9 quarters every
10th time it is played.

Input Specification
Your program should take as input the number of quarters in Martha's jar
(there will be at least one and fewer than ),
and the number of times each machine has been played since it last paid.

Output Specification
Your program should output the number of times Martha plays until she goes broke."""
quarters = int(input())
first = int(input())
second = int(input())
third = int(input())

plays = 0

while quarters >= 1:
    machine = plays % 3
    quarters = quarters - 1

    if machine == 0:
        first = first + 1
        if first % 35 == 0:
            quarters = quarters + 30
    elif machine == 1:
        second = second + 1
        if second % 100 == 0:
            quarters = quarters + 60
    elif machine == 2:
        third = third + 1
        if third % 10 == 0:
            quarters = quarters + 9

    plays = plays + 1

print(f'Martha plays {plays} times before going broke.')
