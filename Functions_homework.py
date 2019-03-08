# write a function that computes the volume of a sphere with a given radius
  # NOTE:  the volume of a sphere is 4/3* pi * Radius^3
        # NOTE:  need to make sure that 4/3 is returning a float
import math


def cube_volume(radius):
    return ( float(4.0/3) * math.pi *radius**3 );



# write a number that checks wether a number is within a given range (inclusive of high and low)
def ran_bool(num, high, low):
    return ( num in range(low, high));


# write a function that accepts a string and calculate the number of upper case and lower case letters
def num_cases(inputString):
    numUppers=0
    numLowers=0

    for letter in inputString:
        if letter.isupper():
            numUppers+=1;
        else:
            numLowers+=1;

    print(f"No. of Upper case characters : {numUppers}");
    print(f"No. of Lower case characters : {numLowers}");



# write a function that takes a list and creates a new list that of unique elements of the first list
 # I.E.  convert a list to a set
def unique_list(inputList):
    mySet = set();
    for item in inputList:
        mySet.add(item)
    return( list(mySet));


# write a function to multiply all the numbers in a List
def multiply(numbers):

    multiple=1;
    for num in numbers:
        multiple*=num;

    return multiple;


#write a function that checks wether a passes string is a palindrome or not
def is_plaendrome(inputString):
    tempStr = inputString[::-1];
    if(inputString == tempStr):
        return True
    else:
        print(f"{inputString} is a not palindrome")
        return False;




