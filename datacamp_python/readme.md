# Python Creator:
>Guido van Rossum
***
# IPython Creator:
>Fernando Pérez
***
* Ipython is part of boarder jupyter system

# Python Scripts
* Explicitly mention print and other functions

# Python as a calculator
* Exponentiation: **. This operator raises the number to its left to the power of the number to its right. For example 4**2 will give 16.
* Modulo: %. This operator returns the remainder of the division of the number to the left by the number on its right. For example 18 % 7 equals 4

# Objects:
Examples: Str, List, Int and so on
Everything == Object

# Functions:
predefined functions and user-defined functions
help()
complex()

# Simple yet effective codes:
\+ --> to concate

# Methods
> This is something that I dont understand fully
* Funtions that belong to objects
* Each object has specific methods associated
* **Some methods can change the objects they are called on**\
Ex: 
* Str --> capitalize() or replace()
> capitalize --> Returns string where the first letter is capitalized
> replace --> replace some parts of the string
* float --> bit_length() or conjugate()
* list --> index() or count() or append() or remove() or reverse
> index --> gives you the index of element in a list
> count --> gives you the number of times element is repeated
> append --> extends list, essentially changing them

# Packages
* Directory of python scripts
* Each script = module
* Modules specify functions, methods, types etc
# Ex:
* Numpy -> to effectively work with arrays
* Matplotlib -> Data Visulization
* scikit-learn -> for ML
# Installing packages
**Use pip to install python packages**
* pip -> prefered installer program
* download get.pip.py
* Terminal: python3 get-pip.py
# Using numpy
``` 
import numpy
numpy.array([1,2,12])
```
> This can be tiresome, so use:
```
import numpy as np
np.array([1,2,12])
```
> To use one specific function from a package:
```
from numpy import array
# You can simply use "array()" now, instead of "np.array()"
array([1,2,12])
```
> Limit using functions from package in this manner as it is hard for someone else to understand especially when the code is very long

# Some Basic Geometry u.u
* Circumference = 2πr
* Area = πr^2
* Calculate the distance travelled by the Moon over 12 degrees of its orbit: r * phi (phi -> angle in radians)
# Math package
* radians
* pi

