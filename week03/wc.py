import sys


def words(filename):
    return len(open(filename, "r").read().split())


def chars(filename):
    print(len(open(filename, "r").read()))


def lines(filename):
    print(open(filename, "r").read().count("\n"))


def main():
    funcs = {'words': words, 'chars': chars, 'lines': lines}
    script, option, filename = sys.argv
    print(funcs[option](filename))

if __name__ == '__main__':
    main()
