#Refer python_theory/notes for understanding few basics of python...

print("************** 1. Basics of Python Programing*************")
print("How to run a python program")
#right click this module tab and run the program or go to run menu and run or click on the play button in the right top
#or type ctrl+shift+f10

#Fundamentals of Python Programming:
####################################
print("A. Python is an indent based programming language")
#Why Python uses indend based programing ->
#1. Managing the program more efficiently
#2. Better Readablility of the code
#3. For creating the hierarchy of programming.
#a=1#dead code
a=2
b=2
if a==b:
    if a!=b:
        print("hello")
    else:
        print("inner else")
else:
    print("outer else")
    print("line2")
#4. By default 4 spaces we will give for indends, but more/less spaces or tabs also can be used...

#Linux is not an intend based program, it is a block based rather:
'''
a=10
b=20
if [ a = b ]
then
    echo "hello"
    echo "a and b are same"
else
    echo "hi"
    echo "a and b are not same"
fi
'''

#indendation has to be uniform within the block of code (not across the block of code)
#below prog doesnt work because we are using different number of spaces between lines of code in a given block
a=10
b=10
if a==b:
    print("hello")
     #print("will not work, bcz Same block must be indented at the same level of spacing")

#below prog doesnt work because we are using different keys like spaces for one line and tab for another line
if a==b:
    print("hello")
    print("will not work, bcz Same block must be indented at the same level of spacing or tabs, not both")
#TabError: inconsistent use of tabs and spaces in indentation

#optimal number of spaces has to be 4, but any numbers you can give
if a==b:
    print("hello")
    print("Use 4 spaces optimally")

print("B. This is a commented line in Python")
print("Comment is used for denoting the interpreter to not execute the commented lines ")
print("Comments can be code (dead code), description about a line of code, inline comment about the program also")
#As like linux , python also has # as a single line comment...
#The below symbol (''',""") is the multi line comments in python, (/* */ or other symbols will not work..)
#a=20
a=25#I am assigning a variable a with a value of 25 using an assignment operator =
print("interpreter will consider a=25, rather than considering a=20")
'''
This is multi line comments
in python
'''
"""
This is multi line comments
in python
"""

print("C. Playing with Quotes: Python treats single quotes the same as double quotes as like triple quotes, but has some differences")
#Python treats single quotes the same as double quotes and triple quotes.
companyname='inceptez technologies'
print(companyname)
companyname="inceptez technologies"
print(companyname)

#In the below case , we can't use single quote...
#companyname='it is an inceptez's property'
companyname='it is an inceptez\'s property'#Use escape sequence
print(companyname)
#Double quotes is used for holding single quoted chars
companyname="it is an inceptez's property"
print(companyname)

#Double quotes is used for holding double quoted chars by using escape sequence
companyname="it is an \"inceptez\" property"
print(companyname)

#Triple double quotes/Triple Single quotes
#To hold double quotes or single quotes without using escape sequence...
companyname="""it is an "inceptez" property"""
print(companyname)
#For handling paragraph/multilines text, we can use 3 single or doublequotes
description="""it is an "inceptez" property
Happy to see you all
Great learning..."""
print(description)

description="it is an inceptez property \n Happy to see you all" #Without using triple quotes, i want to print multiline...

#All about Variables....
#Variables comprised of all the below topics...
'''
D. Variables & Values
E. Naming Conventions
F. Types and Casting
G. Input & Output operations
H. Datatypes (Simple/premetive or Complex/Collection (data structure))
'''
print("D. Variables & Values")
#Any programming language learning has to be started first learning about variables
print("Let's learn all about VARIABLES")
'''1. Variable Properties - Dynamic Inference, Dynamic Typed, Strongly Typed'''

#Dynamic inference - based on the assigned value to a variable, it will automatically decides/infer/identify/refers the data type dynamically
a=10
print("Python is inferring the data type dynamically from the value assigned",type(a))
name="irfan"
print("Python is inferring the data type dynamically from the value assigned",type(name))
#Dynamically typed: If a variable is created with a specific data type, can be changed later
name="irfan"
print("Python is dynamically allow to change the type from string to integer",type(name))
name=102.75
print("Python is dynamically allow to change the type from string to integer",type(name))

#below is possible, because python is dynamically typed language (Duck type language)
'''Scala is a statically typed language
var name="irfan"
#below is not possible - because of statically type feature
name=100
<console>:12: error: type mismatch;
'''

#Strongly typed: Python allow us to operate between the variables of same datatype (of the same hierarchy) and doesn't allow to operate between different datatypes.
ver=1.0
name="irfan"
#print(name+ver)
print(name+str(ver))#Python is strongly typed language, hence we have type cast to make python work...

#Weakly typed: Scala allow us to operate between the variables of even Different datatypes, below is possible
#var x=10
#var name="irfan"
#print(x+name)

print("E. Naming Conventions")
#thumb rules:
#starting with only alphabets/underscores otherwise we can't define a variable
#A variable can have only alphabets, numbers and underscores, no special charactes are allowed
#Variables name are case sensitive a is different from A
#Naming convention can be Camelcase, Initupper case, multi words with underscore

#A variable can have camel case or init upper or with underscores (standard to follow)


#A variable name must start with a letter or the underscore character (no numbers or other symbols are allowed)
ab=1
__ab__=1#Used for special purposes like special/secured variable/internal variables
#A variable name cannot start with a number or other special characters
#1ab=10
#:ab=10
#below doesnt work
#1_var=10
#print(1_var)

#A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
abc123_xyz=10
#abc:123=10#123 is not considered as a variable name, rather it is considered as hint..
#abc-123=10 #Will not work

#Variable names are case-sensitive (For Eg:)
#all are different...
a=10
A=20
irfan=43
IRFAN=40
print(a,A,irfan,IRFAN)
#Multiple Variables can be assigned in a single line (Multi Assignment)
a,A,irfan,IRFAN=10,20,43,40#same as above assignments individually
print(a,A,irfan,IRFAN)

