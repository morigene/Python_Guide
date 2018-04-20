
# String are stored as individual character in a contiguous memory location.
# The benefit of using String it can be access from both direction backword and foward.

name = "  origene"
length = len(name)
i = 0
for n in range(-1,(-length -1 ),-1):
    print (name[i],"\t",name[n])
    i+=1

# 3 basically type of operators supported by String
# 1.Basic, 2.Membership operators, 3.Relational Operators

# 1.Basic Operators(String concantenation Operator).
name += "  MUTUYIMANA"
print(name)

# Replication Operator
print(5 * name)

# 2. Membership Operator, 2 type of membership operator : in and not in
str1="javatpoint"
str2="ssit"
str3="seomount"
str4='java'
str5="it"
str6="seo"
print(str4 in str1)
print(str4 not in str1)

# 3. Relational Operators < > <= => !=
print( " Relation operators ")
print( str1 == str2)

# Slice Notation 1.str[startIndex:endIndex] 2. [:endIndex] 3. [startIndex:]
print( str1[0:6])
print( str1[2:])
print(str1[:9])
# String Function and Method
print( "String Function and Method")
msg = "welcome to javatpoint"
print(msg.capitalize()) # first character on string
print(msg.count("o"))
print(msg.count("o",4,16)) # count function
print(msg.endswith("origene"))
print(msg.find("come"))
