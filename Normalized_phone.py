import re

def normalize_phone(phone_number):
    # Cleaning all sympols except numbers and "+" if present
    cleaned_number = re.sub(r'[^\d\+]', '', phone_number)

    # Adding "+" if "+" is absent but code is present
    if cleaned_number.startswith('380'):
        cleaned_number = '+' + cleaned_number
    # Adding "+38" if both code and + are absent
    elif not cleaned_number.startswith('+'):
        cleaned_number = '+38' + cleaned_number
    
    return cleaned_number

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)