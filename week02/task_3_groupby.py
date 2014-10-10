def groupby(func, seq):
    results_dict = {}
    # Checking if the result exist in the dictrionary
    # if not, we create new key with the result
    # and if it exist, we just append the new-found item
    for i in seq:
        if func(i) in results_dict.keys():
            results_dict[func(i)].append(i)
        else:
            results_dict[func(i)] = [i]
    return results_dict

