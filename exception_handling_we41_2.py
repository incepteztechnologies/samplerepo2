#EXCEPTION HANDLING
#importance - Dataengineer less (already framework spark handled the exceptions)
#importance - python developer (application) medium (already framework spark handled the exceptions)
# Exception is a error occurrs when the program is executing at any stage for any
# reasons (data error, name/key/value error, type error, environment error, file not found, format error)
# and makes the flow of program terminated abruptly
# Exception Handler (graceful handling of program termination)
# help us handle or take the control from the abrupt termination of the program - is a construct/code that help us handle the state of exception
#Example:
#exception->exceptional cases, unexpected events, unusual..
#1. I am going to a store to buy something to my home (plan it perfectly to avoid any unexpected events)
    #take a vehicle, go to shop, add different items in the cart, pay the bill, come back home
#2. any unexpected event occurs, handle it accordingly
    #exception1 - trip got cancelled because of some other priority work came
    #exception2 - vehicle is not starting, but i may use some other vehicle or go by walk or abort my journey
    #exception3 - shop is closed
    #exception4 - some products are not available...
    #exp5- card declined/not accepted or wallet is lost
    #exp6 - vehicle is not starting
    #exp7 - something went wrong which i didn't predicted (expect unexpected)
#3. (If 2 doesn't happened) If I am not getting any exception, what I have to do then?
    #ensure to clean, lock your vehicle when you leave the vehicle in the home
#4. (If 1 or 2  happened) If I am not getting any exception or I got some exception, what I have to do?
    #ensure to clean, lock your vehicle when you leave the vehicle in the home
    #plan for some other alternative journey
#1 and 2 are mandatory
#3 and 4 are not mandatory

#4 block of exception handler in python try,except,else,finally
'''shopname=int(input("enter the shop number"))#program aborted without any handler
print(shopname)
print("go to the shop...")
list_of_products_in_the_shop={"pencil":2,"oil":100}
list_to_purchase=["pencil","oil","fanta"]
shopping_cart=[]
for prod in list_to_purchase:
   shopping_cart.append(list_of_products_in_the_shop[prod])
   print(f"amout to pay finally {sum(shopping_cart)}")'''

try:
    shopname=int(input("enter the shop number"))#program aborted without any handler
    #list_to_purchase=input()
    print(shopname)
    print("go to the shop...")
    list_of_products_in_the_shop={"pencil":2,"oil":100,"notes":50}
    list_to_purchase=["pencil","oil","fanta"]
    shopping_cart=[]
    #print(f"identify only the products in the shop and complete your purchase")
    #set(list_of_products_in_the_shop.keys()).intersection(set(list_to_purchase))
    for prod in list_to_purchase:
       shopping_cart.append(list_of_products_in_the_shop[prod])
    totalamt=sum(shopping_cart)
    promo=10
    finalamt=totalamt-promo
    print(f"amout to pay finally {finalamt}")

except ArithmeticError as msg:
    print(f"enter the shop number as a whole number like 10 or 20 or 30 {msg}")

'''except ValueError as msg:
    #print(f"some exception occured ")
    print(f"enter the shop number as a whole number like 10 or 20 or 30 {msg}")
except KeyError as msg:
    #print(f"some exception occured ")
    print(f"Some of the products is not there in the shop, hence aborting my purchase {msg}")
except Exception as msg:
    print(f"some exception occured {msg}")'''


    #exit(1)