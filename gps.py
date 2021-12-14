NS = 0
EW = 0
STEPS = int(input())
for i in range(STEPS):
    DIR = input()
    DISTANCE = int(input())
    if DIR == 'North':
        NS += DISTANCE
    elif DIR == 'South':
        NS -= DISTANCE
    elif DIR == 'East':
        EW += DISTANCE
    else:
        EW -= DISTANCE
        
print(EW, NS)