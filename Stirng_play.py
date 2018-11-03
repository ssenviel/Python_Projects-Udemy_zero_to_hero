# this is a file for playing with string slicing

myString = "Python"

print("myString is ", type(myString));

print(myString[:3]);

pos=myString.index("thon");
print(pos);

print(myString[::-1]);
print(myString[::-2]);


# TODO:  use the .format() method and floating point formattting.

name="Slim Shady";
sound_fx="ficka-ficka";

print("Hi! name is... \n"*3);
print("{} {}\n\n\n".format(sound_fx, name));


value = 100/77;

print("value is {v:10}".format(v=value));

print("left aligned value is {v:<10.5f}".format(v=value));

print("right aligned value is {v:>10.5f}".format(v=value));


# mytup = tuple(1, 2, 4, 6, 8);

testSet = set([1, 1, 2, 3, 4]);
print(testSet);
