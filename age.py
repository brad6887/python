from datetime import date

def age(birthdate):
    today = date(2007, 2, 27)
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age

voters = int(input())
for voter in range(voters):
    x, y, z = input().split()
    
    new_age = age(date(int(x), int(y), int(z)))
    if new_age >= 18:
        print('Yes')
    else:
        print('No')