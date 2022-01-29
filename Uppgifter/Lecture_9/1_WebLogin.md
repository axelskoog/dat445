Given the class `User`, add the class `WebLogin` which controlls user passwords for a web site. It must have the following components:

* One or more instance variables to keep track of which users are registered on the web site.
* An `__init__` method which initializes the instance variables.
* A method for registering new users:

  ```python
      def addUser(self, name, password, email): ...
  ```

    It remembers the user with its name, password and e-mail, and the information is used in the other methods.

* A method for checking the user name and the password:

  ```python
      def login(self, name, password): ...
  ```

    It must return True if there is a user with that name and password, and False in all other cases.

* A method which can be used to remind the user of his/her password:

  ```python
      def sendPassword(self, name): ...
  ```

    If there is a user with the given name then the method should call the method `sendMessage` from `User` with the message `"Your password is: 123"` where instead of 123 your should place the real password.


```python
class User:
  def __init__(self, name, password, email):
    self.name = name
    self.password = password
    self.email = email
  def getName(self): return self.name
  def getPassword(self): return self.password
  def sendMessage(self,message): print(message,"sent to",self.email)

```
