import sys


def main():
    # We expect 3 arguments, the script and the two files
    script, filename, second_filename = sys.argv

    # We open the files, get the content and write it into megatron
    file = open(filename, "r")
    content = file.read()
    second_file = open(second_filename, "r")
    second_content = second_file.read()

    megatron = open("MEGATRON.txt", "a")
    megatron.write('\n')
    megatron.write(content)
    megatron.write('\n')
    megatron.write(second_content)

    # We close the files
    file.close()
    second_file.close()
    megatron.close()

if __name__ == '__main__':
    main()
