The number C<sup>n</sup><sub>k</sub> indicates the number of [combinations](https://en.wikipedia.org/wiki/Combination) that can be formed with `k` elements out of `n` in total. The combinations can be computed recursively by using the formula C<sup>n</sup><sub>k</sub> = C<sup>n-1</sup><sub>k-1</sub> + C<sup>n-1</sup><sub>k</sub>. The basic cases are that for every `n`, C<sup>n</sup><sub>1</sub> == n, and when n \< k, C<sup>n</sup><sub>k</sub> == 0.

Write the function `combinations(n, k)` which implements the recursive formula.
