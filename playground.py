print ("Practicing Basic Program")

print("Hello Word")

# Display a message
# Get user input and display a message.
myname = input("What is your name: ")
print("Hello " + str(myname))

# Alternative way to format a string
print("Hello %s" % myname)

print("Done practicing Basic Program\n\n")


print("Practicing Variables")

i = 139
print(f"Variable i has the value {i}")

f = 58.7484
print(f"Variable f has the value {f} and its type is {type(f)}")

b = True
print(f"Variable b has the value {b}")

n = None
print(f"Variable n has the value of {n}")

# tuple
c = (20,40,20)
print(f" c[0] has the value {c[0]} and is of type: {type(c)}")

# list
l = ["Salman", "Rick", "Shivam"]
l = [10,20,30]
print(f" l[0] has the value {l[0]} and is of type: {type(l)}")

# Sets variables.
s = set()
s.add(1)
s.add(4)
s.add(6)
print(s)

# Dictionary
grades = {"Salman" : "A", "Rick": "B-"}
grades["Salman"]
grades["Rick"] = "F"


# Create an empty dictionary .
mydictionary = dict()

print("Done practicing Variables\n\n")


print("Practicing Conditionals")
x = 10
if (x > 0):
    print("The number is positive")
elif (x < 0):
    print ("The number x is negative")
else:
    print ("The number x is zero")

print ("Done practicing Conditionals\n\n")

print("Practicing Loops")
for i in range(5):
    print(i)
for i_idx, i_value in enumerate(range(2,10)):
    print(f"{i_idx} - {i_value}")


print ("done practicing loops\n\n")

print ("practicing functions")

def is_even(x):
    if (x % 2) == 0:
        return True
    else:
        return False

print("done practicing functions\n\n")


print("practicing classes")
class Book:
    def __init__(self, title="Software Engineering", isbn=""):
        self.title = title
        self.isbn = isbn

        def printBook(self):
            print(self.title + ", " + self.isbn)

print ("done practicing classes\n\n")

print("practicing use a module")
from mymodule.helper_utils import square

print(square(100))

print ("done practicing use a module")
