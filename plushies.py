N = int(input())
M = int(input())
output = 0
for i in range(M):
    H = int(input())
    if H >= N:
        output += 1
print(output)