print("F. Types & Casting functions")
#3. How to check a given TYPE is of what datatype we expect  & type casting
#Functions we are learning in this topic (type(), str(),int(),isinstance(var,datatype))
age=43
#What we are learning here is the usage of few functions like isinstance(),str(),type()
#To understand the age is of what type
print(type(age))
#To check whether the age is of an expected type
print(isinstance(age,int))

#To convert the age to an expected type
age_string=str(age)
print(age_string)

#Check for a given type, if it is not as expected then cast it to the expected type programatically using if condition
a=1.0
b='irfan'
#print(b+str(a))
if isinstance(a,str):
    print("Directly appending with name")
    print(b+a)
elif isinstance(a,float):
    print("change the type of the a to string and then operate")
    print(b+str(a))

print("G. Standard Input & output options")
#assigning value statically
myname='irfan'
print("static value assigned to a variable is ",myname)
#assigning value dynamically using input()
myname=input("pls input your name\n")
print("dynamic value assigned to a variable is ",myname)
option1=int(input("pls input your option 1 for tamil, 2 for other lang\n"))
print('Datatype of option entered',type(option1))

#print statement will be used as a std output function, which will use \n in the end by default, no need of using println like scala kind of lang
#Quick requirement: Need output like "name of the user is Mayavan and age of the user is 33"
#where name and age has to be dynamically identified using input
name=input("enter the name \n")
age=int(input("enter the age in number \n"))
#Options for achieving above results are there:
print("a","b",123)
print("Option1 using multiple arguments in print : name of the user is", name, "and age of the user is",age)
print("Option2 using concatenation/append operation :name of the user is "+name+" and age of the user is "+str(age))

#below print function is taking only 1 argument (but print can take any number of arguments)
print("Option2 using concatenation/append operation :name of the user is "+name+" and age of the user is "+str(age))
#below print function is taking multiple arguments and printing them individually
concatenated_print_statement="Option1 using multiple arguments in print : name of the user is", name, "and age of the user is",age
print(concatenated_print_statement)

#Formatted strings and use it in the Print statements - positional args
#Positional arguments
prepare_string_to_print_or_for_any_other_operations=\
    "Option3 using formatting option for positional formatting : name of the user is {0} and age of the user is {1}"\
        .format(name,age)
print(prepare_string_to_print_or_for_any_other_operations)

#keyword/named arguments
prepare_string_to_print_or_for_any_other_operations=\
    "Option4 using formatting option for named formatting : name of the user is {myName} and age of the user is {myAge}"\
        .format(myName=name,myAge=age)
print(prepare_string_to_print_or_for_any_other_operations)
#print("Name of user is {name} age is {age}".format(name=myName, age=myAge))

#Formatted string Print statements other way (3x onwards) - named args
#FORGET ALL THE ABOVE 4 (LEGACY) OPTIONS WE USED TO FORMAT STRING.... CONSIDER ONLY THE BELOW ADVANCED OPTION
prepare_string_to_print_or_for_any_other_operations=f"Option5 using formatting option for named formatting : name of the user is {name} and age of the user is {age}"
print(prepare_string_to_print_or_for_any_other_operations)

print(f"name is {name}")#Just consider this...

print("H. Datatypes , Characterisics - Sequence, Mutability & Builtin Functions")
#Datatypes - Hierarchy of the type, Mutable/immutable, use/operate the types with the builtin function
#String Type: String is an indexed sequenced collection of homogeneous characters
# can be assigned with single, double, triple single/double quotes
name="irfan"
#01234
#irfan
print(name[0])#returns i
#Family of the datatype (Numeric, Sequence, Misc, Collection/Complex)? Sequence/Non Sequence type
#A. Falls under Sequence family - If we can perform iteration then it is sequence
for a in name:
    print(a.upper())

age=43 #not a sequence type, as it is not having index or we can't do iteration (looping)

#B. Mutable/Immutable? String is immutable, in python all other types are immutable other than list, dict, set are mutable
name='irfan'
#name[0]='I' #Item assignment is not possible

#eg. for mutability, list is mutable how?
name=['i','r','f','a','n']
name[0]='I'#Possible, because list is mutable...
#name[0]='I' #Item assignment is not possible

#C. Functionalities it supports? operations that can be performed
#Very very important is - understanding/learning how to understand, learn and use a function appropriately... rather than memorizing it...
#Don't try to memorize all functions other than very few... eg. print, split, mathematical function, string function concat, upper...
#Try to primarily understand the functionality by using the name of the function
#By extending using . notation we can see the supportive functions
#Try to understand the function description by hovering the function and try to understand the input arguments and output type...
#or press ctrl+click to see the function definition under the class

name:str='mohamed irfan'
print(name,flush=True)
name.capitalize() #Mohamed irfan
print(name)
name.upper()
print(name)
#interview question
name='fisul--haqkani'
split_name=name.split('--')#important function
fname=split_name[0]
lname=split_name[1]
print(fname,lname)

name='fisul haqkani--inceptez technologies--pvt ltd'
name.split('--')
print(name.partition('--'))#looks similar to split, but different
data='1,irfan,43,chennai'#split this data into list of fields or partition it to the first column in one part and balance columns in another part
print(data.index('chen',5,15))

data='-Irfan,'
data.join(['SE','SSE','TL',''])
data='100'
data.zfill(5)
data='Inceptez'
data.endswith('tez')

name='TN64P7449'
name.isalnum()#checks for alpha and numeric
age='43'
age.isnumeric()#checks for given value is number
age.isalpha()#checks for the given value is string
name='Mohamed Irfan'
name.istitle()#checks for initcap
name=' mohamed irfan '
trimmed_name=name.strip()
trimmed_name=name.rstrip()
nospace_name=name.replace(' ','',4)


#Hints (Variable datatype can be hinted rather than forcefully enforced/applied)
#Why we use hints - for readability, understanding, maintainability
name:int='irfan'
print(name)

#Numeric Types - immutable, non sequenced
#for i in 100:#will not work
#    print(i)
a=100
#a[0] #will not work non sequenced
#a[0]=5 #will not work immutable

