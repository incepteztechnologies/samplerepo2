'''
What is a Function/Method? Aspirant's response
Reusable Block of code to do some specific task when ever we call and it can be kept in a centralized program
Group of predefined codes that can be used for performing multiple tasks
Reduce the code complexity and easy to understand
How we can call a function -> Concurrently, Parallely, Distributedly, Recursively
'''

#Anonymous Coding, non centralized, not reusable, not generic, simple to again write, precise, hard in maintainability,
#which cannot be called concurrently/parallely/distributedly/recursively
import shutil
import os
if os.path.exists("/home/hduser/tmp"):
    shutil.rmtree("/home/hduser/tmp")
else:
    print("path doesn't exist")

#FBP Coding, centralized, reusable, generic, simple to access, precise/easy, easy to maintainability,
#which can be called concurrently/parallely/distributedly/recursively
def cleanup_tmp_dir():
    import shutil
    import os
    if os.path.exists("/home/hduser/tmp"):
        shutil.rmtree("/home/hduser/tmp")
    else:
        print("path doesn't exist")

def cleanup_tmp(tmpdir):#function/method
    import shutil
    import os
    for i in tmpdir:
        if os.path.exists(i):
            shutil.rmtree(i)
        else:
            print("path doesn't exist")

cleanup_tmp(["/home/hduser/tmp","/home/hduser/tmp1","/home/hduser/tmp2"])

#Single program with fundamentals, exception handling and function based programming applied...
def cleanup_mv(tmpdir):#function/method
    try:
        import shutil
        import os
        dir_to_delete=tmpdir.get("del")
        dir_to_move = tmpdir["mv"]
        if dir_to_delete!=None:
            for i in dir_to_delete:
                if os.path.exists(i):
                    shutil.rmtree(i)
                    print(f"directory deleted is {i}")
                else:
                    print("path doesn't exist")
        print("moving directory")
        shutil.move(dir_to_move[0],dir_to_move[1])
    except Exception as err:
        print(f"some exption occured {err} is not found")

cleanup_mv({"del":["/home/hduser/somedir1","/home/hduser/tmp1","/home/hduser/tmp2"],"mv":["/home/hduser/mv_dir","/home/hduser/mv_dir_renamed"]})

#FUNCTION BASED PROGRAMMING (Python is a pure FBP Language, Python treats Functions as first class citizen)
#What? Function/Method is a stored program that perform specific/set of tasks

#Why we need to create Functions or why we need FBP -
#1. Functions can be created once and reused multiple times - reduced complexity, reduced LOC, Precise/simple/ease of understanding, Maintainable
#2. Functions are used to call/run in a parallel (I have 1000 rows, running a function in 10 parallel threads with each thread handles 100 rows)
# and in concurrent fashion (I am calling a single function at the sametime from 10 diffent applications/programs)
# and extend FBP to achieve distributed parallelism also
#single thread - a function run with only one instance(copy) on a given task sequencially.
#parallelism - a function run with multiple instance(copy) on a given task parallely but to some extend.
#concurrently - a function can be called by different applications at the same time.
#distributed parallelism - a function run with multiple instance(copy) on a given task distributed & parallely to any extend (leveraging the power of cluster).
#3. Functions help us reduce the LOC by reusing and by composing
#4. Functions are used for creating Application or Organization specific Reusable Frameworks
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
a_var=10#a variable can hold value
class cls1():
    pass
a_obj=cls1()#a variable can refer a program in the memory (object)
a_function=lambda x:x*x#a variable can hold or act as a function
print("square root of 10 is ",a_function(10))

#Functions are composable - to achive complex output, we don't have to create a complex function rather we can call/compose simple functions
data={"id":1,"name":"mohamed irfan"}
print(len(data.get("name").split(" ")[0]))#5 functions i composed to get the length of the first name, because there is no single function available to achive this...
#data.get("name").split(" ")[0].__len__()

#Functions are not time bounded (stateless or no side effect) - We can call functions any number of times
#Below anonymous code is a time bounded (call the same logic will vary based on how many times you call)
a=1
if a>0:
    a+=2
    print("1",a)

if a>0:
    a+=2
    print("2",a)

if a>0:
    a+=2
    print("3",a)

#If i convert the above code into a function, it will become non time bounded (call the function any time the result will not vary)
def fun1():
    a=1
    if a>0:
        a+=2
        print(a)

fun1()#1
fun1()#2
fun1()#3

