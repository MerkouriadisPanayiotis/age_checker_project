# {{PROBLEM}} Function Design Recipe


## 1. Describe the Problem

As an admin
So that I can determine whether a user is old enough
I want to allow them to enter their date of birth as a string in the format `YYYY-MM-DD`.

As an admin
So that under-age users can be denied entry
I want to send a message to any user under the age of 16 saying their access is denied
And telling them their current age and the required age (16).

As an admin
So that old enough users can be granted access
I want to send a message to any user aged 16 or older to say that access has been granted.

As an admin
So that invalid entries are rejected
I want to generate an exception when the date of birth isn't the right type or format.


## 2. Design the Function Signature

function must determine if a user is old enough (16 or older)
accept a date string representing the date of birth in the format YYYY-MM-DD


```python

    def age_checker(date_of_birth):
        pass
        """returns message with the status access authorized

        side effects:the string would get casted into the data type (date-time) 
```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python
age_checker("1967-10-22") "access granted"
age_checker("2017-01-22") "access denied you are 9 years old you must be 16 years of age or older to access this site"
age_checker("1967-10-22") "access granted"
age_checker("") "error"
age_checker("1967-january-01")"error"
age_checker("22-04-2020)"error incorrect format"
age_checker(19670222)"error"
```
## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
# EXAMPLE

from lib.extract_uppercase import *

"""
Given a lower and an uppercase word
It returns a list with the uppercase word
"""
def test_extract_uppercase_with_upper_then_lower():
    result = extract_uppercase("hello WORLD")
    assert result == ["WORLD"]
```

Ensure all test function names are unique, otherwise pytest will ignore them!
