starting_year = int(input())
future_year = int(input())
counter = 60
for i in range(starting_year, future_year +1):
    if ((counter % 4 == 0)
        and (counter % 3 == 0)
        and (counter % 2 == 0)
        and (counter % 5 == 0)):
        print(f"All positions change in year {i}")
    counter += 1