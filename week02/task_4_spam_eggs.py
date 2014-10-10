def prepare_meal(number):
    n = 0
    spam_and_eggs = ""

    while number != 1 and number != 5:
        if(number % 3 == 0):
            n += 1
            number //= 3

    for i in range(0, n + 1):
        if(i == n):
            if(number == 3):
                spam_and_eggs += "spam"
            else:
                spam_and_eggs += "and eggs"
        else:
            spam_and_eggs += "spam "

    return spam_and_eggs
