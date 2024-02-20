#list of names from tehe user
names = ["Bob", "Lily", "Mira", "Logan", "Maggie"]
swapped = True
for i in range(0,len(names)):
    names[i] = names[i].lower()
while swapped:
    swapped = False
    for i in range (len(names)-1):
        if names[i] > names[i + 1]:
            swapped = True
            names[i], names[i + 1] = names[i +1], names[i]
print(names)
names.reverse()
print(names)