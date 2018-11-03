# this file is for getting practice with errors and exception handling.

#1. handle the exception thrown the following code. using try and except blocks
 #   for i in ['a', 'b', 'c']:
    #    print(i ** 2)          --> generates a TypeError
def hmwk1():

    try:
        for i in ['a', 'b', 'c']:
            print(i**2);
    except:
        print("Exception was thrown in hmwk1() function");


#2. handle the exception thrown by the code below by using try and except blocks.  then use a finallay block to print 'All Done'

#        x = 5
#        y = 0
#        z = x/y  --> generates a ZeroDivision Error
def hmwk2():
    x = 5;
    y = 0;
    z = 0;
    try:
        z = x/y;
    except ZeroDivisionError:
        print("Exception caught in hmwk2() function --  hey Jackass you can't divide by Zero!!")



#3. write a function that asks for an integer and prints the square of it.  use a while loop with a try, except, else block to account for incorrect inputs.
def hmwk3():
    while(True):

        try:
            user_input = int(input("please input an integer: "))
            squared_input = user_input**2
            print("the square of your input is {}".format(squared_input))
        except:
            print("I told you enter an integer.  try again.")
        else:
            break;






####   main script body #####
hmwk1()
hmwk2()
hmwk3()
