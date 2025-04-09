t1 = (1,2,3,4,5)
# tuple demonstration with vowel seperation with its index
alphabetss = ('a', 'b', 'e', 'f', 'g' , 'i', 'o', 'p', 'k')
for i in alphabetss:
    if i=="a" or i == "e" or i =="i" or  i == "o" or i == "u":
        print("the vowels is", i)
        print("at index", alphabetss.index(i))

# dictionary demonstration
dict1 ={ 1: [0,1,2], 2: [8,9,3], 3:[11,10,7], 4: [22,6,4]}
val = dict1.values()
print(dict1.values())
print(dict1.keys())
print(dict1.items())
print(dict1[1])
val_list = list(val)
print(val_list)
print("the first index is ", val_list[0])

# set demonstration
set1 = {1,2,3,4,5,6,7,8,9,10}
print(set1)
 
# an empty {} is dictionary
s1 ={}
print(type(s1))
# set2 doesnot change if we add already existing value
set2 = {1,2,3,4}
set2.add(3)
print(set2)
# list assignment and change
a = [2,3,4]
b = a
b[1]= 4
print(a)
#