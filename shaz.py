a=5.6
b=int(a) #assigning the int value of a
type(b)
print(b) #print value of b
print(type(b));#print type of b
#converting int value into float
k = float(b)
print(k);
#converting normal number into complex no.
b=5
k=6
c = complex(b,k)
print(c);
#boolean
a=5
b=6
b>a
print(b>a);
#dictionaries=key:value pairs,using curly brackets coz key needs to be unique and doesnt repeat and value is  changeable and set doesnt repeat .
d = {'shaz':'iphone','shadab':'poco','pannu':'realme'}
print(d)
print(d.keys())
print(d.values())
d['shaz']
print(d['shaz'])
d.get('pannu')
print(d.get('pannu')) #.get fn is another way of fetching values
