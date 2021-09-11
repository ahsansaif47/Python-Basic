
expList = [0,1,2,3,4,5,6,7,8,9]

## first index in the slicing is the starting index and the last index is
## the ending accessable index
## one value less is accessed when slicing..


## suppose if the ending index is 9 the the last index accessed is 8

print("Printing form 2->7: ", expList[2:8])


## slicing using negtive indexing..

print("Print from -5->-1: ", expList[-5:-1])

## slicing entire list..
## No slice indexing required..
print("Entire list slicing: ", expList[:])


## slicing from starting index to some particular index..
## First index is not mentioned in this case means starting index is 0
print("Ending index is 8: ", expList[:8])


## slicing from some particular index to last index..
## last index is not mentioned in this case..
print("Ending index is 8: ", expList[3:])
