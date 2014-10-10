from task_8_contains_digit import contains_digit

def contains_digits(number, digits):
    #checking if the array contains every single digit
    while len(digits) > 0:
        if(not contains_digit(number,digits.pop(0))):
            return False

    return True
