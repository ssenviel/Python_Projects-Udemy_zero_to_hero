# write a function that returns the lesser or two given numbers if both numbers are even, but returns the greater if one or both numbers are odd.

def lesser_of_two_evens(a, b):
    if (0 ==a%2 and 0 == b%2 ):
        return min(a, b);
    else:
        return max(a, b);

##num1=10;
##num2=20;
##print(f"lesser_of_two_evens({num1}, {num2}) is {lesser_of_two_evens(num1, num2)}")
##
##
##num1=5;
##num2=20;
##print(f"lesser_of_two_evens({num1}, {num2}) is {lesser_of_two_evens(num1, num2)}")
##
##num1=20;
##num2=21;
##print(f"lesser_of_two_evens({num1}, {num2}) is {lesser_of_two_evens(num1, num2)}")

##num1=22;
##num2=20;
##print(f"lesser_of_two_evens({num1}, {num2}) is {lesser_of_two_evens(num1, num2)}")

# write a function that takes a two-word string and returns True if both works begin with the same letter
def animal_crackers(word):
    print(f"the input is {word}");
    # 1. check that the input is a word
    wordList = word.split();

    if( (2 == len(wordList)) and (wordList[0].isalpha and wordList[1].isalpha) and (wordList[0][0] == wordList[1][0]) ):
        return True;
    else:
        return False;

# sanity check
#print(f"{animal_crackers('Levelheaded Llama')}");
#print(f"{animal_crackers('Crazy Kangaroo')}");
#print(f"{animal_crackers('Crazy cat')}");


#animal_crackers('Levelheaded Llama');


# Given two integers, return True if the sum of the integers is 20 or if one the integers is 20. if not return false.
def makes_twenty(num1, num2):
    if(20 == num1 or 20 == num2):
        return True;
    elif( (num1+num2) == 20):
        return True;
    else:
        return False;

def makes_twenty_oneliner(num1, num2):
    return (20==num1 or 20==num2 or 20 == (num1+num2));

#sanity check
#testnum1=100;
#testnum2=80;
#
#print(f"makes_twenty({testnum1} {testnum2})  returns {makes_twenty(testnum1, testnum2)})")
#print(f"makes_twenty_oneliner({testnum1} {testnum2})  returns {makes_twenty_oneliner(testnum1, testnum2)})")



# Level 1 exercise#1: write a function that capitalizes the first and fourth letters of a name
# NOTE: capitalize() method will return the string with the first letter in caps
def old_macdonald(name):
    # 1. capitalize the first letter by using the capitalize method
    # 2. use string slicing to create a new string that will contain string[0:3]+string[3].upper + string[4::]
    # 2.1 option2 -- use string slicing to create a new string from string[0:3] + string[3:]

    Str1='temp'
    tempStr = name.capitalize()
#    return (tempStr[0:3]+tempStr[3].upper()+tempStr[4:]);  # option 1
    return (name[0:3].capitalize() + name[3:].capitalize()) # option 2 -- less lines than option 1

# sanity check 1.1
#testStr='JerseyBoy'
#print(f"old_mac({testStr}) yields {old_macdonald(testStr)}")


#Level 1 exercise #2: given a sentence , return a sentence with the words reversed
  #option 1 -- split the string and use the for loop to regenerate the string
    # lesson learned.  how to use the combination of Range to count down, and join() to convert a list to a string with a delimiter
  #option 2 -- use List comprehension
  #option 3 -- split the list and then use reverse slicing to generate the reverse list and then use join() to create the string
    # lesson learned:
#          reverse slicing on a string will result in a new string that is the reverse of the string.
#         reverse slicing on a list will create a list where the contents of the indexes are reversed.
def master_yoda(text):
    wordList = text.split(' ');
    yodaWordList = [];
    for wordIdx in range(len(wordList)-1, -1, -1):
        yodaWordList.append(wordList[wordIdx]);

    return ' '.join(yodaWordList);    # note:  the space (' ')  is the delimiter for this string