#int type (typically 64bit, but can be extended based on the values assigned/computed..)
#Size of a numeric type (infinate until the memory is filled)
age=43
print(type(age))
#float type
weight=101.75
print(type(weight))

#exponential
salary:int=int(1e5)
salary:float=1e6+.5

#Complex - used in the mathematical application, where we have the real and imaginary values for using in expresions.
a_compex=5j
a_compex=11-5j
print(a_compex)
print(type(a_compex))
#Functions on Number type:
print(age.__lt__(50))
print(age.__ge__(10))
print(salary.is_integer())
print(a_compex.conjugate())
print(a_compex.imag)
print(a_compex.real)

#Misc Types
#bool types (important) : used for performing logical, comparison and conditional operations
print(1==1 and 1==2)
print(1>1)
boolVal1=True
boolVal2=False
print((boolVal1 and boolVal2))
print((boolVal1 and 1==1))#logical and conditional if (boolVal1 and 1==1): do something..
print(boolVal1.__ge__(boolVal2))
print(boolVal1.__and__(boolVal2))
print(boolVal1.__or__(boolVal2))

#None (we should avoid getting it) - None means or Null means? Unknown value (it is not blank, it is not nothing, it is not empty)
a=''#this is not none, rather it is blank
a=[]#this is not none, rather it is nothing
aa=None#this is none (unknown)


#bytes (least bother) - used for converting the values to byte/binary format before transfer across the network or store in a encoded fashion
# or for processing in a secured fashion
name='irfan'
encoded_name=name.encode('utf-8','ignore')
print(bytes(encoded_name))
print(memoryview(encoded_name))
decoded_name=encoded_name.decode()
print(decoded_name)
age=43
age_in_bytes=bytes(age)
print(age_in_bytes)
print(type(age_in_bytes))

#Complex types - list, tuples, set, dict (we learn later deliberately)

print('G. Operators')
#Python supports operators -> assignment, arithmatic, comparison/relational, logical,
# unary (least priority), binary (least priority), ternary (least priority), bitwise (least priority)

#1.Assignment Operators (=)- used to assign some values to a variable - return the value/reference as a result
#x=input()
x:int=10#apply hint while assigning
x=10
z=0
z+=x#Both arithmetic and assignment is happening at the same time like (z=z+x)
z=z+x #Both above and this one are same
x,y=10,20 #Assignment of multiple values to multiple variables in one shot
a=10#= is an assignment operator to assign value
b=a*a#= is an assignment operator to assign result of aritmetic operated value
c= b > 90 #= is an assignment operator to assign result of aritmetic operated value and relational/comparison operated value
d= a*a > 90 or a>5 #= is an assignment operator to assign result of aritmetic operated value, relational/comparison operated and logical operated value

#2. Arithmatic Operators (+-*/**%..) - will returns operated value as a result
#operator precedence: there is an order of operators applied on the variables with higher priority */+-
x=(10+20) *5 #to avoid 20*5 and then add with 10, we are using brackets to perform 10+20 then multiple with 5
a=10
b=20
x=a+b
x=a/b
x=b%a
x=b**a
x=10e5
x=b.__add__(a)

#3. Relational/Comparison operators (==,>,<,>=,<=,!=) - Used for comparing variables and values and returns boolean type as a result
a=10
b=20
print(a==b,a>b,a<b,a!=b,a>=b,a<=b)

#4. Logical Operators (and, or, not) - apply logic between multiple output of the relational operators and Returns boolean
#or -
print((1==1 or 2!=2))#True
#and -
print((1==1 and 2!=2)) #False
#not -
print(not(1==1 and 2!=2))#nand True
print(not(1==1 or 2!=2))#nor False

#5. Bitwise Operators (&, |) - same like logical operator  (use rarely) -
#| for or
print(True | False)#True
#& for and
print(True & False) #False

#Unary - Operator used on a single variable
a=-10#- is the unary operator
#Binary - Operator used on two variable
b=10-20#- is the binary operator
#Ternary - Operator on multiple output based on condition
sal=100000
bonus=10000

print(sal+bonus) if sal>=100000 else print(sal)#this is ternary operator

#We see on daily basis:
#Learning Outcome of this program
#Before we develop some logic (simple/complex) -
# 1. Understand Business req, 2. Apply business requirement and arrive all scenarios,
# 3. Write Pseudo code, 4. Convert pseudo to actual syntax, 5. Apply & Test all the test cases..
#6. we learned how to use most of the important 4 operators
#Swiggy/Zomato
#Business req: minimum purchase cap (1000), discount percent 10% or max discount amt 200 rupees which ever is lower
#Scenarios/test cases
#Scenario1: amount of purchase = 2500, charge amout 2500-200=2300
#Scenario2: amount of purchase = 1500, charge amout 1500-(1500*.10)= 1500-150 = 1350
#Scenario3: amount of purchase = 900, charge amout 900 (no eligible offers)
#Pseudo Code to fulfilling all the above cases:
#runtime (modifiable) variables?
cust_amt:int=int(input("Enter the amount of purchase\n"))
#Static variables?
disc_pct:float=.10
disc_amt:int=200
min_amt:int=1000
#Pseudo code
#if cust_amt<min_amt then dont give any offer, print the same amount to pay else do the calculation for discuount
#Calculation for discount:
#if the (cust_amt*disc_pct)>=disc_amt then calculate final amount as cust_amt-disc_amt eg. 3000-200=2800
#else the (cust_amt*disc_pct)<disc_amt then calculate final amount as cust_amt-(cust_amt*disc_pct) eg. 1500-(1500*.10)=1500-150=1350
#Step by step convert the pseudo code to proper Code
if (cust_amt<min_amt):
    print(f"Scenario3 - Sorry not eligible for discount, pay the actual amount {cust_amt}")
