list1 = [2,3,4,5,97,5,6,8,54]

""" list2 =[] # empty list
for i in list1:
    if i%2==0:
        list2.append(i) # adding even numbers to new list1
print(list2) """

# shortcut to write above code
# list comprehension
list2 = [item for item in list1 if item%2==0]
print(list2)

newList = [1,2,3,2,1,4,5,6,2,3,5]
newSet = {i for i in newList} # Creating set Comprehension , Will remove duplicate values
print(newSet)