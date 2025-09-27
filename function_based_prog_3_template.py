'''
What is a Function/Method? Aspirant's response

'''

#FUNCTION BASED PROGRAMMING (Python is a pure FBP Language, Python treats Functions as first class citizen)
#What?
#Function/Method is a stored program that perform certain/set of tasks

#Why we need to create Functions or why we need FBP -
#1. Functions can be created once and reused multiple times - reduced complexity, reduced LOC, Precise, Maintainable
#2. Functions are used to call/run in a parallel (I have 1000 rows, running a function in 10 parallel threads with each thread handles 100 rows)
# and in concurrent fashion (I am calling a single function at the sametime from 10 diffent applications/programs)
#3. Functions help us reduce the LOC by reusing and by composing
#4. Functions are used for creating Application/Organization specific Reusable Frameworks
# (Masking FW, DMA FW, Metricbot, DQ FW, DQaaS, Datacurra, DAAF etc.,)
# Generic Frameworks (Spark/Airflow/glue/great expectation/deeque)
# or custom functionalities (udf, custom functions, Cloud functions) or
# centralized functionalities (If we change the function in one place, that affects the entire consuming applications of the given functions
# eg. change in bonus calculation in one place)

#Benifits/Features of Functions in Function Based Programming or Why FBP?
#I have Function/Method created called Fun
#1. Concurrency - Calling the method/function "Fun" at the same time from multiple different applications/programs
#2. MultiThreading/Parallelism - Running (Multiple threads/instances to divide the workload evenly in a single computer) of the method/function "Fun" at the same time by multiple different applications/programs or a single appication
#3. Distributed (parallelism) function call - Running (Multiple threads/instances to divide the workload evenly in a cluster) of the method/function "Fun" at the same time across different computers
#4. Simple/Elegant - Program created once and reused, easily maintained, reduced LOC, ease of usage.

#FBP – Characteristics
#In Python functions are first class citizens, that means functions are given equal priority as like variables or a variable can be treated as a function

#Functions are composable - to achive complex output, we don't have to create a complex function rather we can call/compose simple functions


#Functions are not time bounded (stateless or no side effect) - We can call functions any number of times
#Below anonymous code is a time bounded (call the same logic will vary based on how many times you call)

#If i convert the above code into a function, it will become non time bounded (call the function any time the result will not vary)


#All about Functions or Methods in FBP - syntactically...
###################################################
#1. How to Create a function and call a function (High level)
#1. Minimal/least way of creating a method
#Minimum we can create a function with def keyword followed by function name followed by () followed by : followed by body code of a function

#2. Regular/Optimal/typical/formal way of creating a method

#We need to have a def keyword (definition of a function) - (mandatory) any function/method creation has to have starting with def keyword
#followed by the function name - (mandatory), lower case with underscores or just lowercase words
#followed by argument(s) - optional
# with datatype mentioned (to hint us understand the datatype signature of the method)- optional
# mentioned inside the brackets() - mandatory
#followed by ':' (completion of the definition) - mandatory
#followed by - some description in ''' , to display the methods description when hover - optional
#followed by the body of the program (one/multiple lines of code - core logics + std output + return) - mandatory with atleast 1 line
#followed by return keyword - where as return help us send back result to the calling environment - optional

#3. What are the possible way of creating functions/methods
#all permutation and combination works...

#a.Method with no input arguments and no return - eg. exit used in hive

#Quick Usecase: Create a function to delete temporary hardcoded folder /home/hduser/tmp and identify it is not returning anything

#Let us call the above functions ...

#b.Method with input arguments and no return - delete from tablename where city='chennai';

#Quick Usecase: Create a function to delete a temporary folder eg. /home/hduser/tmp or /tmp/tmp etc.,
# which can be passed as an argument dynamically and identify it is not returning anything

#c.Method with no input arguments but return - select status from tablename;

#Quick Usecase: Create a function to check whether the given hardcoded temporary folder /home/hduser/tmp exist or not
# getting a return type of true or false

#d.Method with input arguments and return - select status from tablename where city='chennai';


#Quick Usecase: Create a function to check whether the temporary folder passed as an argument /home/hduser/tmp or /tmp/tmp exist or not
# getting a return type of true or false

#4. How do we call the Methods:
#How to just print the output of a function

