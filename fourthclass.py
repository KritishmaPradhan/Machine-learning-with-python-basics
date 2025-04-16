# passing function as argument
def fun1(a,fun2):
    sum1 = a + fun2()
    return sum1
def funreturn():
    return 2+4
print(fun1(4, funreturn))

# keyword arguments
def keywordarg(*args, **kwargs):
    print(args)
    print(kwargs)
keywordarg(1,2,3, a = 4, b = 7)

#positional argument
def positionalargss(pos, name):
    print(pos, name)
name1 = 'ML'
pos1 = 'Engineer'
positionalargss(pos1, name1)
positionalargss(name = name1, pos = pos1 )
positionalargss(name = pos1, pos = name1)
positionalargss(pos = name1, name = pos1)

# default arguments
def defaultargs(a,b = 2 , c = 6):
    print(a,b, c)
defaultargs(2,3)

# lambda function

square = lambda x: x ** 2
print(square(5)) 


