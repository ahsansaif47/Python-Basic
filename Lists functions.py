

## Lists functions..

numbers = [21,54,24,75,24,58]

## List length
print("Lenght of list is: ", len(numbers))

## Max element of list..
print("Maximum value of list is: ", max(numbers))

## Min element of list..
print("Minimum value of list is: ", min(numbers))

## replace function..
string = "ABCDEFGHIJKL"
elemToReplace = (input("Element to replace: "))
elemToReplaceWith = (input("Element to replace with: "))
print("Printing after replacing ", string.replace(elemToReplace, elemToReplaceWith))

## list function..
## placing a string in a list function creates a list of characters of that string
stringConversion = input("String to convert to list of characters: ")
chars = list(stringConversion)

print("Character list of the string is: ", chars)


