Implement the class `Card` to represent a playing card. Your class should have the following methods:

* `__init__(self, rank, suit)`: here rank is an integer in the range 1-13 indicating the position of the card in the list:
   Ace, 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King

   Suit is a single character: 'd', 'c', 'h', or 's', indicating one of the suits (diamonds, clubs, hearts or spades).

* `getRank(self)`: Returns the rank of the card.
* `getSuit(self)`: Returns the suit of the card.
* `value(self)`: Returns the Blackjack value of the card. Ace counts as 1, Jack, Queen and King count as 10. For all other cards the value is the same as the rank.
* `__str__(self)`: Returns a string that names the card. For example 'Ace of Spades'
