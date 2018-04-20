    # tuple is a sequence of immutable object,therefore type can not be changed
    # Reason for
''''' 
3 Raison why type is good than list
=========================================
1.They are faster than list
2.It makes the data safe as tuple are immutable and hence cannot be changed.
3.Type are used for string formatting.
'''
data=(10,20,'ram',56.8)
data2="a",10,20.9
print(data2)
print(data2[1:])

data1=(10,20,'rahul',40.6,'z')
data2=(20,30,'sachin',50.2)
data3=(20,30,'sachin',50.2)
print(cmp(data2, data3))
print cmp(data2,data3)