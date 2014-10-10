def sevens_in_a_row(arr, n):
    max_sevens = 0 # The variable that the algorithm needs to find
    current_sevens = 0

    # Finding the max sevens in a row, by checking every element
    for i in arr:
        if(i == 7):
            current_sevens += 1
        elif(i != 7):
            if(current_sevens > max_sevens):
                max_sevens = current_sevens
                current_sevens = 0
        else:
            die("Something went wrong!")

    # In the end we just check if we have the needed sevens in a row
    if(max_sevens >= n):
        return True
    else:
        return False