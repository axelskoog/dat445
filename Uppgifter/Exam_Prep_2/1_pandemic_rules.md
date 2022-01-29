The country C has set rules for traveling to the country during an ongoing pandemic. The rules are the following:

* the number of infections in a country are calculated as the number of cases for two weeks per 100 000 citizens.
* if the traveler's country has number of infections 50 or higher, the country is red and traveling from that country is forbidden.
* if the traveler's country has number of infections 25 or higher, but below 50, the country is yellow and traveling from it is allowed, with ten days quarantine.
* if the traveler's country has number of infections less than 25, the country is green and traveling from it is allowed.
* exception: if the traveler's country has number of infections lower than the number of infections in C, the country is green regardless of the number.

Write a function `pandemic_rules(numC, totalNum, population)`, which takes as arguments the actual number of infections in C (`numC`), together with the total number of cases for two weeks (`totalNum`) and the population size in the traveler's country (`population`), and returns the color of the country.