#All about Functions or Methods in FBP - syntactically...
###################################################
#1. How to Create a function and call a function (High level)
#1. Minimal/least way of creating a method
#Minimum we can create a function with def keyword followed by function name followed by () followed by : followed by body code of a function
def fundamental_fun():
    print("function is called")

fundamental_fun()

#2. Regular/Optimal/typical/formal way of creating a method
def complete_function_syntax_symantics(a:int,b:int):
    '''This function will help us add the input parameters and return the sum of those 2'''
    c=a+b
    #print(c)
    return c

#We need to have a def keyword (definition of a function) - (mandatory) any function/method creation has to have starting with def keyword
#followed by the function name - (mandatory), lower case with underscores or just lowercase words
#followed by argument(s) - optional
# with datatype mentioned (to hint us understand the datatype signature of the method)- optional
# mentioned inside the brackets() - mandatory
#followed by ':' (completion of the definition) - mandatory
#followed by - some description in ''' , to display the methods description when hover - optional
#followed by the body of the program (one/multiple lines of code - core logics + std output + return) - mandatory with atleast 1 line
#followed by return keyword - (optional) where as return help us send back result to the calling environment

#3. What are the possible way of creating functions/methods
#all permutation and combination works...
#a.Method with no input arguments and no return - eg. exit used in hive or set hive.cli.print.header;
def fun1():
    print("do some thing")
fun1()

#Quick Usecase: Create a function to delete temporary hardcoded folder /home/hduser/tmp and identify it is not returning anything
def cleanup_tmp():
    import shutil
    import os
    if os.path.exists("/home/hduser/tmp"):
        shutil.rmtree("/home/hduser/tmp")
    else:
        pass

#Let us call the above functions ...
cleanup_tmp()

#b.Method with input arguments and no return - delete from tablename where city='chennai';
def fun2(city):
    print(f"delete from tablename where city='{city}';")
    print("this many rows deleted")
fun2('chennai')
fun2('hyderabad')

#Quick Usecase: Create a function to delete a temporary folder eg. /home/hduser/tmp or /tmp/tmp etc.,
# which can be passed as an argument dynamically and identify it is not returning anything
def cleanup_tmp(dir):
    import shutil
    import os
    if os.path.exists(dir):
        shutil.rmtree(dir)
        print(f"given directory is deleted {dir}")
    else:
        pass

cleanup_tmp('/home/hduser/tmp')
cleanup_tmp('/home/hduser/tmp1')
cleanup_tmp('/home/hduser/tmp2')

#c.Method with no input arguments but return - select count(1) from tablename;
def fun3():
    print(f"select count(1) from tablename;")
    return 1000
fun3()
fun3()

#Quick Usecase: Create a function to check whether the given hardcoded temporary folder /home/hduser/tmp exist or not
# getting a return type of true or false
def check_dir_file():
    import os
    return os.path.exists('/home/hduser/tmp')#function execution will be stopped
    return os.path.exists('/home/hduser/tmp1')


#d.Method with input arguments and return - select count(1) from tablename where city='chennai';
#Can we return multiple values in one return statement?Yes
#Can we have multiple return statements in a function? Yes
#Only one return will work? True
#return has to be the last statement of a given function (under the given functionality)? True
def fun3(city):
    print(f"select count(1) from tablename where city='{city}';")
    if city=='chennai':
        return city,1000
        return city
        print("returned 1000 count")
    elif city=='hyd':
        return city,500
        print("returned 500 count")
    elif city=='mum':
        return city,1500
    print("function completed")

print(fun3('chennai'))
print(fun3('hyd'))

#Quick Usecase: Create a function to check whether the temporary folder passed as an argument /home/hduser/tmp or /tmp/tmp exist or not
# getting a return type of true or false
def check_del_dir_file(path):
        import os
        import shutil
        if os.path.exists(path):
            try:
                shutil.rmtree(path,ignore_errors=True)
                return (True,"deleted")
            except Exception as e:
                print(f"some exception occured {e}")
                return (True, f"Not deleted {e}")
        else:
            return (False,"Not deleted")


#4. How do we call the Methods:
def add_vals(a:int,b:int):
    '''add the 2 input params'''
    c=a+b
    #print(c)
    return c

#How to call the above function
add_vals(10,20)#it runs, but of no use since no print or no return

#How to just print the output of a function
add_vals(10,20)#it runs, meaningful if we have print in it..

