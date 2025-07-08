text = input("Enter text to write to the file: ")
with open("output.txt", "w") as file:
    file.write(text + "\n")
print("Data successfully written to output.txt.")

additional_text = input("Enter additional text to append: ")
with open("output.txt", "a") as file:
    file.write(additional_text + "\n")
print("Data successfully appended.")

print("\nFinal content of output.txt:")
with open("output.txt", "r") as file:
    reading_file = file.read()
    print(reading_file)
