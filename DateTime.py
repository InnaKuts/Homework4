from datetime import datetime

def get_days_from_today(date_str):
    try:
        #Creating datetime from date string
        datetime_from_date = datetime.strptime(date_str, "%Y-%m-%d")
        #Getting current date
        current_date = datetime.now()
        days_since = current_date.toordinal() - datetime_from_date.toordinal()
        return days_since
    except ValueError:
        raise ValueError("Incorrect date format, please use YYYY-MM-DD")
    
try:
    days_since_now = get_days_from_today("2024-06-04")
    print(f"Days since now {days_since_now}")
except ValueError as e:
    print(e)

    
