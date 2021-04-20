A - B
  |


class A:     # Parent class / Super class

    def feature1(self):
        print("feature1 is working")

    def feature2(self):
        print("feature2 is working")

class B:

    def feature3(self):
        print("feature3 is working")

    def feature4(self):
        print("feature4 is working")


class C(A,B):  # C is inheriting both from A & B

     def feature5(self):
         print("feature5 is working")


a1 = A()

a1.feature1()
a1.feature2()

b1 = B()

b1.feature4()
b1.feature3()

c1 = C()
c1.
