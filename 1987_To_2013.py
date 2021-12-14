def check_year_digits(year):
    d = str(year)
    for char in d:
        counts=d.count(char)
        if counts > 1:
            return False
    return True


year = int(input())
year += 1


while not check_year_digits(year):
    year = year + 1

print(year)