else:
    print(f"Eligible for discount, pay the discounted amount")
    disc_pct_applied_amt=cust_amt*disc_pct
    if (disc_pct_applied_amt>=disc_amt):
        print(f"Scenario2- Discount percentage calculation is not applicable {disc_pct_applied_amt}, we are going apply discount amount {disc_amt} since disc amout < disc percent")
        disc_amt_applied_amt = cust_amt - disc_amt
        print(f"Final discounted amout to pay is {disc_amt_applied_amt}")
    elif (disc_pct_applied_amt<disc_amt):
        print(f"Scenario2- Discount percentage calculation is applicable {disc_pct_applied_amt}, since disc amout {disc_amt} > disc percent")
        disc_amt_applied_amt = cust_amt - disc_pct_applied_amt
        print(f"Final discounted amout to pay is {disc_amt_applied_amt}")

#How we used different operators in a single program
#8 operators we have learned?
#runtime (modifiable) variables?
cust_amt:int=int(input("Enter the amount of purchase\n"))
#Static variables?
disc_pct:float=.10#Assignment
disc_amt:int=-200#Unary Operator
disc_amt_ptv=abs(disc_amt)
min_amt:int=1000
if (cust_amt<min_amt):#Relational/Comparison
    print(f"Scenario3 - Sorry not eligible for discount, pay the actual amount {cust_amt}")
else:
    print(f"Eligible for discount, pay the discounted amount")
    disc_pct_applied_amt=cust_amt*disc_pct#Arithmetic operator, Binary operator
    if (disc_pct_applied_amt>disc_amt_ptv or disc_pct_applied_amt==disc_amt_ptv):#Logical Operator
        print(f"Scenario2- Discount percentage calculation is not applicable {disc_pct_applied_amt}, we are going apply discount amount {disc_amt_ptv} since disc amout < disc percent")
        disc_amt_applied_amt = cust_amt + disc_amt#Arithmetic, Binary operator
        print(f"Final discounted amout to pay is {disc_amt_applied_amt}")
    else:
        print(f"Scenario2- Discount percentage calculation is applicable {disc_pct_applied_amt}, since disc amout {disc_amt_ptv} > disc percent")
        disc_amt_applied_amt=cust_amt - disc_pct_applied_amt if (disc_pct_applied_amt < disc_amt_ptv) else 0   #ternary operator
        #disc_amt_applied_amt = cust_amt - disc_pct_applied_amt#Arithmetic, Binary operator
        print(f"Final discounted amout to pay is {disc_amt_applied_amt}")

print('J. Conditional Structure')
#Conditional structure part of programming will help us change the execution pattern/order a program based the boolean return of of a given condition
#I can/must/minimum have if condition alone -
#I must have if condition with else statement -
#I can have only else if or else statement -
#I can have if condition with else condition alone -
#I can have if condition with else if condition alone -
#I must have if condition with else if condition and else statement also -
#I should have my conditional structure started with if (if should be used only once),
# but can have multiple elif and should have only one else
#3 Types of conditional structure - simple (if/ if else), hierarchical (if elif elif else), nested (if->if->if elif else -> if else else if )
#Minimal (simple) Conditional Structure
#Conditional Structure with multiple condition - Hierarchical Conditional structure
#Nested conditional structure, which has to be used appropriately, needs lot of iterative testing

#########################################################################IF ELIF ELSE CODE BASE ##################################
# conditional structure
# 3 components - if,elif,else
# if is minimum needed and we have start conditional struct with if in the starting, rest all are optional
# after if i can use either elif or else or both
# after if, can we use another if?



# req1: I am planning for a trip to abroad by flight, based on the availability of amount,
# if i have amount then i will travel
amt_in_hand = 100000
flight_ticket = 95000

# Simple conditional structure
if amt_in_hand > flight_ticket:
    print("I am going to travel")

# req2: I am planning for a trip to abroad by flight, based on the availability of amount,
# if i have amount then i will travel else i don't travel
amt_in_hand = 100000
flight_ticket = 95000

# Simple conditional structure with else case
if amt_in_hand > flight_ticket:
    print("I am going to travel")
else:
    print("No enough money, hence I am not going to travel")

# req3: I am planning for a trip to somewhere by flight/train, based on the availability of amount, if i have amount then i will travel else i don't travel either in flight or train
# Hierarchical conditional structure with multiple cases
amt_in_hand=35000
flight_ticket = 15000
train_ticket = 15000
if amt_in_hand > flight_ticket:
    print("I am going to travel by flight")
elif amt_in_hand > train_ticket:
    print("I am going to travel by train")
else:
    print("No enough money, hence I am not going to travel")

# Hierarchical conditional structure, which has to be used appropriately, needs lot of iterative testing
# req4: I am planning for a trip, either by flight, train, road to somewhere with whichever the mode is cheap.
flight_ticket = 15000
train_ticket = 15000
bus_ticket = 15000
# pseudo code: ftb
# f<t and f<b then choose f, t<f and t<b then choose t else bus
# Nested Conditional Structure
if (flight_ticket <= train_ticket and flight_ticket <= bus_ticket):
    print(f"choosing flight {flight_ticket}")
elif (train_ticket <= flight_ticket and train_ticket <= bus_ticket):
    print(f"choosing train {train_ticket}")
else:
    print(f"choosing bus {bus_ticket}")

#IF WE TRY TO CONVERT THE ABOVE HIERARCHICAL TO NESTED, WE NEED TO HANDLE IT CAREFULLY, NOT SUGGESTED
#Conclusion: If we can handle using hierarchical or simple itself, then don't opt for nested...
#Lets rewrite the above hierarchical program into nested conditional structure....
flight_ticket = 9000
train_ticket = 10000
bus_ticket = 8000
if (flight_ticket <= train_ticket):
    #print("dead end")
    if (flight_ticket <= bus_ticket):
        print(f"choosing flight {flight_ticket}")
    else:
        print(f"avoiding deadend, opening a new path using else, this must be handled carefully, choosing bus {bus_ticket}")
elif (train_ticket <= flight_ticket):
    #print("dead end")
    if (train_ticket <= bus_ticket):
        print(f"choosing train {train_ticket}")
    else:
        print(f"avoiding deadend, opening a new path using else, this must be handled carefully, choosing bus {bus_ticket}")
