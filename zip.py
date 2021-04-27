# if we want to join two list or tuple or set or dict we'll use zip

names = ('shaz','naaz','chiku')
comps = ('apple','hp','asus')

zipped = list(zip(names,comps))
print(zipped)

# or we can use loop to iterate like

names = ('shaz','naaz','chiku')
comps = ('apple','hp','asus')

zipped = list(zip(names,comps))

for (a,b) in zipped:
    print(a,b)
