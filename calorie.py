"""At Chip's Fast Food emporium there is a very simple menu. Each food item is selected by entering a digit choice.

Here are the three burger choices:
1 – Cheeseburger (461 Calories)
2 – Fish Burger (431 Calories)
3 – Veggie Burger (420 Calories)
4 – no burger	
Here are the three drink choices:
1 – Soft Drink (130 Calories)
2 – Orange Juice (160 Calories)
3 – Milk (118 Calories)
4 – no drink
Here are the three side order choices:
1 – Fries (100 Calories)
2 – Baked Potato (57 Calories)
3 – Chef Salad (70 Calories)
4 – no side order	
Here are the three dessert choices:
1 – Apple Pie (167 Calories)
2 – Sundae (266 Calories)
3 – Fruit Cup (75 Calories)
4 – no dessert
Write a program that will compute the total Calories of a meal."""
burger = input()
side = input()
drink = input()
desert = input()

if burger == '1':
    bc = int(461)
elif burger == '2':
    bc = int(431)
elif burger == '3':
    bc = int(420)
else:
    bc = int(0)
    
if side == '1':
    sc = int(100)
elif side == '2':
    sc = int(57)
elif side == '3':
    sc = int(70)
else:
    sc = int(0)
    
if drink == '1':
    dc = int(130)
elif drink == '2':
    dc = int(160)
elif drink == '3':
    dc = int(118)
else:
    dc = int(0)
    
if desert == '1':
    ddc = int(167)
elif desert == '2':
    ddc = int(266)
elif desert == '3':
    ddc = int(75)
else:
    ddc = int(0)
    
total = bc + sc + dc + ddc
print('Your total Calorie count is ' + str(total) + '.')