#Python Dictionaries 
#class as DICT in code
#We create Dictionaries using key : value
#Denoted by {key:value} - curly bracket
#Key must be unique ; keyvalue can we same
# dict = {key:value, key1:value1, key3:value3}
# mostly used to get values

d1 = {} #create empty dictionary
print(type(d1)) #Output <class 'dict'>

d2 = dict() #Create empty dict
print(type(d2)) #Output <class 'dict'>
print(d2)       # {}

my_dict = {
    "name":"kshitija",
    "role":"devops",
    "city" : "pune"
}
print(my_dict) #Output {'name': 'kshitija', 'role': 'devops', 'city': 'pune'}

# Now, why and how to use dictionary in real life scenario
# Sometimes we need to get value of some keys and it is not so easy,time consuming to see it manually, then we tale help of dictionary
# Say, now I want to know what is the value of role, I will simply run following

#Method1
print(my_dict['role']) #Output devops

#Method2
print(my_dict.get('city')) #Output pune

# Advantage1 - add key:value - method 1
# we can add key:value to it at any instance of time, as following
my_dict['salary'] = 2000
print(my_dict)    #Output {'name': 'kshitija', 'role': 'devops', 'city': 'pune', 'salary': 2000}

#method 2 - using update function
my_dict.update({"hobby":"drawing"})
print(my_dict)  #Output{'name': 'kshitija', 'role': 'devops', 'city': 'pune','hobby': 'drawing'}

# Advantage2 You can update the dict at any time, Here I want to update my name
my_dict['name'] = "Kshitija Bartakke"
print(my_dict)  #Output {'name': 'Kshitija Bartakke', 'role': 'devops', 'city': 'pune','hobby': 'drawing', 'salary': 2000}


# Print Dictionaries key
print(my_dict.keys()) #Output dict_keys(['name', 'role', 'city', 'salary', 'hobby'])

# Print Dictionaries values
print(my_dict.values()) #Output dict_values(['Kshitija Bartakke', 'devops', 'pune', 2000, 'drawing'])

# Dictionary items - get key:value data
print(my_dict.items()) #Output dict_items([('name', 'Kshitija Bartakke'), ('role', 'devops'), ('city', 'pune'), ('salary', 2000), ('hobby', 'drawing')])

# Iteration - show keys using for loop

for keys in my_dict.keys():
    print(keys) 
#Output name role city salary hobby

#show key values

for values in my_dict.values():
    print(values)
#Output name role city salary hobby Kshitija Bartakke devops pune 2000 drawing

# Show key:value together
for key,value in my_dict.items():
    print(key,value) #Output name Kshitija Bartakke role devops  city pune  salary 2000  hobby drawing

# Bonus point : Why Dictionaries??
# Data retrival time is very very low, hence your code execution time reduces and wil get fastest response

# * Interview Question- Dictionary time complexity -  Big O one -means - O(1)
# 1 indicates that only one statement executed and got the output