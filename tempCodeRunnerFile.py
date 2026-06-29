class Circle:
    def __init__(self,radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def area(self,value):
        if value <= 0:
            raise ValueError('Must be positive')
        self._radius = value
    
my_circle = Circle(3)
print(my_circle.area)
my_circle.area = 9
print(my_circle.area)
my_circle.area = 0
print(my_circle.area)
