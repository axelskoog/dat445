The logistic map is a function from a real number in the range [0; 1] to another number in the same range. Using the map:

![logmap](./1_Logistic_Map.dark.svg#gh-dark-mode-only)
![logmap](./1_Logistic_Map.light.svg#gh-light-mode-only)

and an initial number, we can generate a sequence of numbers. Here 0 < r <= 4 is a fixed parameter. For example, if r=3.9, and we start with the number 0.2, then the next number will be 3.9\*0.2\*(1-0.2) == 0.624. We can repeat the mapping and get a sequence:

0.2, 0.624, 0.915, 0.303, 0.824 ...

The [logistic map](https://en.wikipedia.org/wiki/Logistic_map) was first popularized in a 1976 paper by [Robert May](https://en.wikipedia.org/wiki/Robert_May,_Baron_May_of_Oxford) for modelling the size of a population of rabbits. It is interesting because it can exhibit both simple periodic behaviour as well as complex chaotic behaviour.

Your task is to implement three functions which make it possible to experiment with the logicstic map:

1. a function `logmap(r, x)` which takes the value of r and the current x and returns the next number in the sequence.
2. a function `experiment(r, x, n)` which also takes r and x but also the parameter n which indicates how many numbers it should compute. Unlike `logmap`, the new function should not return the numbers, but print them directly on the screen. Here is an example print out from the function:

   ```python console
   >>> experiment(3.9,0.2,10)
   0.2
   0.6240000000000001
   0.9150335999999998
   0.30321373239705673
   0.8239731430433209
   0.5656614700878645
   0.9581854282490118
   0.1562578420270518
   0.5141811824451928
   0.9742156868513789
   ```

   and another example:

   ```python console
   >>> experiment(3.9,0.21,10)
   0.21
   0.64701
   0.8907134336100001
   0.3796377499070677
   0.9185004221350089
   0.29194384702399534
   0.8061792851144187
   0.6093915569306115
   0.9283306003619574
   0.2594782974949042
   ```

   Notice that above we started with two very similar initial values 0.2 and 0.21, but the rest of the sequence quickly becomes very different. This is a typical deterministic but chaotic behaviour.

3. Implement a third function `table(r, x1, x2, n)` which prints two sequences side by side, starting from two different start values x1 and x2. Example:

   ```python console
   >>> table(3.9,0.20,0.21,10)
   0.2 0.21
   0.6240000000000001 0.64701
   0.9150335999999998 0.8907134336100001
   0.30321373239705673 0.3796377499070677
   0.8239731430433209 0.9185004221350089
   0.5656614700878645 0.29194384702399534
   0.9581854282490118 0.8061792851144187
   0.1562578420270518 0.6093915569306115
   0.5141811824451928 0.9283306003619574
   0.9742156868513789 0.2594782974949042
   ```
