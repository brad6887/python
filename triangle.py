side1 = int(input())
side2 = int(input())
side3 = int(input())

if (side1 == 60) and (side2 == 60) and (side3 == 60):
    tri = 'Equilateral'
elif side1 + side2 + side3 == 180:
    if (side1 != side2) and (side2 != side3) and (side3 != side1):
        tri = 'Scalene'
    if (side1 == side2) or (side2 == side3) or (side3 == side1):
        tri = 'Isosceles'
else:
    tri = 'Error'
    
print(tri)