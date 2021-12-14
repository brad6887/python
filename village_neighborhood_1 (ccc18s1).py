n = int(input())

positions = []

for i in range(n):
    positions.append(int(input()))

positions.sort()
print(positions)
left = (positions[1] - positions[0]) / 2
print(left)
right = (positions[2] - positions[1]) / 2
print(right)
min_size = left + right
print(min_size)

for i in range(2, n - 1):
    left = (positions[i] - positions[i - 1]) / 2
    right = (positions[i + 1] - positions[i]) / 2
    size = left + right
    if size < min_size:
        min_size = size

print(min_size)
