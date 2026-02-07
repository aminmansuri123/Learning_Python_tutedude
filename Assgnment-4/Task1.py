try:
    print("Reading file content:")
    file = open("sample.txt", "r")
    i = 1
    for line in file:
        print("Line", i, ":", line.strip())
        i += 1
    file.close()
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")
