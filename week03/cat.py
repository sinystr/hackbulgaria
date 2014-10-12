import sys


def main():
    # We expect 2 arguments, the script and the file
    script, filename = sys.argv

    # We open the file, get the content and print it
    file = open(filename, "r")
    content = file.read()
    print(content)

    # We close the file
    file.close()

if __name__ == '__main__':
    main()
