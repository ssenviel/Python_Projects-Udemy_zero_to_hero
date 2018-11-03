#  this file is for playing around with File I/O in Python.
READ_ONLY='r'
WRITE_ONLY='w'
APPEND='a'
READ_WRITE='r+'
READ_OVERWRRITE='w+'

#1.  open a file and print the contents, line by line
#fileHndl = open("Basic.txt", READ_ONLY);

#print(fileHndl.read() );

#fileHndl.close();

# lesson learned:  the cursor is not by line it is by character


myFile = open("myFile.txt", READ_WRITE);
#print(myFile.read());
myFile.seek(100);  # reset the cursor
#myFileContets = myFile.readlines();
#print(myFileContets);
myFile.write('\nThis is the 7th line');
myFile.close();



#2.  open a file and print every other line

#3  open a file and write to it

#4 open a file and append to it

# use the with open <file name> as <file object>  construct