elif (bus_ticket <= flight_ticket):
    if (bus_ticket <= train_ticket):
        print(f"choosing bus {bus_ticket}")
else:
    pass

# req5: I am planning for a trip, either by flight, train, road to somewhere with whichever the mode is cheap, provided only if i have enough amount in hand.
# Nested + Hierarchical Conditional Structure
amt_in_hand = 100000
flight_ticket = 15000
train_ticket = 15000
bus_ticket = 15000

# Below simple+nested+hierarchical program
#Line 604, 611 is an example of simple, line 604, 604 is an example of NESTED, line 605, 607, 609 is an example of HIERARCHICAL
#Below program is more optimized, but we can't avoid nested programming here..
#SQL Equivalent
''' select case when (amt_in_hand >= flight_ticket or amt_in_hand >= train_ticket or amt_in_hand >= bus_ticket)
 ((flight_ticket <= train_ticket and flight_ticket <= bus_ticket)) then 'choose flight'
or
(train_ticket <= flight_ticket and train_ticket <= bus_ticket))
 from tbl
select 'can i travel' from tbl
where (amt_in_hand >= flight_ticket or amt_in_hand >= train_ticket or amt_in_hand >= bus_ticket)
and
((flight_ticket <= train_ticket and flight_ticket <= bus_ticket)
or
(train_ticket <= flight_ticket and train_ticket <= bus_ticket))
'''
if amt_in_hand >= flight_ticket or amt_in_hand >= train_ticket or amt_in_hand >= bus_ticket:
    if (flight_ticket <= train_ticket and flight_ticket <= bus_ticket):
        print(f"choosing flight {flight_ticket}")
    elif (train_ticket <= flight_ticket and train_ticket <= bus_ticket):
        print(f"choosing train {train_ticket}")
    else:
        print(f"choosing bus {bus_ticket}")
else:
    print("No enough money, hence I am not going to travel by any means")

#  Below Nested+Hierarchical program is (optimized/not optimized)-not optimized
amt_in_hand = 100000
flight_ticket = 15000
train_ticket = 15000
bus_ticket = 15000
if (flight_ticket <= train_ticket and flight_ticket <= bus_ticket):
    if amt_in_hand > flight_ticket:
        print(f"choosing flight {flight_ticket}")
    else:
        print("No enough money, hence I am not going to travel by flight")
elif (train_ticket <= flight_ticket and train_ticket <= bus_ticket):
    if amt_in_hand > train_ticket:
        print(f"choosing train {train_ticket}")
    else:
        print("No enough money, hence I am not going to travel by train")
else:
    if amt_in_hand > bus_ticket:
        print(f"choosing bus {bus_ticket}")
    else:
        print("No enough money, hence I am not going to travel by bus")
########################################################################################################################################

#Usecase1 (novice): Find the greatest of 2 and then 3 numbers using built in functions (max(list of values))
a=10
b=20
c=30

#Usecase2:
#go to our site: www.inceptez.in -> home page popup -> based on the tab user chosed,
# we have provide options and based on the options clicked you are going to execute respective functionality...
# "if" user clicked on the popup then provide the options available upcoming batch or ask anything
# "if" user choosen upcoming batch -> ask user to choose either de or ds or cloud or devops else inform course is not available
# "if" user choosen ask anything ->


#looping Constructs:
#Iterative/repetitive execution of the set of program with some logic on top of the data/values/conditions,
# with different placeholder values used...
#Looping constructs can be executed with/without/in/outside of a conditional structure
#Concepts in Looping we are going to learn
#Types of loops - for, while
#Categories of loops - unconditional, conditional (sub category - entry controlled, exit controlled looping)
#syntax - for, while, break, continue, else
#WHAT IS LOOPING:
#Iterative/repetitive execution of the set of program with some logic based on the data/values/condition,
# with different placeholder values assigned and used...
#Looping constructs can be executed with/without/in/outside of a conditional structure

remote_list=[' tv ',' ac','fan']#data/values
#for loop will take each and every elements in sequence remote=' tv '
for hand_remote in remote_list:#Iterative/repetitive execution (3 times)
    print(f"placeholder value assigned for hand_remote is {hand_remote}")
    print(f"length of every values {hand_remote} {len(hand_remote)}")#set of program with some logics
    print(f"using this {hand_remote.strip()} I am switch on a device")#set of program with some logics

#Iterative/repetitive execution of the set of program = for or while loop with some logic writtern in the body
#hand_remote is a placeholder with value of am will be assigned first, then hand_remote will be assigned in the next iteration and so on until all values are iterated...

#Eg. of the below one is, we are going to perform some operations on the data present in a hive table unconditionally?
#Databases/Warehouses/Lakehouses uses the concept of looping only when we do a select fundamentally...
#select id from tablename is equal to -> for id in table: print(id)
#How a table with 2 columns can be represented in python
table=[(1,'irfan'),(2,'mani'),(3,'bharath')]
#Below for loop is equivalent to writing select * from table...
for row in table:
    print(row)

#Below for loop is equivalent to writing select upper(name) from table... because we prefer select rather than writing for loop,
# oracle/hive/spark/bigquery/synapse tools are introduced...
for row in table:
    id=row[0]
    name = row[1]
    print(name.upper())

#select upper(name) from table where name='irfan';
table=[(1,'mani'),(2,'irfan'),(3,'bharath')]
for row in table:
    id=row[0]
    name = row[1]
    if name=='irfan':
        print(name.upper())
    else:
        print(name)


#Looping constructs can be executed with/without/in/outside of a conditional structure
#possibilities:
'''
for alone
if inside for
for inside if
'''
#for alone
table=[(1,'irfan'),(2,'mani'),(3,'bharath')]
#Below for loop is equivalent to writing select * from table...
for row in table:
    print(row)
#Eg. of the below one is, we are going to perform some operations on the data present in a hive table provided if there is some data in the table?
#take the count of the table, if the count>0, then loop on each and ever rows and perform some operation using the select statement
#select * from wd34tbl where (select count(*) from wd34tbl)>0;
#if with for
table=[]
if len(table)>0:
    for row in table:
        print(row)
