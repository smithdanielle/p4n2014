import numpy as np

# Using lists
myList=[4, 'hi everyone', 5.3423]
print myList
print myList[0], myList[-1]
print myList[1:]

list2 = [6,7,8]

myList.append(list2)
myList.extend(list2)
print myList
myList += list2 # same functionality as .extend

print myList

for goat in myList: # python knows that 'goat' is just a counter - smarter than MATLAB!
    print goat

# Using dictionaries
# key-item pairs; flexible indexing
myDict={'ori' : 5}
myDict['subject'] = 'jonas'

for key in myDict:
    print key
# How to print items of a dict?

# Strings in python
a = 'hi all'
print dir(a) # can see all attributes of a certain object - underscores are for private methods
print len(a) # len() works for any item with a __len__ attribute; finds the length

print a*2 # you can do maths with strings
print a+ "from Jon" # no need for strcat!

print "formatted strs: %03d, %.3f, %s" %(5, 5, 'boo!') # nicely formatted strings! Jon warns there are many ways to skin a cat

# Exercise 1: using indexing to print values from different lists with the same indices
a = "abc"
b = [8,4,6]

for thisN, thisA in enumerate(a): # enumerate is the equivalent of what?
    print thisA, b[thisN]

# Nested objects: list of dictionaries (creating conditions - single dict per trial?)

# Syntactic sugar
position = [43, 67]
x,y = position
print x
print y

# List comprehension
powers = [a**2 for a in range(10) if a%2==0] #returns a list with a code snippet; faster than a tradition for loop
print powers

# Exercise 2; create empty list, loop over range(10) - recreate the list comprehension example above
loopyList=[]
for num in range(10):
    if num%2==0:
        loopyList.append(num**2)
print loopyList

# List multiplication
a = [1,2,3]
print a*3 # oops, not what we want right now

a = np.array([1,2,3])
print a*3 # numpy arrays are like MATLAB matrices

stim = {'ori' : 15, 'size' : 3}
b = [1, 2, stim]
print b*3 # default Python behaviour can be useful!