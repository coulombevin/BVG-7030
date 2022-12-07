#Python Indentation

if 5 > 2:
    print("Five is greater than two!")

#Numbers
x = 3+5j
y = 5
z = -5.877

print(type(x))
print(type(y))
print(type(z))

#Specify a variable type

x = int(1)	# x will be 1
y = float(2.8) # y will be 2.8
z = str("s1") # z will be 's1'

#How to declare and use a variable
a = 100
print(a)

#redeclare a variable
# Declare a variable and initialize it
f = 0
print(f)
# re-declaring the variable works
f = 'dav'
print(f)

#Concatenate variables
a = "DT"
b = 99
print(a+str(b))

#Local and global variables
# Declare a variable and initialize it
f = 101
print(f)
# Global vs. local variables in functions
def someFunction():
    # global f
    f = 'I am learning Python'
    print(f)
someFunction()
print(f)

f = 101;
print(f)
# Global vs.local variables in functions
def someFunction():
    global f
print(f)
f = "changing global variable"
someFunction()
print(f)

#Delete a variable
f = 11;
print(f)
del f
#print(f) return an error

#String

a = "Hello, World!"
print(a[1])
b = "Hello, World!"
print(b[2:5])
a = " Hello, World! "
print(a.strip())
print(len(a))

#Python operators
num1 = 4
num2 = 5
res = num1 + num2
res += num1
print(("Line 1 - Result of + is ", res))

#Python comparison operators
x = 4
y = 5
print(('x > y is',x>y))

#Python logical operators
a = True
b = False
print(('a and b is',a and b))
print(('a or b is',a or b))
print(('not a is',not a))

#Python identity operators
x = 20
y = 20
if ( x is y ):
    print("x & y SAME identity")
y=30
if ( x is not y ):
    print("x & y have DIFFERENT identity")

#Python membership operators
x = 4
y = 8
list = [1, 2, 3, 4, 5 ];
if ( x in list ):
    print("Line 1 - x is available in the given list")
else:
    print("Line 1 - x is not available in the given list")
if ( y not in list ):
    print("Line 2 - y is not available in the given list")
else:
    print("Line 2 - y is available in the given list")

#Python List
thislist = ["apple", "banana", "cherry"]
print(thislist)
#access
thislist = ["apple", "banana", "cherry"]
print(thislist[1])
#change
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)
#Loop
thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)
#Check if exist
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
    print("Yes, 'apple' is in the fruits list")
#Add item
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)
#remove item
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.pop() #specific or last
print(thislist)

thislist = ["apple", "banana", "cherry"]
del thislist[0] #sepecific
print(thislist)

thislist = ["apple", "banana", "cherry"]
del thislist #delete all
#print(thislist) #this will cause an error because "thislist" no longer exists.

thislist = ["apple", "banana", "cherry"]
thislist.clear() #empty
print(thislist)

#Constructor
#thislist = list(("apple","banana","cherry"))
# note the double round- brackets
print(thislist)

#Tuple
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])
thistuple = ("apple", "banana", "cherry") 

#thistuple[1] = "blackcurrant" #Error cant change value
# The values will remain the same: 
print(thistuple)

#set
thisset = {"apple", "banana", "cherry"}
print(thisset)
#Access items
thisset = {"apple", "banana", "cherry"}
for x in thisset:
    print(x)
#Change item
    #You cant

#Add items
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)
#remove
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)

thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)

thisset = {"apple", "banana", "cherry"}
del thisset
#print(thisset) #Error thisset does not exist

#Dictionary
thisdict = { "brand": "Ford",
             "model": "Mustang",
             "year": 1964
             }
print(thisdict)

#Access
x = thisdict["model"]
x = thisdict.get("model")

#Change value
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018
#Add
thisdict = { "brand": "Ford",
             "model": "Mustang",
             "year": 1964
             }
thisdict["color"] = "red"
print(thisdict)
#Remove
thisdict = { "brand": "Ford",
             "model": "Mustang",
             "year": 1964
             }
