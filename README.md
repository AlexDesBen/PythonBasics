# PythonBasics

## To launch:
```
cd ~/git/.../PythonBasics/script/folder
python Main.py
```
## To know

### Importing libraries
```
import library
import library as nickname
from library import module
from library import module as nickname
```
With a library you can use all the modules and sub modules like this
```
library.module()
library.module.submodules()
```

Never do 
```
from library import *
```
It imports the library directly in the script without namespace and might crush already imported modules.


### Printing to screen
```
print("string of text")
```

### if, for & while

The syntax is as follow

if:
```
if foo == bar:
  print("yes")
elif foo == "woody":
  print("Gone!!")
else:
  print("Caribou!")
```
for:
```
L = ["spam","spamety","spamspam"]
for element in L:
  print(element)
```
while:
```
i = 0
while i < 3:
  print(L[i])
  i += 1
```
### Objects

In python, everything is an object. See documentation for information.

Examples:
```
x = "string of text"
x.isalpha()            # Will return True because all the chars in x are alpha
x.isalnum()            # Will return True because all the chars in x are alphanumerical
x.isdigit()            # Will return False because the chars in x are not all numbers
print(x.upper())       # Will print string will all chars capitalised
print(x.capitalised()) # Will print string but with first char capitalised
```

### def

In python you can define functions like this
```
def SomeFunction(argument1, argument2):
  temp = argument1 + argument2  # Add both arguments
  output = temp**2              # Square variable temp
  return output                 # Return the value of the variable output
```
and used like this in a script
```
x = SomeFunction(2, 3)
print(x) # Would return (2+3)**2 = 25
```

### Class

In python you can define your own classes and inherit from other classes
```
class MyClass(ParentClass):                      # Leave empty of there is no need for a Parent class
  def __init__(self, arg1, arg2, arg3, ...):
    ParentClass.__init__(self, arg1, arg2, ...)
    self.stuff = arg1
    self.otherStuff = arg2
    self.lastBitOfStuff = arg3
  def NewMethod(self, SomeArgument):
    self.stuff = SomeArgument
```
in the code:
```
class Human():
  def __init__(self, Name, Age):
    self.Name = Name
    self.Age = Age
  def setName(self,NewName):
    self.Name = NewName.capitalise()  #Will change my name and make sure it's capitalised

Moi = Human("Alex", 33)
print(Moi.Age)                        # Will print my age, 33
print(Moi.Name)                       # Will print my name, Alex
Moi.setName("charles")                # Will change my name to Charles
print(Moi.Name)                       # Will print my name, Charles
```



