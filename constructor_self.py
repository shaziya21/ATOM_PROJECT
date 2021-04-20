# size of object depends upon no of variables & size of ezch variable.
# Constructor will assign that memory and calculate the memory

class computer():

    def __init__(self):
        self.name = "shaziya"
        self.age = 20

    def update(self):
        self.age = 19

    def compare(self,other):      # here c1 becomes self coz c1 is calling it.
        if self.age == other.age:  #other is c2
            return True
        else:
            return False


c1 = computer()
c2 = computer()

c1.age = 26
c2.age = 30

if c1.compare(c2):
    print("they are same")
else:
    print("they are different")


c1.update()


print(c1.name)
print(c1.age)
print(c2.name)
print(c2.age)
