import sys


def main():
    # We loop the arguments
    for arg in sys.argv[1::]:
        # We open the file, get the content and print it
        file = open(arg, "r")
        content = file.read()
        print(content)

        # We close the file
        file.close()

if __name__ == '__main__':
    main()
