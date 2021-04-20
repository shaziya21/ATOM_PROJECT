class A:  # Parent class / Super class

    def __init__(self):   # Constructor of parent class A
        print("in A init")

    def feature1(self):
        print("feature1 is working")

    def feature2(self):
        print("feature2 is working")

class B(A):

    def __init__(self):
        super().__init__()  # jump up to super class A executes it thn jump back to B and thn execute it.
        print("in B init")


    def feature3(self):
        print("feature3 is working")

    def feature4(self):
        print("feature4 is working")

a1 = B()


#  when you create object of sub class it will call init of sub class first.
# if you have ccall super then it will first call init of super class thn call init of sub class.
