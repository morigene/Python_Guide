
# if statement

a = 10
if a == 10:

    print("Hello Mr.Ben")

# if else

year = 2000

if year % 4 == 0:
    print("Year is leap")

else: print("year is not leap")

# Nested If statement.

age = 20
if age >= 12:
    print("hello my mom")
else:
    if age < 10:
        print("Hello Asifiwe")

    else:print(" you are Rose")

'''''
Loop in python
=====================================
for loop, while, do while

for (variable) in range(sequence)
'''
# For loop.
for i in range (1,9):
    print (i)

# Nested loop.

for i in range(1,6):

    for j in range(1,i+1):

        print(i),

    print

# second example

for i in range(1,6):

    for j in range(5,i-1,-1):
      print("*"),
    print

# while loop

i = 0
while i < 10:
  print (i),
  i = i + 1
print

  

# to use continue keyword
print("Learn to use continue keyword in python")
for year in range(1,9):
   if year%2 == 0:
      continue
   print(year)

#  use break keyword
print(" Learn to use break keyword in python")

eggs = 10
while (eggs < 20):
  if eggs%4==0:
    break
  print (eggs),
  eggs = eggs + 1
print
# we can use also pass if we want no any code to be executed,
print(" Learn to use pass keywork in python")
for i in [12,2,1,8,3,9]:
    if(i==8):
        pass
        print("pass values when is",i),
    print(i),
  