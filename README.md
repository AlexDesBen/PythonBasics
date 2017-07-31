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

### Objects

In python, everything is an object. See documentation for information.

Examples:
```
x = "string of text"
x.isalpha() #will return True
x.isdigit() #will return False
print(x.upper()) #will print string will all chars capitalised
print(x.capitalised()) #will print string but with first char capitalised
```
