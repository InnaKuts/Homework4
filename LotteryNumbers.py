import random

def get_numbers_ticket(min, max, quantity):
    # Check for input parameters 
    if min < 1 or max > 1000 or quantity < 1 or quantity > (max - min + 1):
        return []
    # Random nummbers generation
    generated_numbers = random.sample(range(min, max + 1), quantity)
    # Sorting
    sorted_numbers = sorted(generated_numbers)
    return sorted_numbers

lottery_numbers = get_numbers_ticket(5, 49, 1)
print("Lottery_numbers: ", lottery_numbers)

            