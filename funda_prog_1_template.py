#Refer python_theory/notes for understanding few basics of python...

print("************** 1. Basics of Python Programing*************")
'''Day1 Learning (theory)'''
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
#4. By default 4 spaces we will give for indends, but more/less spaces or tabs also can be used...

#Indendation is needed for (hierarchy of programming), because we are doing block operation (lines of code) with in the for loop


#Linux is not an intend based program, it is a block based rather:


#indendation has to be uniform within the block of code (not across the block of code)
#below prog doesnt work because we are using different number of spaces between lines of code in a given block


#below prog doesnt work because we are using different keys like spaces for one line and tab for another line


#optimal number of spaces has to be 4, but any numbers you can give


print("B. This is a commented line in Python")


print("C. Playing with Quotes: Python treats single quotes the same as double quotes as like triple quotes, but has some differences")
#Python treats single quotes the same as double quotes and triple quotes.


##we can use escape sequence also

#Double quotes is used for holding single quoted chars

#Triple double quotes is used for muliline
#For handling paragraph/multilines text, we can use 3 single or doublequotes


#Any programming language learning has to be started first learning about variables
print("Let's learn all about VARIABLES")
'''1. Variable Properties - Dynamic Inference, Dynamic Typed, Strongly Typed'''

#Dynamic inference - based on the assigned value to a variable, it will automatically decides/infer/identify/refers the data type dynamically

#Dynamically typed: If a variable is created with a specific data type, can be changed later

#below is possible, because python is dynamically typed language (Duck type language)


'''Scala is a statically typed language

#below is not possible - because of statically type feature

'''

#Strongly typed: Python allow us to operate between the variables of same datatype (of the same hierarchy) and doesn't allow to operate between different datatypes.


'''Day2 Learning '''
#2. naming convention
#A variable can have camel case or init upper or with underscores

#A variable name must start with a letter or the underscore character

#A variable name cannot start with a number
#below doesnt work
#

#A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )

#below doesn't work
#
#Variable names are case-sensitive (For Eg:)

#Multiple Variables can be assigned in a single line (Multi Assignment)
#all are different...


#3. How to check a given TYPE is of what datatype we expect  & type casting

#What we are learning here is the usage of few functions like isinstance(),str(),type()
#To understand the age is of what type

#To check wheter the age is of an expected type

#To convert the age to an expected type


#
#Above code will not work. Since Python is strongly typed language, we can't operate between age:int and desc:str , hence we have to type cast age to string

#Check for a given type, if it is not as expected then cast it to the expected type programatically using if condition

#4. input (assigning value directly/using input function/passing arguments) / output (print/assigning/return)
#assigning value directly (Hardcoding)

#assigning value directly (applying some functionalities/operations/program on some other/same variables)


#Run time input
#below input will collect salary as string (using input function)

#below input will collect salary as string and type cast to int


#pass parameters to a variable when we use functions (FBP and OOPS we learn in detail)


print("D. Standard output options of print statements")

#print statement will be used as a std output function, which will use \n in the end by default, no need of using println like scala kind of lang
#semi colon can be used to seperate a statment if we write multiple statements in one line

#below print function is taking only 1 argument (but print can take any number of arguments)

#below print function is taking multiple arguments and printing them individually

#Formatted string Print statements - positional args
#Positional arguments

#keyword/named arguments

#Formatted string Print statements other way (3.6x onwards) - named args
