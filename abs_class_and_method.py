

# this method has declaration but not definition , this is called abstract mrthod.
# a class which will have abstract method is called abstract classes.
# python by-default doesn't support abstract classes.
# we cannot create object of abstract class.

from abc import ABC,abstractmethod

class computer:
    @abstractmethod
    def process(self):  # we are declaring the method here which means it doesnt have a body.
         pass  # pass is the way to declare a method

class laptop(computer):
    def process(self):
        print("its running")

class whiteboard:
    def write(self):
        print('its writing')

class programmer:
    def work(self,com):
        print('solving bugs')
        com.process() # aesa q kr rhe hain?


com = computer()
com.process()

com1 = laptop()
# com1.process()

prog1 = programmer()
prog1.work(com1)

# com2 = whiteboard()
# prog1.work(com2)  # it will give error coz this method doesnt have a process method and if we make whiteboard a subclass of computer its compulsion for whiteboard to have process method.