def master_yoda3(text):
    wordList = text.split(' ');
    yodaWordList = wordList[::-1];
    return ' '.join(yodaWordList);    # note:  the space (' ')  is the delimiter for this string

#sanity check 1.2
#testString1 = 'I am home';
#testString2 = 'We are ready'
#print(f"master_Yoda({testString1}) Yields {master_yoda(testString1)}");
#print(f"master_Yoda({testString2}) Yields {master_yoda(testString2)}");
#
#print(f"master_Yoda3({testString1}) Yields {master_yoda3(testString1)}");
#print(f"master_Yoda3({testString2}) Yields {master_yoda3(testString2)}");


# Level exercise #3: given an integer 'n', return True if 'n' is within 10 of either 100 or 200
 # option1 use the absolute value function to find the distance.
def almost_there(n):
    return ( (abs(100-n)<=10)  or (abs(200-n) <=10)  )


#sanity check 1.3
#testnum1=90;
#testnum2=104;
#testnum3=150;
#testnum4=209;
#testnum5=189;
#print(f"almost there({testnum1}) gives back {almost_there(testnum1)})");
#print(f"almost there({testnum2}) gives back {almost_there(testnum2)})");
#print(f"almost there({testnum3}) gives back {almost_there(testnum3)})");
#print(f"almost there({testnum4}) gives back {almost_there(testnum4)})");
#print(f"almost there({testnum5}) gives back {almost_there(testnum5)})");


#Level 2 exercise 1:
# given a list of ints, return True if the array contians a 3 next to a 3 somewhere  -- i.e consecutive 3's
# option 1 - cycle through the list and use a counter to determine the True condition
# option 2 - use a for loop that will cycle through all the indexes and if we find a condition where list[i]==3 and list[i+1] = 3 then return True.

    # lesson learned

def has33(nums):
    counter=0;
    for num in nums:
        if(3 ==num and 0==counter):
            counter=1;
        elif(3 == num and 1==counter):
            return True
        elif(3!= num):
            counter=0;

    return False;

def has33_2(nums):
    for i in range(0, len(nums)-1):
        if(3 == nums[i] and 3 == nums[i+1]):
            return True;

    return False;



# sanity check 2.1
#testList1 = [1, 3, 3];
#testList2 = [1, 3, 1, 3];
#testList3 = [3, 1, 3];
#
#print(f"testList1 = {testList1} ,  has33 gives back {has33(testList1)}");
#print(f"testList3 = {testList2} ,  has33 gives back {has33(testList2)}");
#print(f"testList3 = {testList3} ,  has33 gives back {has33(testList3)}");
#
#print(f"testList1 = {testList1} ,  has33_2 gives back {has33_2(testList1)}");
#print(f"testList3 = {testList2} ,  has33_2 gives back {has33_2(testList2)}");
#print(f"testList3 = {testList3} ,  has33_2 gives back {has33_2(testList3)}");


# Level 2 exercise 2 -- Paper Doll : Given a String , return a string where for every character in the original there are 3 characters
# cycle through each char in the string and duplicate each character *3 then rebuild the string --
    # lesson learned: Strings can be concatenated but not overwritten.   cannot index into a string to modify it
def paper_doll(inputStr):
    myArray=''
    for char in inputStr:
        myArray+= char*3;

    return ''.join(myArray);

# sanity check 2.2

#testString1='Hello';
#testString2 ='Mississippi'
#print(f"paper_doll( {testString1} ) gives back  {paper_doll(testString1) } ");
#print(f"paper_doll( {testString2} ) gives back  {paper_doll(testString2) } ");



