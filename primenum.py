def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

x = int(input("Enter a number to see if it's prime: "))
if is_prime(x):
    print(f"{x} is a prime number.")
else:
    print(f"{x} is not a prime number.")
