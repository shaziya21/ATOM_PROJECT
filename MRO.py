class A:     # Parent class / Super class

    def __init__(self):   # Constructor of parent class A
        print("in A init")

    def feature1(self):
        print("feature 1-A is working")

    def feature2(self):
        print("feature2 is working")

class B:

    def __init__(self):   # Constructor of class B
        print("in B init")

    def feature1(self):
        print("feature 1-B is working")

    def feature4(self):
        print("feature4 is working")


class C(A,B):  # C is inheriting both from A & B

     def __init__(self):
        super().__init__()  # Constructor of parent class A
        print("in C init")

     def feature5(self):
         print("feature5 is working")

     def feat(self):
         super().feature2()  # super method is used to call other method as well not just init

a1 = C()  # it will give output for C & A only coz in multiple inheritance
a1.feature1()   # it starts from left to right
a1.feat()        # to represent super class we use super method.
