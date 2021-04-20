def dec(func):
    def inner():
        print("executing now")
        func()
        print("executed")
    return(inner)

@dec
def hello_world():
    print("hello my world")

# hello_world = dec(hello_world)
#  in a replacement of this line we'll use @dec.
hello_world()