else:
    print("OK")

#We can run the loop and then check for some conditions using the if conditional structure
#eg. Query the hive table using the looping construct, check for a where clause (if condition) and execute the logic accordingly..
#select id hand_remote from wd34tbl where id>1;
#if inside for
table=[1,2,3]
for i in table:
    if i>1:
        print(i)
    else:
        pass

#In our so far learning of hive/mapreduce, did we used looping constructs or/and conditional structure? yes these constructs are used heavily
#Mapper collects, mapper filters... using what? collected using looping, filtered using conditional structure only...
#Hive select, where... using what? select using looping, where using conditional structure only...
#list command with some pattern matching is an example of looping with conditional structure...


#All about Looping Construct-> for, while, continue, break, else
'''
#What is looping - repetitive/iterative execution of some program based on some data/conditions..
Types -> UnConditional (for loop) & Conditional looping, Conditional looping (Entry controlled/Exit controlled) 
#Additional constructs syntax in the looping
break -> 
continue ->
else ->
'''
#Iteration or repetitive execution of the some tasks across data or conditions is called loops
#Two way of Performing Looping -
#unconditional
remote_list=[' tv ', ' ac', 'fan']
for i in remote_list:#Run the loop unconditionally
    print(i)

#conditional - Complex to write because it requires multiple variables, maintaining the state of variables/values,
# If we fail to maintain the state, chances of going out of bound or infinate looping
# , but more customizable...
#              0        1     2

remote_list=[' tv ', ' ac', 'fan']
no_of_remotes=len(remote_list)#3
start_val=0#Starting index

while (start_val<no_of_remotes):#Conditional looping
    print(remote_list[start_val].strip())
    start_val=start_val+1#Incrementing the index to pick the next item and to avoid infinate looping

#Conclusion: while loop is a conditional looping, relatively complex to use, hence for loop is preferred

#Realtime example of a Un-conditional looping
#I have a requirement of offering bonus to our employees working in inceptez
sal_list=[10000,20000,15000,25000]
bonus=1000
#bonus_applied_sal_list=[]
#bonus_applied_sal_list=[11000,21000,16000,26000]
#For loop is preferred because we have list of iterable elements with the fixed number of elements and we need to run the loop unconditinoally
for i in sal_list:
    #bonus_applied_sal_list.append(i+bonus)
    print(i+bonus)

#Let's try to understand the looping concept in detail with some case studies including the other constructs like break and continue:
#First lets' learn For loop -
#For loop will run on an iterable/sequence type only which has collection of elements/items (str, list, tuple, set, dict)
#For loop is a unconditional looping - We don't put any condition explicitly, loop will execute on all elements unconditionally
#For loop - number of iterations are already known - We can directly say the no. of iteration = the no. of elements/items
#Any looping has options for simple/nested looping

#Direct/Simple for loop
sal_list=[10000,20000,15000,25000]
bonus=1000
for i in sal_list:
    print(i+bonus)

#Nested For loop
#When Do we use Nested For loop
#wfh has to be given for all departments of all companies
#Requirement: Govt wanted to declare WFH for the IT companies due to some Flood/Covid
#If we relate with database, we are doing join (cartesian/cross join)
it_companies=['cts','infy','tcs','hcl','bny']
depts=['it','hr','security','mkt']
for comp in it_companies:
    print(f"company {comp}")
    for dept in depts:
        print(f"company {comp} and dept {dept} work from home")

#Requirement: I have 4 employees in my company, wanted to give bonus for each of them and output should be like below..
#Eg.  Employee Arun is getting a salary of 10000 after bonus of 1000 he is getting salary of 11000
emp_list=['Arun','Jaman','Bharath','Saravanakumar']
sal_list=[10000,20000,15000,25000]
bonus=1000
for emp in emp_list:
    for sal in sal_list:
        print(f"Employee {emp} is getting a salary of {sal} after bonus of {bonus} he is getting salary of {sal+bonus}")
#Using the above methodology, we can't achieve the desired result, because the nested looping will iterate on all the elements of inner loop for a given element of the outer loop...

#         0,Arun  1,Jaman
emp_list=['Arun','Jaman','Bharath','Saravanakumar']
sal_list=[10000,20000,15000,25000]
bonus=1000
i=0
for emp in emp_list:
   print(f"Employee {emp} is getting a salary of {sal_list[i]} after bonus of {bonus} he is getting salary of {sal_list[i]+bonus}")
   i=i+1

#We can use an important function "enumerate" to get the index and the value of a given list
#enumerate is equivalent to pos_explode in hive/spark
emp_list=['Arun','Jaman','Bharath','Saravanakumar']
sal_list=[10000,20000,15000,25000]
bonus=1000
for idx,emp in enumerate(emp_list):#0,arun   1,jaman
    #idx,emp=0,'Arun'
   print(f"Employee {emp} is getting a salary of {sal_list[idx]} after bonus of {bonus} he is getting salary of {sal_list[idx]+bonus}")


#Looping with Break and Continue constructs/clauses/syntax: for, while, break, continue, else
#Break - Stop the iteration of a loop if the break is applied based on a condition.
#Continue - Skip the current iteration and continue to the next one...
#else - if the loop is completed/broken/failed with a condition then go to else statement.

#Govt wanted to declare WFH for the IT companies due to some Flood/Covid,
#Based on the business criticality, IT companies wanted to skip some of the departments from WFH option
#continue:
it_companies=['cts','infy','tcs','hcl','bny']
depts=['it','hr','security','mkt']
for comp in it_companies:
    print(f"company {comp}")
    for dept in depts:
        if dept=='security':
            continue#Skip for security alone...
        else:
            print(f"company {comp} and dept {dept} work from home")

#Break -
#Requirement: Calculate the bonus applied salary for the employees getting salary more than 30000?
sal_list=[10000,20000,50000,70000,15000,35000]
bonus=1000
for sal in sal_list:
    if sal>30000:
        print(f"offering bonus for this salary {sal+bonus}")
    else:
        print(f"skipping this salary {sal}")
        continue

