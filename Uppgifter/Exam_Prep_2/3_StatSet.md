Create a class called `StatSet` that can be used to do simple statistical calculations. The methods for the class are:

* `__init__(self)`: Initializes a StatSet with no data in it.
* `addNumber(self, x)`: Adds the number `x` to the `StatSet`.
* `mean(self)`: Returns the mean (the average) of the numbers in the `StatSet`.
* `median(self)`: Returns the median, i.e. the average of the minimum and the maximum value in the set.
* `stdDev2(self)`: Returns the squared standard deviation of the numbers in the `StatSet`, computed according to the formula:

  <img src="./3_StatSet.dark.svg#gh-dark-mode-only" alt="Standard Deviation" width="250pt" />
  <img src="./3_StatSet.light.svg#gh-light-mode-only" alt="Standard Deviation" width="250pt" />

* `count(self)`: Returns the count of numbers in the set.
* `min(self)`: Returns the smallest number in the set.
* `max(self)`: Returns the biggest number in the set.
