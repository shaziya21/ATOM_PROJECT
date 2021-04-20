# VARIABLE : Instance variable
#          : class(static) variable

class car:

    wheels = 4  #class or static variable


    def __init__(self):
        self.mil = 10  # instance variables
        self.com = "bmw"

c1 = car()
c2 = car()

c1.mil = 8

car.wheels = 5

print(c1.com,c1.mil,c1.wheels)
print(c2.com,c2.mil,c2.wheels)
