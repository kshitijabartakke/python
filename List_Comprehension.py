#You add new element in list using append function
#But, When you use append so many times, your code becoms lenthty and bulky 
#So, to avoid it we use *list Comprehension* 

#List Comprehension so the same job by reducing the lengh of a code in an efficient manner
#You no need to write anything manually in the list

#List using append
list_of_nums = []
for i in range(1,11):  
    list_of_nums.append(i)
print(list_of_nums) #Output [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#List Comprehension
list_comp_new = [i for i in range(10,20)]  
print(list_comp_new) #Output [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

#Print odd numbers using List Comprehension
list_odd_num = [i for i in range(1,11,2)]
print(list_odd_num) #Output [1, 3, 5, 7, 9]

