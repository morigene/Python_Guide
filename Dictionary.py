'''''
3 Dictionary
=========================================
Dictionary is unordered set of key and value pair.
The key and the value is separated by a colon(:). This pair is known as item. Items are separated from each other by a comma(,). Different items are enclosed within a curly brace and this forms Dictionary.
'''

data = {100: "MUTUYIMANA Origene" , 101: " MUREGO", 102: "Donatien"}
print(data)
# Dictionary is mutable.
# Accessing Value
print(data[102])
# Updation
data[109] = " Samuel"
print(data)
# Delation
del data[100]
print (data)