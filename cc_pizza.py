"""One summer evening, while curled up with her beloved Cheese-kun plushie, C.C. begins craving pizza. 
Although she would really like a large, extra-cheesy pizza, her stomach is willing to settle for anything. 
Without hesitation, she snatches up Lelouch's credit card and makes a very important phone call…

C.C. will be absolutely satisfied if the pizza she gets has a width of 3 units and an extra-cheesiness of at least 95%.
C.C. will be fairly satisfied if the pizza she gets has a width of 1 unit and an extra-cheesiness of at most 50% .
C.C. will be very satisfied with any other pizza she receives."""

unit = int(input())
cheese = int(input())

if unit >= 3 and cheese >= 95:
    sat = 'absolutely'
elif (unit == 1) and (cheese <= 50):
    sat = 'fairly'
else:
    sat = 'very'
    
print(f'C.C. is {sat} satisfied with her pizza.')