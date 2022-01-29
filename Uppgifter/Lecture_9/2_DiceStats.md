Every time when we throw a dice we get a random number from 1 to 6. A fair dice should roll to any of its sides with an equal probability. Write the class `DiceStats` that can be used to check whether a dice is fair. It should have the following methods:

* an `__init__` method to initialize all attributes that you need.
* a method to register a new roll of the dice:

  ```python
      def addRoll(self, roll): ...
  ```

    Here, `roll` is a number between 1 and 6.

* a method to compute the frequences of all possible outcomes:

  ```python
      def getFrequences(self): ...
  ```

    The frequency of an outcome is the number of times the corresponding number rolled up divided by the total number of dice rolls. The result from `getFrequences()` should be a list which contains one frequency for each possible outcome.

* a method to estimate whether the dice is fair:

  ```python
      def isFair(self,epsilon): ...
  ```

    A dice is fair if the frequencies for each outcome is in the range 1/6 ± epsilon. The method should return True/False depending on whether the dice is fair.
