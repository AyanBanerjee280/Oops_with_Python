# Write a class calculator capable of finding square, cube, and squareroot of a nnumber

class Calculator:
    def __init__(self, num):
        self.number = num

    def square(self):
        print(f"The value of {self.number} square is {self.number**2}.")

    def cube(self):
        print(f"The value of {self.number} cube is {self.number**3}")

    def squareroot(self):
        print(f"The squareroot of {self.number} is {self.number**0.5}")

    @staticmethod
    def greet():
        print("*******Hello there, welcome to the best calculator of the world!********")

        

a = Calculator(125)
a.greet()
a.square()
a.cube()
a.squareroot()