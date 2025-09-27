#ANY Prog that we write, first ensure the prog is going to be handle all possible failure scenarios gracefully
#If anything still goes wrong, then use except block to handle it..
#try:#try something level best (simply bring all our code into try block)
    #actual code
#except Exception :
    #handler code

#EXCEPTION HANDLING
#Understanding of Exception: what? unexpected event occured, if we have a handler/mitigation for an exception then it is exception handler
# exception handler blocks (try, except, else, finally)
#Types of Exception: Predefined (TypeError, ValueError, KeyError, FileNotFound, OutOfMemory, ArithmeticException, ZeroDivisionError...)
# & Userdefined/CustomExceptions (Our own Classes also we can create to handle some specific exceptions)
#What? unexpected event occured
#Reallife Example:
#1. try - I am going to a store to buy something and come back to my home (Try my level best by planning to achieve it)
    #take a vehicle (check whether enough air)
    # go to shop, (look for the timing)
    # add different items in the cart (check expiry date, then add)
    # pay the bill,
    # take a vehicle
    # come back home
#2. except -
    #exception1 - trip got cancelled because of some other priority work came
    #exception2 - vehicle is not starting, but i may use some other vehicle or go by walk or call the mechanic and abort my journey
    #exception3 - shop is closed
    #exception4 - some products are not available...
    #exp5- card declined/not accepted or wallet is lost
    #exp6 - vehicle is not starting
    #exp7 - something went wrong which i didn't predicted (expect unexpected)
#3. else - (If except doesn't happened) If I am not getting any exception, what I have to do then?
    #ensure to clean, lock your vehicle when you leave the vehicle in the home
#4. finally (If 1+3 or 1+2  happened) If I am not getting any exception or I got some exception, what I have to do?
    #ensure to clean, lock your vehicle when you leave the vehicle in the home
    #plan for some other alternative journey

#What are mandatory blocks:
#try with either except or with finally is mandatory (eg. try except or try finally or try except else finally or try except else)

print("1. Fundamendals of Exception Handling")
print("a. Exception handling blocks in python- minimum fundamental blocks (try & except first then with else and finally also added) ")
#Below try, except and else - help us understand what if everything went fine or if exeption occured?
#if all are good, then send mail to the user, if anything fails handle in the exception block..
#How often we use try except in real time sir ?
#Minimum we have write all our code with the try and except block minimum as per the below example...
try:
    print("line1 code"+10)
    print(100/0)
except Exception:
    print("handler program")


import shutil
import os
try:
    print("process1: let us do some cleanup")
    shutil.rmtree("/home/hduser/somedir1")
    print("Directory is removed")
    print("other lines of code...")
except FileNotFoundError as errmsg:
    print(f"FileNotFoundError occured, pls check the dir/file exist :{errmsg}")
except Exception as errmsg:
    print(f"Something went wrong :{errmsg}")
else:
    print("MAIL: cleanup is completed")

#Below try, except and else - help us understand what if everything went fine or if exeption occured?
#if all are good, then send mail to the user, if anything fails handle in the exception block and finally cleanup the tmp directory..
try:
    print("process2: let us process some file and purge the directory after processing")
    import json
    import os
    import shutil
    if os.path.exists("/home/hduser/somedir1/metadata.json"):#gracefully avoid exceptions
        file1 = open("/home/hduser/somedir1/metadata.json", 'r')
        json_parsed = json.load(file1)
        process = json_parsed['process']
        print(f"process name is {process}")
    else:
        #pass
        print("log: file not exist for the given run of the program, run this program later")
        print("though json parsing is not done, but i will continue other part of this program")

except FileNotFoundError as errmsg:
    print(f"email: FileNotFoundError occured, pls check the dir/file exist :{errmsg}")
except Exception as errmsg:
    print(f"Something went wrong :{errmsg}")
else:
    print("mail: dataprocessing in completed")
    print("archiving the processed file")
    shutil.move("/home/hduser/somedir1/metadata.json","/home/hduser/somedir1/archive")
finally:
    print("whether while reading the file exception occured or completed successfully, "
          "I am going to do some temp cleanup")
    shutil.rmtree("/home/hduser/tmp/")


print("b. Types of exception handling - Predefined exception - "
      "When we anticipate the possible exception may happen which is already defined by python")
try:
    course_lst=['DS','DE','DEO','CLO']
    usrinput=int(input("enter the desired program to learn 0 for DS, 1 for DE, 2 for DEO,3 for CLO\n"))
    #assert usrinput in (0,1,2,3);#help us do validation
    if course_lst[usrinput]:
        print(f"we have the availability of the given course {course_lst[usrinput]}")
    else:
        print("no such course available")
    a=10
    den=int(input("provide the denominator number\n"))
    b=a/den
    print(b)

except AssertionError:
    print(f"assertion error occured, because the input is not as expected")
except IndexError:
    course_lst = ['DS', 'DE', 'DEO', 'CLO']
    print(f"input is not within the given Index range, max supported is {len(course_lst)-1}")
except ValueError:
    print(f"provide only numbers, not string or other type")
except NameError:
    print(f"some variable is not defined, but used")
except ZeroDivisionError:
    print(f"zero division error")
except Exception as errmsg:
    print(f"some exeception occured with an error message of : {errmsg}")


print("c. Types of exception handling - "
      "Userdefined/custom exception - "
      "If python doesn't provided some exception which we wanted to create and use ")
class InceptezCustomError(Exception):#inheritance
    print("custom exception occured, because of some particular business reason")
    import shutil
    shutil.rmtree("/home/hduser/tmp/")

try:
    course_lst=['DS','DE','DEO','CLO']
    usrinput=int(input("enter the desired program to learn 0 for DS, 1 for DE, 2 for DEO,3 for CLO\n"))
    if  usrinput not in (0,1,2,3):
        raise InceptezCustomError
    else:
        print("continue the program further...")
    print("further line of code")
except InceptezCustomError:
    print("customer exception occured, raised due to wrong option chosen")

#Example2 to address Chetan and Saranya's question, we learn about the class, methods, importing, etc., subsequently...
class NegativeError(Exception):
    def __init__(self):#dont bother about this line, we learn it later
        print("exception handler class executed")
#Chetan - why the print is happening when u define a class - i dont wanted to talk about the class code
#Saranya - Without instantiating, how do we execute the class - We are not executing the class, rather we are raising the class
try:
    sal=int(input())
    penality=int(input())
    finalsal=sal+penality
    if finalsal<0:
        raise NegativeError()
    else:
        print("salary after deduction of penality",finalsal)
except NegativeError:
    print("Final salary cannot be negative for a given month")

print("d. Two ways of handling exception code - Block level and statement level")
# Block level exception handling program -
# we can keep all lines of code in a single block (if any one line fails, rest of lines will not run)
try:
    print("line1 code" + '10')  # line1 (statement1)
    print("line2 depends on line1", 100 / 1)  # line2 (statement2)
    print("line3 depends on line1 and line2: one more lines of code")  # (statement3)
except Exception:
    print("handler program")

# Statement level exception handling program -
# we can keep all lines of code in a single block (if any one line fails, rest of lines will not run)
try:  # try for statement1
    print("line1 code" + 10)  # line1 (statement1)
except Exception:
    print("handler program")

try:  # try for statement2
    print("line2 independent of line1", 100 / 1)  # line2 (statement2)
except Exception:
    print("handler program")

try:  # try for statement3
    print("line3 independent of line1 and line2: one more lines of code")  # (statement3)
except Exception:
    print("handler program")