# accessing a list with dictionary as elements in the form of database
person = [{'name' : 'ram', 'roll_no' : 1, 'status' : 'in_university', 'age' : 20, 'enrolled' : ['DBMS', 'python', 'DSA']},
          {'name' : 'hari', 'roll_no' : 1, 'status' : 'passout', 'age' : 21, 'enrolled' : ['DBMS', 'AI', 'DSA']},
          {'name' : 'siya', 'roll_no' : 1, 'status' : 'passout', 'age' : 22, 'enrolled' : ['DBMS', 'DMDW', 'DSA']},
          {'name' : 'john', 'roll_no' : 1, 'status' : 'passout', 'age' : 20, 'enrolled' : ['DBMS', 'python', 'cyber_security']}
          ]

for person_dict in person:
    if person_dict['name'] == 'hari' :
        person_dict['status'] = 'expelled'

print(person[1])
print("_"*100)
print("The data of students after updating")
for i in person :
    print(i)

# Conditions in python / control structures in python
# for loop
list1 = [1, 2, 3, 4]
for i in list1:
    print(i)
# while statement
i = 1
while i<=5:
    print('hello world')
    i += 1
# range implementation
for i in range(0,4):
    print('hello world')
# enumerate implementation
list2 = [1, 2, 3, 4, 5, 6]
#for some_values in list2:
for some_values in enumerate(list2):
    print(type(some_values))
    print(some_values)

list2 = [1, 2, 3, 4, 5, 6]
for some_values in enumerate(list2):
    index, element = some_values
    print(f"index = {index} element = {element}")

# functions in python
def addfun(a, b) :
    print(a+b)
addfun(2,4)

def subtfun(c, d) :
    return c-d
subtractvalues = subtfun(2,4)
print(subtractvalues)

listfun = [subtfun(), addfun()]


#--------------python basic mathematical operation-----------------------------
def add_ab(a,b):
    return a+b

def sub_ab(a,b):
    return a-b

def mult_ab(a,b):
    return a*b

def div_ab(a,b):
    return a/b

def operation(selection):
    if selection == 'add':
        print('The sum is ',add_ab(a,b))
    
    elif selection == 'sub':
        print('The sum is ',sub_ab(a,b))

    elif selection == 'mul':
        print('The sum is ',mult_ab(a,b))

    elif selection == 'div':
        print('The sum is ',div_ab(a,b))
    
    else:
        print('Invalid entry!!!!')


a = int(input('Enter the value for a : '))
b = int(input('Enter the value for b : '))


selection = input('''Enter the operation:
                  1.add
                  2.sub
                  3.mul
                  4.div
                  ''')

operation(selection)

