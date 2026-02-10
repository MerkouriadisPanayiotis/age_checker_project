from datetime import date, datetime

def age_checker(date_of_birth: str) -> str:
    if type(date_of_birth) is not str:
        raise TypeError("error")
    
    age_in_years = 0

    try:
        age_as_date = datetime.strptime(date_of_birth, "%Y-%m-%d").date()
        today = date.today()

        date_diff = today - age_as_date

        age_in_years = date_diff.days // 365

    except ValueError:        
        raise ValueError("DOB must be in YYYY-MM-DD format")



    if age_in_years > 15:
        return "access granted"
    else:
        return f"access denied you are {age_in_years} years old you must be 16 years of age or older to access this site"
    
    
