def distance_between(cities, i, j):
    if i < j:
        city1 = i
        city2 = j
    else:
        city1 = j
        city2 = i
    total = 0
    for k in range(city1, city2):
        total = total + cities[k]
    return total


#
cities = input().split()
for i in range(len(cities)):
    cities[i] = int(cities[i])

print(cities)

for i in range(len(cities) + 1):
    distances = []
    for j in range(len(cities) + 1):
        distances.append(str(distance_between(cities, i, j)))
    print(' '.join(distances))