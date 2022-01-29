A quick way to decide if a number is divisible by 9 is to compute the sum of its digits. If you do that recursively, at the end, you will get only a single digit. That last digit is always 9 for all numbers divisible by 9. The only exception is for the number 0 where the last digit is the zero itself.

Example: 1998 → 1+9+9+8 → 27 → 2+7 → 9.

Write the function `div9(num)` which does the divisibility test and and prints out the intermediate sums after each step.
