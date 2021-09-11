

## Sequences and basic searching in python..

## Sequnece concatination..
a = [0,1,2,3,4]
b = [5,6,7,8]

## C sequence is the concatination of a and b
c = a + b

print("Result of concatination is: ", c)



## Note: You can't concainate 2 differant datatypes..


## Use of in keyword..

string = input("Your string to search in: ")
searchLetter = input("Your search letter: ")

if(searchLetter in string):
    print("Letter found!!")

else:
    print("Letter not found!!")
