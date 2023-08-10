# SET
# Unordered structure - if you put a to z content - it will print different combination every time
# Set only hold unique values
# Simple scenario - if you want to remove duplicate entries in a ser; you can convert list into set
# Functionality of set - add, remove , union, intersection, difference, subset/superset
# Denoted by {}

# Don't get confused with set and dictionary | dictionary contains data as key:value 

dict_1 = {}
print(type(dict_1)) #Output <class 'dict'>
set_1 = set()
print(type(set_1)) #Output <class 'set'>

#unordered and unique print
#Add
cars = {"audi","BMW","volvo","audi"}
print(cars) #{'audi', 'volvo', 'BMW'}

#Remove
cars.remove("volvo")
print(cars) #Output {'audi', 'BMW'}

cars_set = {"audi","BMW","volvo"}
print(cars_set)
another_cars = {"Mahindra","Maruti","Tata"}
print(another_cars)

#union
set3 = cars_set.union(another_cars)
print(set3) #Output {'audi', 'volvo', 'Tata', 'BMW', 'Mahindra', 'Maruti'}

#Intersection - common element
car1 = {"BMW","TATA","KIYA"}
car2 = {"BMW", "Mahindra"}

inter_car = car1.intersection(car2)
print(inter_car)  #Output {'BMW'}

#Difference
# A-B
diff_car= car1.difference(car2)
print(diff_car) #Output {'KIYA', 'TATA'}
# B-A
diff_car_1 = car2.difference(car1)
print(diff_car_1) #Output {'Mahindra'}

# Subset - b = {2,5}
a = {1,2,3,4,5}
b = {2,5}
c = b.issubset(a)
print(c) #Output True

# Superset - a = {1,2,3,4,5}
d = b.issuperset(a)
print(d) #Output False

e = a.issuperset(b)
print(e) #Output True
