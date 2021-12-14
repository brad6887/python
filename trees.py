days = int(input())
for j in range(days):
    numlogs = int(input())
    logs = 0
    for i in range(numlogs):
        newlogs = int(input())
        logs += newlogs
    if numlogs == 0:
        print('Weekend')
    else: 
        print(f'Day {j + 1}: {logs}')