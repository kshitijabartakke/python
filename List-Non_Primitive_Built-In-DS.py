#List
# Non-Primitive Data Structure - a type of data structure that can store the data of more than one type. 
#List is mutable DS - We can change its value
#List written is square bracket []
#List contains heterogenous data type means list consist of int. float, string, boolan
#List are  mostly used in data storage and data organization

list_of_fruits = [1,2,3,"Kshitija",True,False]
print(type(list_of_fruits))
print(list_of_fruits)

# Function based list
list_of_names = list()
print(type(list_of_names))

#*******Interview Queastion - 1 *** Who is faster [] or list()
"""Answer -  [] is faster and straight forward because it does not need to call another class like need to call in list()"""

#*******Interview Queastion - 2 ***
""" 3 double quotes called as multiline comments"""


# Operation in List - Append - attach the value to the end of the list
list_of_people = []
list_of_people.append("Sachin")
list_of_people.append("Dhoni")
list_of_people.append("Yuvraj")
print(list_of_people)

list_of_people.clear()
print(list_of_people)

#count the frequency of items
list_of_nums = [1,1,2,3,2,3,7,6,5,7,6,7,5,7]

print(list_of_nums.count(7)) #o/p 4


#combine/concatenate 2 lists
list_of_nums_new = [1,2,3,6000,3000]
#list_1.extend(list_2)
list_of_nums.extend(list_of_nums_new)
print(list_of_nums)



#For loop in List
list_of_people = ['Sachin', 'Dhoni', 'Yuvraj','Virat']
print(len(list_of_people))

print(list_of_people[0:2]) #slicing

for people in list_of_people:
    print(people)

for i in range(0,len(list_of_people)):
    print(list_of_people[i])



