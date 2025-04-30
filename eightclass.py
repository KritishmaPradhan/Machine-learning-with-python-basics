# Zip implementation in Python using generator
list1 = [1,2,3,4]
list2 = [5,6,7,8]
list3 = [9,10,11,12]
zipped_list = zip(list1, list2, list3)
print(zipped_list)
print(next(zipped_list))
print(next(zipped_list))
print(next(zipped_list))
print(next(zipped_list))

# Zip using iterator
zipped_list1 = list(zipped_list)
print(zipped_list1)

# Map in Python 
import math
def sigmoid(x: float) -> float:
    return (1/(1 + math.e ** -x))
sigmoid_list = [12.3,32.1,2]           # using looping
for value in sigmoid_list:
    print(sigmoid(value))

sigmoid_list1 = map(sigmoid, [5.261, 3.719, 4.2133, 6.789, 3.125])   # using map function  and generators
print(sigmoid_list1)
print(next(sigmoid_list1))
print(next(sigmoid_list1))
print(next(sigmoid_list1))
print(next(sigmoid_list1))
print(next(sigmoid_list1))
print(list(sigmoid_list1))                                            # conversion to list from generator

# Filter in Python
# Function to check if a number is even
def if_even(n):
    return n % 2 == 0
a = [1, 2, 3, 4, 5, 6]
b = filter(if_even, a)
print(list(b))  

usr_database = ['xyz@gmail,com', 'abc@gmail.com', 'hello@gmail.com']
subscription = { 'xyz@gmail.com' : 1,
                 'abc@gmail.com' : 0,
                 'hello@gmail.com' : 1}
def if_spam(email1):
    global usr_database
    return email1.values() == 1 and email1 in usr_database
verify = filter(if_spam, subscription)
print("It exists", list(verify))

# decorator in Python
def addition(a,b):
    return a+b 
def subtraction(a,b):
    return a-b
def operation(fx):
    def wrapper_function(a,b):
        result = fx(a,b)
        return result
    return wrapper_function
operation(addition)
print(operation(addition)(2,3))
print(operation(subtraction)(6,4))

# decorator function in Python
@operation
def add(a,b):
    return a+b
a1 = add(2,3)
print(a1)

