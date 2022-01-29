Implement a class `TrainSeats` which realizes a naive system for train tickets. For the sake of simplicity we will assume that the seats are simply numbered with integers and there are no separate car numbers, rows, etc. The class should have the following components:

* An `__init__` method:

  ```python
      def __init__(self, nrOfSeats): ...
  ```
    where `nrOfSeats` is the number of seats in the train. When you construct a new object then by default all seats in the train are free.

* The user can book a seat on the train by calling one of the methods:

  ```python
      def pick(self, seatNum): ...
      def book(self, n): ...
  ```

    Calling `pick(seatNum)` reserves a seat with number `seatNum` and the method returns `True` if the reservation was successful. If the seat is already booked then the result must be `False`. In contrast, calling `book(n)` reserves `n` seats from the train and the user has no way to choose which seats will be allocated; the simplest strategy is that you just allocate the first n available seats that you find. The seats don’t have to be next to each other. Seats that are already reserved with `pick()` or `book()` cannot be reserved again. The result from `book()` is a list with `n` elements which contains the numbers of the allocated seats. If it is impossible to find `n` free seats then no booking is made and the result must be the special value `None`.
