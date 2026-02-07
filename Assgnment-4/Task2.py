# Take input and write to file
text1 = input("Enter text to write to the file: ")

file = open("output.txt", "w")
file.write(text1 + "\n")
file.close()

print("Data successfully written to output.txt.")

# Take input and append to file
text2 = input("Enter additional text to append: ")

file = open("output.txt", "a")
file.write(text2 + "\n")
file.close()

print("Data successfully appended.")

# Read and display final content
print("\nFinal content of output.txt:")

file = open("output.txt", "r")
for line in file:
    print(line.strip())
file.close()
