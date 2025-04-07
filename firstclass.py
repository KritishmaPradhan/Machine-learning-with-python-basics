print("This is first ML workshop !!!!!!!")
# type indication
a = 4
print(type(a))
b = 2.4
print(type(b))
# string is immutable demonstration
c = "Hello"                                                    
print(c)
print(id(c))                                                   # prints the address where c is stored
print(hex(id(a)))                                              # prints address in hex value
d = c.replace("e", "i")                                        # replace function for replacing e with i   (understand and come hw)
print(d)
# iterative printing of string Hello
for i in c:                                                                                                
    print(i)
# memory allocation for same integer 2 demonstration
e = 2
f = 2
print(id(e))                                                   # number 2 is assigned in same memory address but
print(id(f))                                                   # assigned to different index variables 

print("*"*100)                                                   # printing * 100 times

# list structure demonstration
def fun1():                                                     # list structure
    return 1
l1 = [fun1(),"hello", 10,30 ]  
for i in l1:
    print(i) 
# 2d list demonstrtion and indexing                                  
l2  = [[1,2,3], [4,5,6]]                                          
print(l2[0][0])
for i in l2:
    print(i)

# dictionary demonstration with example (trial)
dict1 = {'humidity': [10,21,40], 'temperature': [20,30,12], 'wind': [21,13,23], 'rain': [12,43,23]}
for i in dict1.items():
    print(i)
    sum = 0
for i in dict1.values():
    sum = sum + i[0]
sum = sum/4
print(sum)
# list slicing 
l3 = [55,23,44,77,23,22,24]
print(l3[0:4:1])                                                # slicing from 55 to 77
print(l3[1:8:2])                                                # stepsize 2
print(l3[::-1])                                                 # reverse

# find average of the data per column using pandas module
import pandas as pd
list2 = [[10,21,40], [22,24,22], [16,35,13]]
data1 = pd.DataFrame(list2, columns = ['humidity', 'temperature', 'wind'] )
avgg = data1.mean()
avgg

