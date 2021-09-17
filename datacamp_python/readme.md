# Python Creator:
>Guido van Rossum
***
# IPython Creator:
>Fernando Pérez
***
* Ipython is part of boarder jupyter system

# PYTHON USES ZERO INDEXING

# Python Scripts
* Explicitly mention print and other functions

# Objects:
Examples: Str, List, Int and so on
Everything == Object

# Functions:
predefined functions and user-defined functions
help()
complex()

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
# Using numpy package
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

# Math package
* radians
* pi

# List Recap
* Powerful
* Collection of values
* Hold different values
* Change, Add and Remove
* **Still very slow and doesnt have list functions, Solution: Use Numpy array**

# Numpy solution to list
* Perform operations in numpy.array() as if single values
# Numpy remarks
* Assumes that np.array() contain values of **same type**
* np.array() is a **DATATYPE** and comes with its own methods
* Excels at vector arithmetic
# Numpy Subsetting
```
a = np.array({1,2,3])
a[1]
# 2
a > 1
# array([False, True, True], dtype=bool)
a[a > 1]
# array([2,3])
```
# Numpy 2D subsetting
```
b = np.array([2, 7, 29])
np_2d = np.array(a,b)
np_2d[0][2]
# 3
np_2d[0,2]
# 3
np_2d[:,1:3]
np_2d[:,1]
np_2d[1,:]
n_2d.shape
```
# Numpy Basic Statistics
```
np.mean()
np.median()
np.corrcoeff(list, list) #to check if lists are correlated
np.std()
np.sum()
np.sort()
```
# Generate Data using Numpy
* Arguements for np.random.normal()
    * distribution Mean
    * distribution standard deviation
    * number of samples
```
height = np.round(np.random.normal(1.75, 0.20, 5000), 2)

weight = np.round(np.random.normal(60.32, 15, 5000), 2)

np_city = np.column_stack((height, weight))
```

# Sample beginner code, to be deleted after I am good at numpy
```
# baseball is available as a regular list of lists
# updated is available as 2D numpy array

# Import numpy package
import numpy as np

# Create np_baseball (3 cols)
np_baseball = np.array(baseball)

# Print out addition of np_baseball and updated
print(np_baseball + updated)

# Create numpy array: conversion
conversion = np.array([0.0254, 0.453592, 1])

# Print out product of np_baseball and conversion
print(np_baseball * conversion)
```
# Numpy sideffects
* numpy arrays cannot contain elements with different types. If you try to build such a list, some of the elements' types are changed to end up with a homogeneous list. This is known as **type coercion**


# Simple yet effective codes:
\+ --> to concate

# Some Basic Miscellaneous stuff u.u
* Circumference = 2πr
* Area = πr^2
* Calculate the distance travelled by the Moon over 12 degrees of its orbit: r * phi (phi -> angle in radians)
* height_in_meters = heigh_in_inch * 0.0254
* weight_in_kg = weight_in_lb * 0.453592



