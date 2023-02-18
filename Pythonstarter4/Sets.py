
shoppingSet = {"Bread","Sugar","Salt"}
print(shoppingSet)

print(len(shoppingSet))

for x in shoppingSet:
    print(x)

check = "Bread"
print(check in shoppingSet)

shoppingSet.add("Flour")
print(shoppingSet)

juiceFlavours = {"Mango","Passion","Apple"}
shoppingSet.update(juiceFlavours)
print(shoppingSet)

simpleList = ["Oranges","Soap","spoons"]
simpleTuple = ("Forks","Spades")
set2 = {"item2","item3"}
shoppingSet.update(simpleList)
shoppingSet.update(simpleTuple)
shoppingSet.update(set2)
print(shoppingSet)



set3 = {"item5",5}
set4 = shoppingSet.union(set3)  # union creates a new set .
print(set4)

x = {"apple","banana"}
y = {"microsoft","apple"}
x.intersection_update(y)
print(x)

x = {"apple","banana"}
y = {"microsoft","apple"}
z = x.intersection(y)
print(z)

x = {"apple","banana"}
y = {"microsoft","apple"}
x.symmetric_difference_update(y)
print(x)

x = {"apple","banana"}
y = {"microsoft","apple"}
z = x.symmetric_difference(y)
print(z)

x = {"apple", "banana", "cherry", True, False}
y = {"google", 1, "apple", 2, 0}
z = x.symmetric_difference(y)
print(z)












