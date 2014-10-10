def reduce_file_path(path):
    path_array = path.split('/')
    valid_path = '/'

    # Splitting the array to keys and removing the useless values
    removed = 0
    for i in range(0, len(path_array)):
        if path_array[i - removed] == '' or path_array[i - removed] == '.':
            path_array.pop(i - removed)
            removed += 1

    # Checking for ".." and deleting it +
    # the element before the "..", only if it exists
    removed = 0
    for i in range(0, len(path_array)):
        if path_array[i - removed] == '..':
            path_array.pop(i - removed)
            # removing the previous element, only if it exists
            if len(path_array) > 0:
                path_array.pop(i - removed - 1)
                removed += 2
            else:
                removed += 1

    # Making the array a string
    for i in range(0, len(path_array)):
        valid_path += path_array[i]

        if(i != len(path_array) - 1):
            valid_path += '/'

    return valid_path
