"""
    problem 1:
        create a Generator that generates the squares of numbers up to some number 'N'    
    problem 2:
        create a generator that yields "n" random number between a low and high number
        NOTE: use random.randrange or random.randint 
    problem 3: 
        use the iter() function to convert the string 'hello'  into an iterator.




"""
import random


def square_generator(N):

    i=0
    while i < N:
        yield i**2
        i += 1
    
def random_generator(N, start, stop):
    """
    NOTE: need to figure out how to get unique random numbers
    """    
    i=0
    while i < N:
        yield random.randrange(start, stop)
        i += 1
        
def convert_str_to_iter():
    my_string = 'hello'
    my_str_iter = iter(my_string)
    for char in range(0, len(my_string)):
        print(next(my_str_iter))
        
        
convert_str_to_iter()

        
        
