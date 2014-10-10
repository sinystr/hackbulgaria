from sum_digits import make_valid
from sum_of_all_devisors import sum_of_all_devisors


def is_prime(number):
    number = make_valid(number)
    if(number == 1):
        return False
    # If it's a prime number (has 2 devidors - 1 and the number)
    # we return true
    elif(sum_of_all_devisors(number) == number + 1):
        return True
    elif(sum_of_all_devisors(number) != number + 1):
        return False
    else:
        die("Something went wrong!")
