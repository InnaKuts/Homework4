from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    current_date = datetime.now().date()
    upcoming_birthdays = []

    for user in users:
        # Get user's birthday and convert it to datetime object
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        
        # Replace year with current year to calculate upcoming birthday
        birthday_this_year = birthday.replace(year=current_date.year)
        
        # If birthday has passed this year, calculate for next year
        if birthday_this_year < current_date:
            birthday_this_year = birthday_this_year.replace(year=current_date.year + 1)
        
        # Calculate days until upcoming birthday
        days_until_birthday = (birthday_this_year - current_date).days
        
        # Check if birthday is within the next 7 days, including today excluding same day of next week
        if 0 <= days_until_birthday < 7:
            weekday = birthday_this_year.weekday()
            # Check if birthday falls on a weekend (Saturday or Sunday)
            if weekday in [5, 6]:  # 5: Saturday, 6: Sunday
                # Adjust birthday to the next Monday
                birthday_this_year += timedelta(days = 7 - weekday)
            
            # Add user's name and upcoming birthday date to the list
            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": birthday_this_year.strftime("%Y.%m.%d")
            })

    return upcoming_birthdays

# Example usage
users = [
    {"name": "John Doe A", "birthday": "1985.07.01"},
    {"name": "John Doe B", "birthday": "1985.07.02"},
    {"name": "John Doe C", "birthday": "1985.07.03"},
    {"name": "John Doe D", "birthday": "1985.07.04"},
    {"name": "Jane Smith A", "birthday": "1990.07.06"},
    {"name": "Jane Smith B", "birthday": "1990.07.07"},
    {"name": "Jane Smith C", "birthday": "1990.07.08"},
    {"name": "Jane Smith D", "birthday": "1990.07.10"},
    {"name": "Jane Smith E", "birthday": "1990.07.11"},
    {"name": "Jane Smith G", "birthday": "1990.07.12"},
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)