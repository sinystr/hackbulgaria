from random import randint
import sys

# The function that returns random number as a string
def generateRandom():
    return str(randint(1, 1000))


def main():
    # The 3 arguments that we need
    script, filename, numbers = sys.argv

    # Casting numbers to int, to use it in "for"
    numbers = int(numbers)
    target = open(filename, 'w')

    for i in range(0, numbers):
        target.write(generateRandom())
        target.write(" ")

if __name__ == '__main__':
    main()
