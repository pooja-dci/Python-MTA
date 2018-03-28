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

