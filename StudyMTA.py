__author__ = 'pooja'

'''1. Evaluate an expression to identify the data type Python will
assign to each variable'''
#a will be an int
a = 2

#b will be float
b = 1.2

#c will be str
c = "Hello World!"

#d would be bool
d = True

#Modulus - remainder of the division
print("*************************Modulus***************************");
print(6.5 % 2)
print(8 % 3)
print("***********************************************************");

print("*************************Exponent***************************");
print(3 ** 2)
print(4.5 ** 3)
print("***********************************************************");


#Division of 2 numbers would always return float. For example:
div1 = 6/3
print("The result of 6/3 is",div1," it's type is ",type(div1))

#Floor division - returns the result as floor value integer (highest integer below the result)
div2 = 7//3
print("The result of 7//3 is",div2," it's type is ",type(div2))

# You cannot concatenate str with other type: Below statement would throw error: TypeError: Can't convert 'int' object to str implicitly
'''check1 = "abc" + 123'''
#To concatenate, convert to string using str method
check2= "abc" + str(123)
print(check2)

#Learn general comparisions operator: >,<,!,==, >=, <=
#Learn general logical operators: and, or, not

#Learn general is, is not
x1 = 5
y1 = 5
x2 = 'Hello'
y2 = 'Hello'
x3 = [1,2,3]
y3 = [1,2,3]
# Output: False
print(x1 is not y1)
# Output: True
print(x2 is y2)
# Output: False
print(x3 is y3)


'''2. Perform data and data type operations'''
#http://luckypants.weebly.com/datatype-conversion.html - Read this to understand conversions in Python

'''construct data structures; perform indexing and slicing operations'''
# Before you continue with this topic, read about the differences between mutable and immutable types in Python
#Lists - are mutable
# Create a list
list1 = [5,6,7,8,9]
list2 = [1,2,3,4]
#Append to end of list
list2.append("Hello") #Appends and returns None
list2.append("World!")
print(list2)
#Check what happens when you append one list to another
list2.append(list1)
#It just appends the whole list and not each element of the list
print(list2) #OUTPUT: [1, 2, 3, 4, 'Hello', 'World!', [5, 6, 7, 8, 9]]

#What if I want to append each element one by one? Use the concatenate + operator
list3 = [10,11]
list2 = list2 + list3
print(list2) # Output: [1, 2, 3, 4, 'Hello', 'World!', [5, 6, 7, 8, 9], 10, 11]

#Indexing and slicing
learnLists = ['My', 'Name', "is", "Tom", "and", "my", "lucky", "numbers", "are", [9,19,22]]
#Index starts from 0 to len-1 so if I want just the name i.e Tom from the list I would do
print(learnLists[3])
#Negative indices are also allowed. So -1 would be the last element and -len would be the first element
print(learnLists[-1])
#DO you know what I am doing here? Basically -len would be the first element of the list
print(learnLists[-len(learnLists)])

'''You can use slicing to print elements for a range of indices. Slicing is [fromIndexIncluded:ToIndexExcluded] so if you wanted elements
from index 2 to index 5 you would do [2:6]
Example: Say you just wanted to print the part "My name is Tom" from learnLists, you would do:
'''
print(learnLists[:4]) #Missing start index means 0 by default
#And print lucky numbers you would do:
print(learnLists[5:]) #Missing end index means till end of list
#To print "Tom and my":
print(learnLists[3:6])

#What do you think this will print?
print(learnLists[1:-1])



#in operator - check if an element is in list
print("and" in learnLists) #True
print("Hello" in learnLists) #False
print(9 in learnLists) #False because it's inside a list that's inside learnLists

#Min and max - When all the elements in the list are of same type you can use min and max
print(min([1,4,88,99,1234,56,60,1,52]))
print(max([1,4,88,99,1234,56,60,1,52]))

#index methods returns position of the element in the list - so it's basically equivalent index_of(someElement)
print(learnLists.index("lucky"))
#print(learnLists.index("Hello")) #Raises value error: ValueError: 'Hello' is not in list

'''  3. Determine the sequence of execution based on operator precedence &
     4.Select the appropriate operator to achieve the intended result'''

'''
Precendence Order:

    Highest Precedence:	()	Parentheses
                        **	Exponentiation
                        *	Multiplication
                        /	Division
                        +	Addition
    Lowest Precedence:	–	Subtraction
'''

x = 3 * (2 + 1)
y = 3 * 2 + 1
print(x)
print(y)
#Inner most parentheses has precendence in a nested parentheses statement. Example:
z = ( ( ( ( 13 + 5 ) * 2 ) - 4 ) / 2)
print(z)