#or we can achieve the same above outcome using break also...
#Break is optimized/better in performance than using continue in this case...
#Have we seen this concept in Hive, spark, bigquery, synapse, redshift?
#
sal_list=[10000,20000,50000,70000,15000,35000]
sal_list.sort(reverse=True)#Desending order of sorting
#sal_list=[70000, 50000, 35000, 20000, 15000, 10000]
bonus=1000
for sal in sal_list:
    if sal>30000:
        print(f"offering bonus for this salary {sal+bonus}")
    else:
        print(f"breaking this salary {sal}")
        break
else:#for loop else
    print("all salaries are processed")

#Let us apply break to get a better performance of running the loop only to the desired iteration (3 times rather than 7 times)
#we have to sort and loop the data and break if condition meets

#We can achieve using continue also, but which is not optimistic solution, because "it iterates on all elements (7 times)"

#Usecase1 for for loop: Try create tables for your kids from 2 to how many (10) tables (get as an input)?
#input1: ending table Howmany tables you want (12 tables)
#input2: starting table 3 table
#input3: table to skip 5 table
#input4: in a given table what is the maximum numbers (15) to multiple , for example 3*15=45
#mi,mx=(input(),input())
#Generate a dynamic tables program that should take the starting table, ending table,
# skipping table and print in the below format, howmany table values is needed
#create a list1 with a range of 2 to 20 lst1=list(range(2,21))
#Table has to created upto 12 numbers
'''
2 * 1 = 2
2 * 2 = 4
2 * 3 = 6
.
.
2 * 12 = 24

3 * 1 = 3
3 * 2 = 6
.
.
3 * 12 = 36

'''

#While Loop

#Looping constructs available in Common Prog languages - for, while and do while
#Looping constructs available in Python language - for and while (no do while is available in python)
#Types of Looping - Entry Control & Exit Control loops

#All about While loop:
#While loop will run based on the boolean return of a condition
#While loop is a conditional looping - We add condition explicitly, loop will execute until the condition is fulfilled
#While loop - number of iterations can't be predicted because the iterations will be based on the initial value, condition output, incremental value etc.,
#for both for and while looping has options for simple/nested looping
#While loop has one more feature of used as an entry contolled or exit controlled looping

#While loop Challenges:
#1. Chances of getting infinate loop
#2. Challenge in maintaining the variables used in the conditions properly.
#3. Challenge in using the conditions

#Simple/Basic While loop:
'''
while condition is met:
 perform some operation
'''
import time
max_val=5
start_val=1
while start_val<max_val:#Conditional looping
    print(f"executing the loop of {start_val}<{max_val}")
    time.sleep(1)
    start_val += 1
else:#Not mandatory, but we can use for finding the else part of the loop
    print(f"loop did not run due to {start_val<max_val} or the loop is exhausted with the {start_val} < {max_val}")

#Realtime Example of using While loop: Entry controlled loop
#Usecase1: Login username/password used in our routine life
#We use CONDITIONAL looping with ENTRY contolling looping concept
#Entry control loop will run the loop minimum 1 time if the condition is met, otherwise not even single iteration of loop will run
initial_attempt=1
max_attempt=3
username=input("enter the username: \n")
stored_passwd='hduser'
while (initial_attempt <= max_attempt and ['irfan','saranya','mayavan'].count(username)>0):#before i allow the user to try the password, it will put some condition
        user_passwd = input("enter the password\n")
        if user_passwd == stored_passwd:
            print(f"Hello {username} \n ******** Welcome ********")
            break
        else:
            print("try again")
            initial_attempt += 1
            #continue
else:
        print("3 incorrect password attempts")

#Example of exit controlled loop (allow the loop to execute without validating anything in the entry), validate later in the exit..
initial_attempt=1
max_attempt=3
username=input("enter the username: \n")
stored_passwd='hduser'
while (True):#before i allow the user to try the password, it will put some condition
        user_passwd = input("enter the password\n")
        if (initial_attempt <= max_attempt and ['irfan', 'saranya', 'mayavan'].count(username) > 0):
            if user_passwd == stored_passwd:
                print(f"Hello {username} \n ******** Welcome ********")
                break
            else:
                print("try again")
                initial_attempt += 1
        else:
            print(f"{username} is not in the sudoers file.  This incident will be reported.")
            break
            #continue


#Usecase2 related to exit controlled loop (do while loop) + break & continue:
#Create a scheduler program to run a code minimum once or continue to run multiple hours + skipping odd hours
'''
Exit control loop is represented in other programming languages as do while loop, but python don't have do while loop specifically,
rather we can use exit control loop as an alternative for do while loop
scala> do{ print("Exit controlled loop")
    }while(1>2)
user is allowed
scala> while(1>2){print("Entry controlled loop")}
'''
#sfm_insure.py
lst_odd_hrs=list(range(1,24,2))
'''lst_all_hrs=list(range(0,24))
lst_odd_hrs=[]
for i in lst_all_hrs:
    if i%2==1:
        lst_odd_hrs.append(i)
'''
#lst_odd_hrs=list(range(0,24,2))
lst_odd_hrs=[3,5]
while(True):#Exit control loop
    print("loop is running unconditionally")
    for i in lst_odd_hrs:
        if i%2 != 0:
                print(f"running some program at {i} hour")
        else:
                print("no iteration of program to run")
                continue
    else:
        break

#Exit control looping

odd_hr=3
while(True):#Exit control loop
    print("loop is running unconditionally")
    if odd_hr%2 != 0:
                print(f"running some program at {odd_hr} hour")
                break
    else:
                print("no iteration of program to run")
                break

##############################################Condition Structure & Looping Constructs####################################

