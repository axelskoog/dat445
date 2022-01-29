Write a function called `basel` to compute the [Basel sum](https://en.wikipedia.org/wiki/Basel_problem):

![Basel Sum](./1_basel.dark.svg#gh-dark-mode-only)
![Basel Sum](./1_basel.light.svg#gh-light-mode-only)

The sum has infinitely many terms but it eventually converges to π2/6. Your function should take a parameter `epsilon` and sum as many terms as possible until the next one is less than epsilon.

Note that we don't know in advance how many terms to sum, instead we have a termination condition. This indicates that it is convenient to use a `while` loop.