#How to store the output of a method and use that output/return value further as an input to other functions
return_val=add_vals(10,20)#it runs, meaningful if we have return in it..
operating_on_the_return=return_val+100
print(return_val)

#Simple usecase:
# a. Complete the Swiggy/zomato usecase (anonymous program) by creating a formal reusable method/function
# b. and add exception handling also in it..

#5. How to create & call the methods using different Argument types: Important part
##############################################################################
#Different type of methods/functions arguments are there -
# positional arg func, named/keyword arg func, default arg func, arbitrary arg func, keyword arbitrary argument function
#Irfan, Are you declare the arg with dtattype?
#i am hinting the argument with the type
def calc_sal_bonus(sal:int,bon:int,inc:int):
    '''Function to calculate the salary applied bonus'''
    bonus_value=bon/100# 10/100=.10
    final_bonus_applied_sal=round(sal+(sal*bonus_value)+inc)#10000+(10000*.10)
    return final_bonus_applied_sal

#Different arguments methdologies of calling this functions:
#A. Positional arguments methods
#table (id int,name string) -> insert into table values(1,'irfan') #positional
final_sal=calc_sal_bonus(10000,20,1500)#Passing the arguments based on the position
print(final_sal)
final_sal=calc_sal_bonus(20,10000,1500)#Passing the arguments not based on the position (result with wrong values)
print(final_sal)
#B. Named/keyword arguments methods
#table (id int,name string) -> insert into table(name,id) values('irfan',1) #positional
final_sal_IT=calc_sal_bonus(bon=10,sal=10000,inc=1500)#Passing the arguments not based on the position but based on name/keyword works
print(final_sal)

#c. Default arguments methods - If the function is not called with enough argument values, then default value can be used
def calc_sal_bonus(sal:int=5000,bon:int=5,inc:int=1000):
    '''Function to calculate the salary applied bonus'''
    bonus_value=bon/100# 10/100=.10
    final_bonus_applied_sal=round(sal+(sal*bonus_value)+inc)#10000+(10000*.10)
    return final_bonus_applied_sal

print("only with default arguments")
final_sal_MKT=calc_sal_bonus()
print(final_sal_MKT)

print("positional, named and default arguments")
final_sal_MKT=calc_sal_bonus(10000,inc=2000)
print(final_sal_MKT)

#d. Arbitrary (any numbers) Argument Method/Function - Accepts the argument as tuple with the notation of *argument_name
# If we are not sure about the number of arguments that we are going to pass to this method, but we use the same order (position) of passing the arguments

print("d.Arbitrary Argument Function/Method")
def fun1(*abcd):
    print(abcd)
    print(type(abcd))

#Realtime example of this arbitrary argument function?
#Usecase: Whoever is joing Inceptez (employee/vendor), we need to create mailid for them.
#mohamed, irfan, cts.com -> mohamed.irfan@cts.com
#mohamed,irfan -> mohamed.irfan@inceptez.com
#mohamed -> mohamed.emp@inceptez.com

def generate_mail(*args):
    print(args)
    print(type(args))
    default_domain='@inceptez.com'
    arg_len=len(args)
    if arg_len==3:
        return args[0]+'.'+args[1]+'@'+args[2]
    elif arg_len==2:
        return args[0] + '.' + args[1] + default_domain
    elif arg_len==1:
        return args[0] + '.employee' + default_domain

#e. Keyword Arbitrary Argument Method/Function - Accepts the argument as  with the notation of **argument_name
# If we are not sure about the number of arguments that we are going to pass to this method and
#the order of the argument we are going to pass is unknown (Named arguments) , we can use keyword arbitrary arg method

print("e. Keyword-Arbitrary Argument Function/Method")
def fun1(**kwargs):
    print(kwargs)
    print(type(kwargs))


def generate_mail(**kwargs):
    print(kwargs)
    print(type(kwargs))
    #default_domain='@inceptez.com'
    return kwargs.get("fname")+'.'+kwargs.get("lname")+'@'+kwargs.get("domain")

generate_mail(lname='irfan',fname='mohamed',domain='infosys.com')

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



#7. Scope of Variables in Functions/Methods - Local and Global variable
print("7. Scope of Variables in Functions/Methods - Local and Global variable")
print("a. Local Variable - variable created inside a method is local by default")

print("b. Global Variable - No need of global keyword, since by default variable in module is global")

print("c. Local Variable defined as global - By using global keyword we can achive")
