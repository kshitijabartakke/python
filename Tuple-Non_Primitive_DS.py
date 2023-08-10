
# What is a tuple? - Immutable - can not change sequence of data; whereas you can do it in list(mutable)
# Why to use tuple? - We use tuple because it is very fast than list
# Unpacking - multiple variable can hold same value - a,b,c,t = (1,2,3,4) **

#**Interview Question
t = 1,  #why it is not an int; because we use comma after defining a value
print(type(t)) #Output <class 'tuple'>

a = ("2",)
print(type(a)) #Output <class 'tuple'> - Look at that Comma*

t1 = (1,2,3,4,5)
print(t1[0]) #Output 1
print(t1[0:3]) #Output (1, 2, 3)

#Try this out by uncommeting - real time example of tuple is Immutable*
#t[2] = 3000 #TypeError: 'tuple' object does not support item assignment
#print(t)

# *VERY INTERESTING Interview Question *
# Now we have learnt that, tuple in Immutable, But here I can change its value using following trick

t2 = ([1,2,3],5,6,7)
t2[0].append(100)
print(t2)  #Output ([1, 2, 3, 100], 5, 6, 7)

# This got changed because 0th indev of tuple is actually *list* and we can modify list at any time ;)

#Output 20 30 40
t3 = (20,30,40)
print(t3)


# Why Tuple is so fast?
# Its data is immutable and it saves its data in RAM in hash as its know this is tuple and no one can edit it

# real time example of tuple is fast
import timeit
print(timeit.timeit('x=(1,2,3,4,5)', number=1000000))
print(timeit.timeit('x=[1,2,3,4,5]', number=1000000))

#Output tuple 0.05204740003682673
#Output list 0.18130309996195138

# see how fast tuple is!