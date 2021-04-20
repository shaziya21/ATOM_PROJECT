def fib(n):
    a=0
    b=1


    if n<0:
        print("Enter a positive fibonacci")

    else:
            print(a)
            print(b)

            for i in range(0,n):
                c = a + b
                a = b
                b = c
                print(c)

n=int(input('enter the value of n :'))
fib(5)


# def fib(n):
#      n= abs(n)
#      a = 0
#      b = 1
#      if n==1:
#          print(a)
#      else:
#          print(a)
#          print(b)
#          for i in range(2,n):
#                 c = a + b
#                 a  = b
#                 b = c
#                 print(c)
# fib(-10)
