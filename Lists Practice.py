animals = ["dogs", "cats", "lions", "sheeps"]


print("Animals are: ", animals)

print("Adding animal to the list..")
animals.append("Pandas")

print("List after adding Pandas is: ", animals)

print("Deleitng cats..")
animals.remove("cats")

print("List after deleting cats is: ", animals)

print("First occurance of cat is: ", animals.count("cats"))

animals.pop()

print("Final animals list is: ", animals)
