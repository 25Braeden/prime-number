"""
This module provides a function to check if a given number is prime.
"""

def is_prime(number):
    """
    Check if the given number is prime.

    Args:
        number (int): The number to check.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


while True:
    while True:
        try:
            x = int(input("Enter a number to see if it's prime: "))
            break
        except ValueError:
            print("You did not enter a valid number.")

    if is_prime(x):
        print(f"{x} is a prime number.")
    else:
        print(f"{x} is not a prime number.")

    while True:
        new_num = input("Would you like to see if another number is prime? (Y/N): ").lower()
        if new_num in ['y', 'n']:
            break
        else:
            print("Invalid input, please enter 'Y' or 'N'.")

    if new_num == 'n':
        break
    