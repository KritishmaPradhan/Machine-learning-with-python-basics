# normal form
list1 = [2,3,4,5]
dict1 = {}
for i in list1:
    dict1[i] = i**2
print(dict1)

# dictionary comprehension
list2 = [2,3,4,5]
dist1 = {i : i**2 for i in list1}
print(dist1)

# dictionary where same above but there is no even
list2 = [2,3,4,5]
dist1 = {i : i**2 for i in list1 if i%2 != 0 }
print(dist1)

# dictionary to determine uniqueness of key
uniq_dict = {
    1 : [9,8,7],
    2 : [6,7,8],
    1 : [2,3,4]
}
print(uniq_dict)

# repersentation of dictionary for key as tuples, it cannot take list
dict2 = {
    (1,2,3) : 'attack enemy',
    (4,5,6) : 'take weapon'
}
print(dict2)
print(dict2[(1,2,3)])
