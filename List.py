print( " Python List")
data1 = [ 10 , 20, 30, 40, 50 ]
print(data1)
data2 = [" Hello", "How are ", "you", "doing"]
print(data2)
print(data2[2])  #Accessing Element from list
print(data2[2:])

# List Operators
print( " List Operators ")
list1 = [10,20]
list2 = ["Hello", "Python","yacu","dukunda", "which is very simple"]
print(list2 + list1)  # Adding a list
print (list2 * 2)   # Replicating list
# updating list
list1[1] = " Welcome python"
print(list1)
# Appanding List
print( " Element of List are")
print(list1)
print( " list after appending ")
list1.append(45)
print(list1)
# Deleting Element
del list2[2]
print(list2)
# Function and Method of list.
l1 = [10,34,29, 62,3,89 ]
l2 = ['python', 'list', 'origene']
print(min(l1))
print(max(l2))
print(l1.remove(29))
print(l1)
l1.reverse() # reversing
print(l1)
l1.sort()
print(l1) # sorting