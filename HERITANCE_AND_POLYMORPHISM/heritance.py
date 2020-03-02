#Superclass
class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width*self.height

#Subclass
class Square(Rectangle): #Class Square extends Rectangle

    def __init__(self, h):
        super().__init__(h, h) #Superclass reference

def run():
    rectangle = Rectangle(3, 4)
    print(rectangle.area())
    square = Square(3)
    print(square.area())

if __name__ == '__main__':
    run()
