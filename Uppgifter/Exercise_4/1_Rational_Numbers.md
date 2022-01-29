We have talked that arithmetics with floating point numbers is imprecise due to rounding errors. One way to avoid that is to use rational numbers instead of floating point numbers. In this way, for example, the number 1/3 can be stored exactly, while with a floating point the best that we can get is 0.333...333 with a finite sequence of digits after the dot, while mathematically it should continue indefinitely. For that purpose Python provides the module fractions.

Try this in the Python shell:

```python console
>>> from fractions import *
>>> x = Fraction(1,3)
>>> 2*x
Fraction(2, 3)
>>> y=Fraction(1,2)
>>> x+y
Fraction(5, 6)
```

Here, after the import, we first assign to x the value 1/3 which in Python is written as Fraction(1,3). After that we print the result of 2\*x which is equal to 2/3. Finally we assign to y the value 1/2 and we print the result of x+y which is 5/6.

Fraction in Python is actually a class. When you say Fraction(1,2) this calls the constructor of the class which stores the numbers 1 and 2 to two attributes. Whenever we use an operator like \*, +, /, etc., Python actually calls a method. Here is a list of operators and their corresponding methods:

| Operator | Method          |
|----------|-----------------|
| +        | \_\_add\_\_     |
| -        | \_\_neg\_\_     |
| -        | \_\_sub\_\_     |
| *        | \_\_mul\_\_     |
| /        | \_\_truediv\_\_ |
| <        | \_\_lt\_\_      |
| <=       | \_\_le\_\_      |
| ==       | \_\_eq\_\_      |
| !=       | \_\_ne\_\_      |
| >        | \_\_gt\_\_      |
| >=       | \_\_ge\_\_      |

When you type an expression in the Python shell, the result can be an object of an arbitary type. In order to show the result, Python calls the method `__repr__` from that object, which can be redefined to provide a user friendly representation. That is how Python knows that fractions should be printed as `Fraction(5, 6)`.

This replacement of operators with method calls lets us to redefine what different operators mean for different types. The following tasks are an exercise in defining your own types. Implement the class `Ratio` with at least the following methods:
* a constructor `__init__` which should take as arguments the nominator and denominator of the fraction and save them in attributes. Note that for instance `6/10` is just another representation for `3/5`. A correct implementation must first divide both the nominator and the denominator by their greatest common divisor. The math module provides the function `gcd` which computes the divisor. For example:
  ```python console
  >>> import math
  >>> math.gcd(6,10)
  2
  ```

    Now if we divide both the nominator and the denominator, we get `(6/2)/(10/2)` => `3/5`.

* a method `__repr__` for conversion to a string. The method should return a string composed of the class name and the nominator and the denominator.
* a method `__add__` for adding two rationals.
* a method `__mul__` for multiplying two rationals.
* a method `__eq__` for checking whether two rationals are equal, i.e. whether they have the same nominators and denominators.

```python
import math

class Ratio:
  def __init__(self, nom, denom):
    # TODO
    pass

  def __repr__(self):
    # TODO
    return s

  def __add__(self,other):
    # TODO
    return Ratio(nom , denom)

  def __mul__(self,other):
    # TODO
    return Ratio(nom , denom)

  def __eq__(self,other):
    # TODO
    return res
```
