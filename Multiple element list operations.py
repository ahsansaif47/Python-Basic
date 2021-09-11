

## Multiple element list operations..

stringChars = list("SimpleABC")
print("Characters list is: ", stringChars)

## Updating multiple list elements..
stringChars[6:] = list("XYZ")
print("Updated list using list slicing is: ", stringChars)

## Deleting multiple list entries (index specified)..
stringChars[6:] = []
print("List after deleting elements 6 onwards: ", stringChars)
