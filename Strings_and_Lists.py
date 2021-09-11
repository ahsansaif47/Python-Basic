firstName = "Ahsan "
lastName = "Saif"
name = firstName + lastName

print("Name is: ",name)
print("Length of name is: ", len(name))
print("First name is: ", name.split()[0])


animals = ["zebra", "cat", "dogs"]
print("Animals List is: ", animals)

animals.append("tiger")
print("Total animals are: ", len(animals))
animals.append("cat")
print("Animals: ", animals)
print("Finding first occurance if a cat: ", animals.count("cat"))
animals.remove("cat")

animals.pop(1)

print("Final animals list: ", animals)