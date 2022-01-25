Implement the function `passwords` which given a file name builds a dictionary with user/password pairs. Each line of the file contains a user name and a password separated by space.

For example if the file passwords.txt contains:
```
jim 1234
karolina k333
beth bravo
```
then `passwords('passwords.txt')` must return `{'jim': '1234', 'karolina': 'k333', 'beth': 'bravo'}`
