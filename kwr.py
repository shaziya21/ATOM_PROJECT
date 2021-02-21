# def person(name,*data):
#     print(name)
#     print(data)
#
# person('shaz',age = 28,city = 'bhilai',pincode = 490023)

# In variable length argument we can pass any no of parameters
#but in kwargs(keyword variable length  argguments) we have
#to also mention the keyword.

# when we say (*) it will not accept a keyword args.

# using (**) it means passing multiple args but with the help of keywords.

# If we want to pass multiple data with help of keyword we use KWARGS

def person(name,**data):

    print(name)


    for i,j in data.items():
        print(i,j)

person('shaz',age=28,city='bhilai',pincode=490023)
