class student:

    school = "telusko"


    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return(self.m1 + self.m2 + self.m3)/3

    def get_m1(self): #getter
        return self.m1,self.m2,self.m3



    def set_m1(self,a,b,c):
        self.m1 =a
        self.m2=b
        self.m3 =c
        return self.m1+self.m2+self.m3  #setter


s1 = student(12,43,76)
# s1 = student(m1,m2,m3)
s2 = student(32,54,15)
s3 = student(322,544,115)

s1.set_m1(12,1,2)
s1.set_m1(12,12,12)

# two types of instance method  : accessors and mutators
