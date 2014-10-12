import sys


def main():
    # The 2 arguments that we need
    script, filename = sys.argv

    # Opening the file, reading the first line and closing it
    target = open(filename, 'r')
    string = target.readline()
    target.close()

    # Making the string into an array and removing the empty items
    string = string.split(' ')

    # The variable that we are gonna return
    nubmers_sum = 0

    for i in string:
        nubmers_sum += int(i)

    return nubmers_sum

if __name__ == '__main__':
    print(main())
