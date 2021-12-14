text = input().upper()

match = 0
position = 0
total = 0

for i in text:
    if position == 0:
        match = "H"
    elif position == 1:
        match = "O"
    elif position == 2:
        match = "N"
    elif position == 3:
        match = "I"
    if match == i:
        position = position +1
        if position == 4:
            position = 0
            total = total + 1 
print(total)   