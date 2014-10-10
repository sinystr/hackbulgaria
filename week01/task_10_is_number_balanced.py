def is_number_balanced(number):
    numbers = []
    while number > 0:
        numbers.append(number % 10)
        number //= 10

    left_side = 0
    right_side = 0

    #calculating the left side
    for i in range(0,len(numbers) // 2):
        left_side += numbers[i]
        
    start = (len(numbers) // 2)
    # Checking is the number odd, so we can know where to start checking
    # the right side

    if(len(numbers) % 2 != 0):
        start += 1

    #calculating the right side
    for i in range(start, len(numbers)):
        right_side += numbers[i]

    if(left_side == right_side):
        return True

    return False

print(is_number_balanced(2331323))