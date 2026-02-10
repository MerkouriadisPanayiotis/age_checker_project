from lib.age_checker import age_checker
from datetime import date
import pytest
"""
    Given the date of birth that equates to age of 16 years old or above
    Returns message "access granted"
"""

def test_age_checker_old_enough():
    result = age_checker("1967-10-22")
    assert result == "access granted"

"""
    Given the date of birth that equates to the age below 16 years old
    Returns message "access denied you are {true_age} years old you must be 16 years of age or older to access this site"
"""

def test_age_checker_not_old_enough():
    age_string = "2017-01-22"
    today = date.today()
    age_as_date = date.strptime(age_string, "%Y-%m-%d")
    date_diff = today - age_as_date
    age_in_years = date_diff.days // 365
    
    result = age_checker(age_string)

    assert result == f"access denied you are {age_in_years} years old you must be 16 years of age or older to access this site"

"""
    Given incorrect type or format of date
    Raises an exception
"""

def test_age_checker_wrong_type_format():
    #Invalid format YYYY MMM DD
    with pytest.raises(Exception) as e:
        age_checker("1967-january-01")
    result = str(e.value)
    assert result == "DOB must be in YYYY-MM-DD format"
    #Invalid format DD-MM-YYYY
    with pytest.raises(Exception) as e:
        age_checker("22-04-2020")
    result = str(e.value)
    assert result == "DOB must be in YYYY-MM-DD format"
    #Invalid type (int)
    with pytest.raises(TypeError) as e:
        age_checker(19670222)
    result = str(e.value)
    assert result == "error"