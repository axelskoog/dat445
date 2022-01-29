The greatest common divisor of two natural numbers `m` and `n` is the largest natural number `d` such that both `m` and `n` are divisible by `d`. Such greatest common divisor exists if `m` and `n` are not both zero.

Example: The greatest common divisor of 60 and 84 is 12, which the reader is invited to check for himself/herself.

Your task is to complete the function `gcd` which calculates and returns the greatest common divisor of arguments `m` and `n` by using Euclid's algorithm:

* If `n` is 0, the result is `m`.
* Otherwise, the greatest common divisor of `m` and `n` is equal to the greatest common divisor of `n` and `m % n` (where `m % n` is the remainder of dividing `m` by `n`).

For example we get that:

    gcd(84,60) == gcd(60,24)
    gcd(60,24) == gcd(24,12)
    gcd(24,12) == gcd(12,0)
    gcd(12,0)  == 12
