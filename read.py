try:
    file1 = open('sample.txt', 'r')
    print("Reading file contents:\n")
    reading_file = file1.readlines()
    for index, line in enumerate(reading_file, start=1):
        print(f"Line {index}: {line.strip()}")
    file1.close()
except FileNotFoundError:
    print('Error: The file sample txt was not found.')

