In the lecture, we talked about binary search and wrote an iterative solution. In this task you need to write a recursive alternative. The function `binarySearch` below should use recursion to find the position of a key in a sorted list. The search should be limited to the range from element with index `i` to the element with index `j`. If the key is not in the range then the return value must be `None`. The basic steps in the implementation should be as follows:

* If the given range is empty, i.e. `i > j` then just return `None`.
* Compare the element at position `k=(i+j)/2` with the key.
* If the element is bigger than the key then recursively search in the range `i` to `k-1`.
* If the element is smaller than the key, then recursively search in the range `k+1` to `j`.
* If the element is equal to the key then return `k`.
  
```python
def binarySearch(values, i, j, key):
  pass
```