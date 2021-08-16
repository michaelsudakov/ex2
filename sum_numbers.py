import argparse

try:
    sum = 0
    parser = argparse.ArgumentParser()
    parser.add_argument("file_path")
    args = parser.parse_args()
    file_reader = open(args.file_path, "r")
    for number in file_reader:
        sum += int(number)
    print(sum)

except IOError:
    print("File not found. ")

except ValueError:
    print("The file is empty or the file contains characters ")
