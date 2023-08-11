# Array
# Array is storing similar types of element
# Why Array - List do hold different type of element which consume lot of memory, it got replaced with an array which stores similar types of element 
# a = [1,2,3,4]  (int) | b = [1.0, 2.3,3.0,4.5] (float)

l1 = []
print(type(l1)) # Output <class 'list'>

# To use array we need to import it, as follows

import array
arr = array.array('i',[])  # Empty Integer Array
print(arr)
arr1 = array.array('f',[])  # Empty Float Array
print(arr1)

int_arr = array.array('i',[100,200,300]) # Output array('i', [100, 200, 300])
print(int_arr)

# ****Interview Question****
# Can I save my python file as array.py?
# When you import array as a module, it will not execute anythiing and throw error as 'module' object is not callable
# You can see now file name is Array_Python

# Array Operations
# append
int_arr.append(400)
print(int_arr)      # Output array('i', [100, 200, 300, 400])

# Delete last element of an array
int_arr.pop()
print(int_arr) 

# Delete specific element of an array
int_arr.pop(0)
print(int_arr) # Output array('i', [200, 300])

float_arr = array.array('f',[1.2,2.0,3.9,4.6,5.5])
print(float_arr[0:3]) # Output array('f', [1.2000000476837158, 2.0, 3.9000000953674316])

