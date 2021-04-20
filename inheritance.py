
# SINGLE-LEVEL INHERITANCE

class A:     # Parent class / Super class

    def feature1(self):
        print("feature1 is working")

    def feature2(self):
        print("feature2 is working")

class B(A):     # Child class / Sub class
    # this class B is inheriting  all the features of class A
    def feature3(self):
        print("feature3 is working")

    def feature4(self):
        print("feature4 is working")

# MULTI-LEVEL INHERITANCE

class C(B):

     def feature5(self):
         print("feature5 is working")

a1 = A()

a1.feature1()
a1.feature2()

b1 = B()

b1.  # we can also use any feature from class a.

c1 = C()

c1. # can access any feature staing from feature1 to feature5.
