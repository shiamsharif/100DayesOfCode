list = ["a", "b", "c", "d", "e", "f", "g"]
tuple = ("aa", "bb", "cc", "dd", "ee", "ff", "gg")

print(list[2:5])  # o/p: ['c', 'd', 'e'] 
print(tuple[2:5])  # o/p: ['c', 'd', 'e'] 

print(list[2:5:2]) #skip 2nd one. o/p: ['c', 'e']
print(tuple[2:5:2]) #skip 2nd one. o/p: ['c', 'e']

print(list[::2])  # skip every 2nd one. o/p:['a', 'c', 'e', 'g']
print(tuple[::2])  # skip every 2nd one. o/p:['a', 'c', 'e', 'g'] 

print(list[::-1 ])  # o/p: ['g', 'f', 'e', 'd', 'c', 'b', 'a']
print(tuple[::-1 ])  # o/p: ['g', 'f', 'e', 'd', 'c', 'b', 'a']

""" Reverse list with "reverse()" key word"""
list.reverse()
print(list)




""" All Output """ 
# ['c', 'd', 'e']
# ('cc', 'dd', 'ee')

# ['c', 'e']
# ('cc', 'ee')

# ['a', 'c', 'e', 'g']
# ('aa', 'cc', 'ee', 'gg')

# ['g', 'f', 'e', 'd', 'c', 'b', 'a']
# ('gg', 'ff', 'ee', 'dd', 'cc', 'bb', 'aa')
#         
# ['g', 'f', 'e', 'd', 'c', 'b', 'a']