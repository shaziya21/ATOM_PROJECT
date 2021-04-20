class computer:

    def config(self):
        print("i5,8gb,1tb")

com1 = computer()
com2 = computer()

computer.config(com1)
computer.config(com2)
# for understanding purpose

com1.config()
com2.config()
# in this line behind the scene config is taking com1 as argument.
