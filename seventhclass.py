import math
from time import perf_counter
def if_prime(num : int)->bool:
    '''
    check whether a number is prime or not
    '''
    for i in range(2,math.floor(math.sqrt(num))+1):
        if (num % i == 0):
            return False
    return True
result = if_prime(4)
print(result)

prime_list = []                           # looping of list for checking prime number
for i in range(1, 1000001):
        if if_prime(i):
            prime_list.append(i)
print(prime_list)   
                                          # list comprehension
starttime = perf_counter()
prime_list_new = [i for i in range(1, 1000001) if if_prime(i)]
# print(prime_list_new)
stoptime = perf_counter()
execution_time = stoptime - starttime
print("The time taken for execution of loop: ", execution_time)

def simple_generator():
    yield 1
    yield 2
    yield 3
a = simple_generator()
print(a)
print('Next gives the next element of generator',next(a))
alist = list(a)
print(alist)

generator_list = (i for i in range(0,5))
print(generator_list)
print(next(generator_list))
print(next(generator_list))
print(next(generator_list))

prime_generator = (i for i in range(2, 1000000000000) if if_prime(i))   # called lazy evaluation
print(next(prime_generator))