# Level 2 exercise 3 -- BlackJack: Given three Integers between 1 and 11, if their sum is less than or equal to 21, return their sum.
#                                  if Their sum exceeds 21 and there is an eleven, reduce the total sum by 10.
#                                  Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'
def blackjack(a, b, c):
    hand = sum([a, b, c]);
    if(hand <=21):
        return hand;
    elif( hand >21 and (11==a or 11==b or 11==c) ):
        if(11==a ):
            hand-=10
        if(11==b):
            hand-=10
        if(11 == c):
            hand-=10

        if(hand<=21):
            return hand;
        else:
            return 'BUST';

    else:
        return 'BUST';


# sanity check 2.3

def testBlackJack(testhand):
    print(f"blackjack {testhand} gives back {blackjack(testhand[0], testhand[1], testhand[2])}");

#testhand1=(5, 6, 7)
#testhand2=(9, 9, 9)
#testhand3=(9,9, 11)
#testhand4=(11, 11, 11)
#
#testBlackJack(testhand1);
#testBlackJack(testhand2);
#testBlackJack(testhand3);
#testBlackJack(testhand4);


# NOTE:  should ask a question about the solution to this, in the event of more than 11 does the instructor solution still work


#Level2 exercise 4 -- summer of '69: return the sum of the numbers in the array except ignore sections of numbers starting with a 6 and ertending to the next 9
#    (every 6 will be followed by at least one 9).  return 0 for no numbers.
def summer_69(arr):
    found_six=False;
    sum=0;
    for element in arr:
        if(False == found_six and 6 !=element ):
            sum+=element;
        elif(element == 6):
            found_six = True;
            continue;
        elif(True == found_six and 9 == element ):
            found_six= False;
        else:
            continue

    return sum;

# instructor solution uses a 2 while-loops within a for-loop that  accomplishes the same logic


#sanity check
#testArray1 = [1, 3, 5]
#testArray2 = [4, 5, 6, 7, 8, 9]
#testArray3 = [2, 1, 6, 9, 11]
#print(f"summer_69 {testArray1} gives back {summer_69(testArray1)}")
#print(f"summer_69 {testArray2} gives back {summer_69(testArray2)}")
#print(f"summer_69 {testArray3} gives back {summer_69(testArray3)}")


# Start of the Challenging function problems

# SPY GAME: Write a function that takes a list of integers and returns True if it contains 007 in order

# cycle through the list , looking for the sequence 007

# instructor solution uses and array with [0, 0, 7, 'x'] and when the digit is found it pops() an element off.
# if the length of the array is one then it returns True
def spy_game(inputList):

    zeroCount=0;
    for item in inputList:
        if(zeroCount >=2 and 7 ==item):
            return True;

        elif(0 == item):
            zeroCount+=1;

        else:
            continue;

    return False;


#gameInput1=[1, 2, 4, 0, 0, 7, 5];
#gameInput2=[1, 0, 2, 4, 0, 5, 7];
#gameInput3=[1, 7, 2, 0, 4, 5, 0];
#
#print(f"spygame {gameInput1} gives back {spy_game(gameInput1)} ");
#print(f"spygame {gameInput2} gives back {spy_game(gameInput2)} ");
#print(f"spygame {gameInput3} gives back {spy_game(gameInput3)} ");



# COUNT PRIMES:  write a function that returns the number of prime numbers that exist up to and including an given number
   # by convention treat 0 and 1 as not prime.
#    NOTE:  a prime number is a number that is only evenly divisable by 1 and itself

def count_primes(num):
    primeCount=0;
    for i in range(2, num+1):
        startCheck=2;
       # print(f"checking {i}")
        if (i==2 or i==3):
            print("\t\t\t{} is prime".format(i));
            primeCount+=1;
            continue;
        else:  # check if this number is prime
            isPrime= True;

        while startCheck < i:
         #   print(f"checking {i} vs {startCheck}");
            if( i%startCheck ==0):
                isPrime=False;
                break;
            else:
                startCheck+=1;

        if(isPrime):
            print("\t\t\t{} is prime".format(i));
            primeCount+=1;


    return primeCount;



#sanity check
myNum=100;

print(f"count_primes ({myNum}) gives back {count_primes(myNum)}");




