# this file is for playing around with classes in python
import math



# udemy course homework assignments:
#
#1.  fill in the line class methods to accept coordinates as a pair of tuples and return the slope
    # and distance of the line

class Line:

    def __init__(self, coor1, coor2):
        if( len(coor1) !=2 or len(coor2) !=2 ) :
            print("ERROR -- invalid coordinates provided")
            exit(-1)

        self.coordinate1 = coor1;
        self.coordinate2 = coor2;
        self.deltaX = abs(self.coordinate1[0] - self.coordinate2[0])
        self.deltaY = abs(self.coordinate1[1] - self.coordinate2[1]);


        #  can use the pathagorean theorm.   a^2 + b^2 = c^2,  a = delta-X, b = delta-Y
    def distance(self):
        dist = math.sqrt( self.deltaX**2 + self.deltaY**2 )  ;
        return dist;

       # m = (y2-y1) / (x2-x1)a
    def slope(self):
        return float(self.deltaY / self.deltaX)



class Cylinder:

    def __init__(self, height=1, radius=1):
        self.height = height;
        self.radius = radius;
        print("\ncreating cylinder with height = {}  , radius= {} ".format(self.height, self.radius));


        # volume = pi * Radius^2 * Height
    def volume(self):
        vol= math.pi * self.radius**2 * self.height;
        return vol;

     # 2* Pi * Radius ^2  +  2*Pi* Raduis* Height
    def surface_area(self):
        surf_area = (2* math.pi * self.radius**2) + (2 * math.pi * self.radius * self.height)
        return surf_area;


def test_Line():
    print("testing the line class implementation");

    coordinate1 = (3, 2)
    coordinate2 = (8, 10)

    myLine = Line(coordinate1, coordinate2);
    print("coordinate_1 is {}".format(coordinate1))
    print("coordinate_2 is {}".format(coordinate2))
    print("distance of the line is {}".format(myLine.distance()) );
    print("slope of the line is {}".format(myLine.slope() ) );


def test_Cylinder():
    myCylinder = Cylinder(2, 3);
    print("Volume of the cylinder is {}".format(myCylinder.volume()))
    print("Surface area of the cylinder is {}".format(myCylinder.surface_area()))





# 2.  OOP challenge:
# 2.1 create a bank account class that has 2 attributes, owner and balance, and two methods, deposit and withdraw.
#   NOTE:  withdraws cannot exceed the available balance.
#2.2  use create a majic/Dunder method for print that will print the account owner and the account balance. if the banks account object is used in it
  # print(accnt1) -- this requires overriding the str built-in
        # Account owner: <owner>
        # Account balance: <balance>
#2.3  deposits and withdrawls should print an acknowledgement that the operation was sucessful.
   # i.e.  "Deposit Accepted"  "withdrawl accepted".

def test_Bank_Account():
    user1 = BankAccount("User_1");
    user2 = BankAccount("User_2", 100);
    print(user1)
    print(user2)

    user1.withdraw(10);
    user2.deposit(-40);

    user1.deposit(30)
    user2.withdraw(81);
    print(user1);
    print(user2);

class BankAccount():

    def __init__(self, owner, initial_balance=0):
        self.owner = owner;
        self.balance = initial_balance;

    def deposit(self, amount):
        if(amount <= 0):
            print("{} Deposit Denied: requested amount to deposit, {} , is not a valid amount\n".format(self.owner, amount))
        else:
            self.balance += amount;
            print("{} Deposit Accepted\n".format(self.owner));

    def withdraw(self, amount):

        if(amount > self.balance):
            print("{} Withdrawal Denied: amount requested, {} , is greater than available balance of {}.".format(self.owner, amount, self.balance))
        else:
            self.balance -= amount;
            print("{} Withdrawal Accepted\n".format(self.owner));

    def __str__(self):
        return "Account Owner : {} \nAccount Balance: {}\n".format(self.owner, self.balance)

# main execution
#test_Line();
#test_Cylinder();
test_Bank_Account()