#How to store the output of a method and use that output/return value further as an input to other functions


#Simple usecase:
# a. Complete the Swiggy/zomato usecase (anonymous program) by creating a formal reusable method/function
# b. and add exception handling also in it..

#5. How to create & call the methods using different Argument types: Important part
##############################################################################
#Different type of methods/functions arguments are there -
# positional arg func, named/keyword arg func, default arg func, arbitrary arg func, keyword arbitrary argument function


#A. Positional arguments methods

#B. Named/Keyword arguments methods

#c. Default arguments methods -

print("only default arguments")

print("named with default arguments")

#d. Arbitrary (any numbers) Argument Method/Function - Accepts the argument as tuple with the notation of *argument_name
# If we are not sure about the number of arguments that we are going to pass to this method, but we use the same order (position) of passing the arguments

print("d.Arbitrary Argument Function/Method")


#e. Keyword Arbitrary Argument Method/Function - Accepts the argument as  with the notation of **argument_name
# If we are not sure about the number of arguments that we are going to pass to this method and
#the order of the argument we are going to pass is unknown (Named arguments) , we can use keyword arbitrary arg method

print("e. Keyword-Arbitrary Argument Function/Method")

#Usecase: Create a method to calculate sal+bonus+incentives for differenct IT companies


#6. Special Types of Methods/Functions in Python - Is not much important for creating/implementing the methods by Dataengineers,
#but for understanding the type of methods/functions used in the framework, the below learning is useful.
# FBP (special methods) - Higher Order Function, Anonymous/lambda/function literal/value function,Closures, recursive functions/tail recursion
# OOPs (special methods)- instance (default), class,static methods
print("**********Special Types of Methods/Functions in Python - Important (interview purpose)***************")
#a. Higher Order Functions - Top priority
print("Benifits of HOF1 -> 1. We can use the functions seperately or along with other functions "
      "2. Rather than rewriting the code in a given function we can reuse it by passing the function as an argument ")


#Realtime example : Calculate the salary of our employees based on working days

#How to convert the above method into HOF and what is the benifits of doing it?

print(f"HR Sending a mail to the supervisor about the days the given employee didn't worked for a given month ")
print(f"Finance Depositing the final salary for the given employee in bank ")

#Usecase to understand HOF1: Create a calculator method that should take add/sub/mul/div method as an input argument

print("b. Closures Functions")
print("What is closure? If the result of a given method is changed/affected by the value defined outside of the given function ")

#Usecase Can you create a method called calc_sal_bonus_incentive using a higher order method and closure concepts?

print("c. Lambda Function - A function created anonymously or a function as a variable using lambda keyword")
#Lambda functions can be called as function literal/anonymous function/value function
#Interview Question: Diff between methods & functions -
# Method: Any functionalities/store program created with def keyword (syntactically)

# Method: Can be used for some common, complex (logic can be in multiple lines) functionality purposes across the modules of an application

# Function: Any simple functionalities/store program created with lambda keyword (syntactically)

# Function: Can be used for some anonymous/adhoc, simple (logic should not be in multiple lines) functionality purposes within the given module, not across the module


print("d. Recursive Function or tail recursion - A function called by itself repeatedly or recursively")

#Realtime example of Recursive Function? SIP, FD, Complex Interest (interest for interest)
#I am investing 100000 rupees with an return of 10% year over year, after 3 years what is my return?
#100000 -> 100000+10000=110000 (year1) -> 110000+11000=121000 (year2) -> 121000+12100=133100 (year3)

#Lets write the above function in a single recursive function


#Some of the interview questions asked in python or any other programming languages?
#Find the given value is prime number or not
#calculate the even or odd values from the given list
#build a pyramid using python
#check whether given value is palindrome
#create fibboneci series 0,1,1,2,3,5,8,13,21 (Agile/Scrum - Sprint planning -story points)
#create factorial of n numbers - fact(4) = 4*3*2*1
#usecase: to calculate factorial or fibboneci series using recursive function?


#Factorial of n number


#7. Scope of Variables in Functions/Methods - Local and Global variable
print("7. Scope of Variables in Functions/Methods - Local and Global variable")
print("a. Local Variable - variable created inside a method is local by default")

print("b. Global Variable - No need of global keyword, since by default variable in module is global")

print("c. Local Variable defined as global - By using global keyword we can achive")
