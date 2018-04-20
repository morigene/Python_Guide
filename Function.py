# 2 type of function.1 Built_in Function and 2. user defined function
'''''
1.keyword def is used.
2.def is followed by function name followed by parenthesis.
3.Parameters are passed inside the paranthesis. at the end colon is marked

def <function_name> ():
'''




#Providing Function Definition
def sum(x,y):
    s=x+y
    print ("Sum of two numbers is")
    print(s)
       #Calling the sum Function
sum(10,20)
sum(20,30)

# Return Statement
print( " learn  to use  return statement in function")
def total(a , b):
    x = a + b
    return x
total = total( 10 , 20)
print (total);

'''''
There can be two types of data passed in the function.

1) The First type of data is the data passed in the function call. This data is called ?arguments?.

2) The second type of data is the data received in the function definition. This data is called ?parameters?.

Arguments can be literals, variables and expressions.

Parameters must be variable to hold incoming values.

Alternatively, arguments can be called as actual parameters or actual arguments and parameters can be called as formal parameters or formal arguments

There can be two types of data passed in the function.

1) The First type of data is the data passed in the function call. This data is called ?arguments?.

2) The second type of data is the data received in the function definition. This data is called ?parameters?.

Arguments can be literals, variables and expressions.

Parameters must be variable to hold incoming values.

Alternatively, arguments can be called as actual parameters or actual arguments and parameters can be called as formal parameters or formal arguments
Apart from matching the parameters, there are other ways of matching the parameters.

Python supports following types of formal argument:

1) Positional argument (Required argument).

2) Default argument.

3) Keyword argument (Named argument)

Positional/Required Arguments:

When the function call statement must match the number and order of arguments as defined in the function definition it is Positional Argument matching.
'''

# Passing parameters
def sum(a, b):
    "Function having two parameters"
    c = a + b
    print (c);
sum(10,20)
#sum(20)   Error cause there is two parameters.

# Default parameters
def msg(Id, Name, Age=21):
    "Printing the passed value"
    print (Id)
    print (Name)
    print (Age)
    return
# Function call
msg(Id=100, Name='Ravi', Age=20)
msg(Id=101, Name='Ratan')

# Anynomous Function (not bond to name , created using lambda ,created without using keyword, take any number of arguments)
print("learn anynomous function")
square = lambda x:x*x
summing = lambda x1,x2,x3,x4:x1+x2+x3+x4
print (square(10))
print(summing(2,9,3,2))

# local variable and Global Variable
print( " learn global variable and local variable")

def msg():
    a = 10
    print (a)

msg()

#print(a) Error because is local , below is global

b = 20

def msg():
    print (b)
    return

print( b )

