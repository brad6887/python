# Class: blueprint for crateing new objects
# Object: instance of a class

# Class: Human
# Objects: John, Mary, Jack

# Create Class
# class Point:
#     def draw(self):
#         print("draw")
        
# point = Point()
# print(type(point))
# print(isinstance(point, Point))

# Constructors
# methods should have at least 1 parameter ( 'self' by convention)

# class Point:
#     def __init__(self, x, y) -> None:
#         self.x = x
#         self.y = y
    
    
#     def draw(self):
#         print(f"Point ({self.x}, {self.y})")


# point = Point(1,2 )
# point.draw()

# instance attribution
# attributes (x,y,z) are instance attributes 
# 
# class Point:
#     default_color = "red"
    
#     def __init__(self, x, y) -> None:
#         self.x = x
#         self.y = y
    
    
#     def draw(self):
#         print(f"Point ({self.x}, {self.y})")

# Point.default_color = "yellow" # change value for all objects
# point = Point(1, 2 )
# print(point.default_color) # object level attribute
# print(point.default_color)         # class attribuet
# point.draw()
# point.z = 10
# another = Point(3, 4)
# print(another.default_color)
# another.draw()

# class vs instance methods
# class Point:
    
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
        
#     @classmethod
#     def zero(cls):
#         return cls(0,0)



#     def draw(self):
#         print(f"Point ({self.x}, {self.y})")


# point = Point.zero()    # class level
# point.draw()    # instance method

# magic methods
# python3 magic methods

# class Point:
    
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
        
#     def __str__(self) -> str:
#         return f"({self.x}, {self.y}"

#     def draw(self):
#         print(f"Point ({self.x}, {self.y})")
        
# point = Point(1, 2)
# print(point)

# Comparing objects
# class Point:
    
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
    
#     def __eq__(self, other):
#         return self.x == other.x and self.y == other.y
    
#     def __gt__(self, other):
#         return self.x > other.x and self.y > other.y
        
# point = Point(10, 20)
# other = Point(1, 2)
# print(point == other)   # Not equal (False) because it 
#                         #compares address in memory, so magic method must be used(above)
# print(point > other)
# print(point < other) # lt magic method not needed because the gt method was defined

# Arithmetic Operations
class Point:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    
    
point = Point(10, 20)
other = Point(1, 2)
print(point + other)
combined = point + other
print(combined.x)

# Custom containers
class TagCloud:
    def __init__(self):
        self.tags = {}
        
    def add(self, tag):
        self.tags[tag.lower()] = self.tags.get(tag.lower(), 0) + 1
        
    def __getitem__(self, tag):
        return self.tags.get(tag.lower(), 0)
        
    def __setitiem__(self, tag, count):
        self.tags[tag.lower()] = count
        
    def __len__(self):
        return len(self.tags)
    
    def __iter__(self):
        return iter(self.tags)
    
    
cloud = TagCloud()
cloud.add("python")
cloud.add("python")
cloud.add("python")
cloud.add("Python")
print(cloud.tags)
len(cloud)
cloud["python"] = 10
# for tag in cloud:
#     print(tag)