print('K. Collection/Complex Types') #Data Structure (vague topic, 3+ dimension)...
#Application of using collection types in realtime world?
#Self served metadata driven Data movement automation (DMA, DMT, DQF(DQAAS, ACCura), DAF, nifi/minifi/kylo, DPF, TVCF, AIBOT, ) tool
'''
{"process": "ETL Process1",
  "source": [
    "hive",
    "Bigquery"
  ],
  "target": [
    "HDFS",
    "GCS"
  ],
  "cols": [
    "custid",
    "upper(custname) as upper_custname"
  ],
  "tablename": "customer",
  "where": "(city='chennai')",
  "gcs_uri": "gcs://abc/xyz_bucket/"
}
'''

#This is outcome of our next 1 hour learning...
#users -> webgui -> choose source system/source table/tgt system/tgt table/ETL(query)/username/pwd
import json
file1=open("/home/hduser/metadata.json",'r')
json_parsed=json.load(file1)
process=json_parsed['process']
source=json_parsed['source']
query_string=f"create table cust_target as select {json_parsed['cols']} from {json_parsed['tablename']} where {json_parsed['where']}"
print(f"running the program {process} query in {source[1]} {query_string}")

#Hive - Array [] (designation), Map {} (other_info), Struct {} (address)
#Python-list [],                dict {},             Tuple (), Set/Frozen Set {}

#What is a collection/complex type?
#Collection or group of values that stored in a format for managing the different complex data efficiently

#Examples of Collection Types in order of importance (list, dictionary, tuple, set) :
#list [] (hive array)
#Defenition: collection of same datatype items
#Indexed Sequenced collection of homogeneous items/elements/values of variable elements
desig_lst=['SE','SSE','TL','PM']
sal_lst=[10000,20000,40000,100000]

#How to access/select the elements/items of a list? using index value starts with 0
print(f"first salary of the emp: {sal_lst[0]}")
print("Want to access all elements of a list")
for sal in sal_lst:
    print(sal)


#dictionary {} (hive map)
#Defenition: collection of key and value pair
#Indexed Sequenced collection of homogeneous items/elements/values
desig_dict1={'SE':10000,'SSE':20000,'TL':40000,'PM':100000}
aspirants_dict2={'murali': {'age':35,'height':5.10,'weight':75},'irfan': {'height':5.11,'age':42}}

#How to access/select the elements/items of a dictionary? using key
se_sal=desig_dict1['SE']
sse_sal=desig_dict1['SSE']
for i in desig_dict1.items():
    print(i)


#tuple () (hive struct) (not much important)
#tuple is index sequence collection of hetrogeneous type of fixed elements
emp_address=(1,'ags colony','velachery','chennai')
emp_address.__add__('tamilnadu')

#set {} (hive struct) (not much important)
#set is iterable type of unique/distinct homogeneous elements, mainly used for performing set operations...
emp_countries={'SE','SSE','TL','PM','TL'}

#Notataions:

#Example of all collection types used:
#{'process': 'ETL Process1', 'source': {'hive', 'Bigquery'}, 'target': ['HDFS', 'GCS'], 'cols': ['custid', 'upper(custname) as upper_custname'], 'tablename': 'customer', 'where': "(city='chennai')", 'uris': ('gcs://abc/xyz_bucket/', 100)}

#Different types of collection types? in the order of importance
#list, dict, tuple, set

#Why we need collection types?
#To manage/store/parse the complex dataset in a hirarchical/nested/complex structure stored or to process semi structure data, nested data,

#Different characteristics of collection types?
#Iterable (looping), mutable (changable) - updatable (modifyable) & resizable (added/removed), accessible (select using index, position, value, key)

######What are the topics we have to learn in collection types#######
#Iterable?

#Notation, access, resizable/mutable/immutable?  insert/update/delete, functions to apply
#All the above we are going to see in detail
#Notation:
#Accessed using ?
#Definition: Indexed, sequenced collection of homogeneous elements

print("list operations")
#List can be hetrogeneous too (but not suggested, why ? because while operate between the elements of the list, program fails because python is a strongly typed language)


#All the python collections are iterable -


#select/access


#insert/update/delete (list is mutable, hence updating and resizing (add/removing) is possible)

#append in the last (proves list is mutable/resizable/can be inserted)


#insert in the index position


#update the list elements (mutable)

#delete the elements of the list using value


#delete multiple same elements using the value


#pop (delete) the elements of the list using index


print("list after popping out a given index element")

#search for a value with in the given index (range) value and pop(remove) it

#Wanted to remove the duplicate in a given list?
#Convert to set and back to list

#certain builtin functions to try out on list

print("Dictionaries (mutable) - {k:v, k:v}")

#Access a dictionary - using key


#Adding Items - if the key is not found


#Updating Items - if the key is found

#Removing an Item (from the last)

#Delete(pop) the given key

#Delete all the elements of a dict

#Iteration of Dictionary
#Iterate on the items of the Dict - will return what datatype???


#Iterate on the keys of the Dict - will return what datatype???respective key's datatype

#Iterate on the values of the Dict - will return what datatype???respective value's datatype

#Some additional functions

#Setdefault will add the key and value provided if key is not present already, if already present consider the given value and not the default value

#create a dictionary with the keys from list and value from the second argument


print("Tuples (immutable?)")
#Definition of Tuple:Tuple is an indexed sequenced collection of hetrogeneous elements, tuples are immutable (non updatable and non resizable)
#Notation is ()


#select/access
#City where Anirudh present

#count of some element in the given tuple

#search for some element in the given tuple to identify the index


#Resizable?
#Try to Add some elements to the tuple, lets try to add age of Anirudh
#Insert/Append?

#delete?

#Modify (update) -

#I want to achieve Insert/update/Delete in a tuple? Not possible by default,
# but we can do some workaround to achieve it? convert to list , do insert update delete and convert back to tuple

#Do all operations/functions that list supports (#Other functions to apply)
#Insert

#Update

#Delete


print("Set (mutable) (least important)- Notation {} - ")

#set is iterable?

#set is mutable?

#set is mutable (resizable) -

#set is supported with set operation (If we use set, we use it for these purposes)
#Requirement of identifying the common department in the given lists

#intersect - combine both the sets

#difference (difference/subtract/minus) - find the difference between the sets
