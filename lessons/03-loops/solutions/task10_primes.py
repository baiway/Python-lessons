for number in range(2, 100):
    # Assume the number is prime until we find something that divides it
    is_prime = True
    for divisor in range(2, number):
        if number % divisor == 0:
            is_prime = False
            break  # no need to check any more divisors

    if is_prime:
        print(number)
