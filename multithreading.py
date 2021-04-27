from time import sleep
from threading import *

class hello(Thread):
    def run(self):
        for i in range(5):
            print('hello')
            sleep(1)  # before printing the next execution go for sleep of 1 sec.

class hi(Thread):
    def run(self):
        for i in range(5):
            print('hi')
            sleep(1)



t1 = hello()

# the moment we say t1 and t2 obj we got two diff threads still they arein to main thread.
# <t1 --main Thread --> t2

t2 = hi()

 # after calling start it creates a new thread , Main Thread,t1,t2 total 3 threads.

t1.start()           # even if create our class a thread we're not creating two diff threads,
sleep(0.2)             #if we want to craete two diff thread we need to use start method instead of original method.
t2.start()           # start() method causes this thread to begin execution,
                     # the Java Virtual Machine calls the run method of this thread. The result is that two threads are running concurrently: the current thread (which returns from the call to the start method) and the other thread (which executes its run method).

t1.join()  # asking main thread to wait.
t2.join()

# we want to print bye at the end so we'll ask main thread to wait for t1,t2 to join.


print('bye')   #main thread is rsponsible for printing this bye

# main(print Bye)
# t1(print hello) sleep
#sleep(0.2)
# t2(print hi) sleep
