One public school every year receives applications for new students. Each application is sent through a web site and the relevant information is packaged in an instance of the class `Application` shown below.

The number of students that will be accepted is always fixed in advance and the students are accepted in the order in which they have sent their applications. Moreover only applications from students who live at most five kilometers from the schools are considered.

Add the class `ApplicationList` which collects the applications. The class should contain the following components:

* An `__init__` method:

  ```python
      def __init__(self, nrOfStudents): ...
  ```

    where `nrOfStudents` is the number of students that will be accepted this year.

* A method which adds a new application:

  ```python
      def addApplication(self, app): ...
  ```

* A method which prints the list of students that were accepted:

  ```python
      def printAccepted(self): ...
  ```
    Each student should be printed with its name and personal number.


```python
class Application:
    def __init__(self, name, personalNum, distance):
        self.name        = name
        self.personalNum = personalNum
        self.distance    = distance
    def getName(self): return self.name
    def getPersonalNumber(self): return self.personalNum
    def distanceFromSchool(self): return self.distance
```
