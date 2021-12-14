# Classes - blueprint for craeating new objects
# Object: instance of a class

# Class: human
# Object: John, Paul, George, Ringo

class Point:
    def __init__(self, x, y): 
        self.x = x
        self.y = y
    def draw(self):    
        print(f"draw")
        
point = Point(1, 2)
print(point.x)
print(type(point)) 
print(isinstance(point, Point))
print(isinstance(point, int))
