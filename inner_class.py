class student:   # outer class
    def __init__(self,name ,rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.laptop() # obj of inner class


    def show(self):
        print(self.name , self.rollno)
        self.lap.show()


    class laptop:    # inner class

        def __init__(self):
            self.brand = "hp"
            self.cpu = 'i5'
            self.ram = 8

        def show(self):
            print(self.brand,self.cpu, self.ram)


s1 = student("shaziya",83)  # obj = class
s2 = student('yuvti', 44)

s1.show()  # obj.method
s2.show()

lap1 = student.laptop()  # cannot access laptop directly coz it belongs to  student class.

# you can create obj of inner class the outer class or
# you can create obj of inner class outside the outer class provided
# you use oter class name  to call it.
