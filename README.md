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
x.isalpha() # Will return True because all the chars in x are alpha
x.isalnum() # Will return True because all the chars in x are alphanumerical
x.isdigit() # Will return False because the chars in x are not all numbers
print(x.upper()) # Will print string will all chars capitalised
print(x.capitalised()) # Will print string but with first char capitalised
```