thisdict.pop("model")
print(thisdict)

thisdict = { "brand": "Ford",
"model": "Mustang", "year": 1964
}
thisdict.popitem()
print(thisdict)

thisdict = { "brand": "Ford",
"model": "Mustang", "year": 1964
}
del thisdict["model"]
print(thisdict)

thisdict = { "brand": "Ford","model": "Mustang", "year": 1964
}
del thisdict
#print(thisdict) #this will cause an error because "thisdict" no longer exists.

thisdict = { "brand": "Ford",
"model": "Mustang", "year": 1964
}
thisdict.clear()
print(thisdict)


#If else
a = 200
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")

#While loops
i = 1
while i < 6:
    print(i)
    i += 1

i = 1

#break
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

#Continue
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

#For loops
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

for x in "banana":
    print(x)

#Break
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break

#Continue
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)

#Range
for x in range(6):
    print(x)

#Else
for x in range(6):
    print(x)
else:
    print("Finally finished!")

#Nested loops (For in a For)
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x, y)


#Recursion (ATTENTION CAN BECOME UNFINISHING LOOP)
def tri_recursion(k):
    if(k>0):
        result = k+tri_recursion(k-1)
        print(result)
    else:
        result = 0
    return result

print("\n\nRecursion Example Results")
tri_recursion(6)


#Function
def my_function():
    print("Hello from a function")

#Calling
def my_function():
    print("Hello from a function")

my_function()

#Parameters
def my_function(fname):
    print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

#Default parameters
def my_function(country = "Norway"):
    print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

#Return
def my_function(x):
    return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))

#Classes
class MyClass:
    x = 5

#Create object
p1 = MyClass()
print(p1.x)

#__init__ function
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)

#Object methods
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()


#self parameter
class Person:
    def __init__(mysillyobject, name, age):
        mysillyobject.name = name
        mysillyobject.age = age
    def myfunc(abc):
        print("Hello my name is " + abc.name)
p1 = Person("John", 36)
p1.myfunc()
#Modify propertie
p1.age = 40
#Delete propertie
del p1.age
#Delete object
del p1

#File handling
#f = open("demofile.txt")#error does not exist
    #or we can use r to read t to text
#f = open("demofile.txt", "rt")#error does not exist

# Create a file called "myfile.txt":
#f = open("demofile.txt", "x") #error file already exist
# Create a new file if it does not exist:
f = open("demofile.txt", "w")
f = open("demofile.txt", "r")
print(f.read())

#writing
# Open the file "demofile.txt" and append content to the file:
f = open("demofile.txt", "a")
f.write("""Hello! Welcome to demofile.txt This file is 
for testing purposes. 
Good Luck!""")
f = open("demofile.txt", "r")
print(f.read())

#Read part
f = open("demofile.txt", "r")
print(f.read(5))
#Read line
f = open("demofile.txt", "r")
print(f.readline())
# Read two lines of the file:
f = open("demofile.txt", "r")
print(f.readline())
print(f.readline())
# Loop through the file line by line:
f = open("demofile.txt", "r")
for x in f:
    print(x)

# Open the file "demofile.txt" and overwrite the content:
f = open("demofile.txt", "w")
f.write("Woops! I have deleted the content!")
# the "w" method will overwrite the entire file.
f = open("demofile.txt", "r")
print(f.read())

#Delete file
# Remove the file "demofile.txt":
import os
os.remove("demofile.txt")

#Check if file exist
# Check if file exist, then delete it:
import os
if os.path.exists("demofile.txt"):
    os.remove("demofile.txt")
else:
    print("The file does not exist")

#Delete folder
# Remove the folder "myfolder":
import os
os.rmdir("myfolder")

#BIOPYTHON

#see version
import Bio
print(Bio.__version__)

from Bio.Seq import Seq
from Bio.Alphabet import generic_dna
my_dna = Seq("AGTACACTGGT", generic_dna)
print(my_dna)
print(my_dna.complement())
print(my_dna.reverse_complement())
print(my_dna.transcribe())

