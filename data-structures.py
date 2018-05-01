__author__ = 'pooja'

'''
Lists: Lists are a sequence of elements and each element is assigned a number i.e the position or index of the element in the list.
The first index is 0, second index is 1 and so on.
Lists are written as [] and the important thing about a list is that items in a list need not be of the same type.
Examples: myUniversity = ["UNH", 300, "Boston Post Road", [0,6,5,1,6], 19.9]
Now you can access elements using myUniversity[0], myUniversity[1]...

Lists are mutable meaning: When you modify a list, it is changed in place (in the same memory location).

A straightforward definition of mutable and immutable is : Mutable - internal state of the object can be changed
immutable - internal state of the object cannot be changed

Lists are generally used if you need to store different types of data and perform different operations on the data like add, delete, modify
furitsICurrentlyHave = ['apple', 'banana']
I bought oranges so I modify: furitsICurrentlyHave.append('orange')

Now let's create a list and copy it to another list. Then we will change value of one list and see how it affects the other.
'''
#Create a list and prepopulate values
myUniversity = ["UNH", 300, "Boston Post Road", [0,6,5,1,6], 19.9]
anotherUniversity = myUniversity
myUniversity.append("University of New Haven")
#Remeber that index starts from 0 so first element would be myUniversity[0]
myUniversity[2] = "Boston Post Rd" #Changed road to Rd
print("myUniversity is: " + str(myUniversity))
print("anotherUniversity is: " + str(anotherUniversity)) #Run the program to see the results

'''
Tuples: Are written as (). They cannot be modified once created
The position of the elements are recognized through index - just like lists. index 0 is element 1 ...so on.
Real world example of tuple: Coordinates (latitude,longitude) : ((41.326527, -72.956296),(41.308274, -72.927884))

Or coordinates in a graph: currentCoordinate (5,10). Now this coordinate exists on the graph and cannot be changed. If your currentCoordinate
changes, you need to assign it to a new tuple object. You will not be able to modify (5,10) coordinate
coord = (5,10)
currentCoordinate = coord
currentCoordinate = (coord[0] + dx, coord[1] + dy) : This wouldn't change (5,10) it would just create a new coordinate tuple object and assign it to
currentCoordinate
'''
hello = ('Hi!!',) * 4 # A comma specifies that it's a tuple and not just a string. Try removing the comma and executing
print(hello)
print(hello[2])
'''hello[2] = "Hello" #Error: 'tuple' object does not support item assignment'''

'''
Sets: Sets are unordered collection of unique elements. When When you try to append a duplicate element to a set, it ignores it.
Since it is unordered, it doesn't support indexing. Sets are usually used to hold unique values and they are not generally used
to access elements individually.
'''
passportNums = {"XYZ123", "XZW989"}
passportNums.add("SAS787")
print(passportNums)
#Adding the same number again
passportNums.add("XYZ123")
print(passportNums)
#Say you have a list with duplicate elements and you would like to extract unique values from that list:
l1 = [1,2,3,1,4,4,5,2,6,7,2,2,8,7,9,1]
s1 = set(l1)
print(s1)

'''
Dictionary: Key Value pair
example = {"University": "University of New Haven", "Age" : 26, "Birth Year" : 1991}
'''
#Build dictionary:
dict1 = {}
dict1['Hello'] = 'World'
#Keys of dicts have to be immutable - I'll explain why, in our next lecture
#Let's try adding a mutable object as key
'''dict1[[1,2,3]] = [4,5,6] #TypeError: unhashable type: 'list'''

#Construct a dict: A list of tuples each tuple containing key and value
dict2 = dict([('hello','world'), (1,2), ('why', 'how')])
print(dict2)
