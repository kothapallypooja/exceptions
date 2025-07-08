#File Handling with Python

1. **File Reader**: Reads and prints the contents of a text file line-by-line.
2. **File Writer & Appender**: Allows user input to be written to a file and appended later.

## Features
- Read contents of a file and display them with line numbers
- Catch and handle file-not-found errors gracefully
- Write user input to a new file
- Append additional input to the same file
- Display final content of the modified file

## Installation
Make sure you have **Python 3.x** installed.
```bash
python --version
```
Then, clone this repository using:
```bash
git clone https://github.com/your-username/simple-file-handling.git
cd simple-file-handling
```

## How to Run

###  Reading from a File
1. Ensure you have a file named `sample.txt` in the same directory.
2. Run the script:
```bash
python file_reader.py
```
If `sample.txt` is not found, you'll see a user-friendly error message.
---

### Writing and Appending to a File
1. Run the script:
```bash
python file_writer_appender.py
```
2. Enter your desired text when prompted.
3. Additional text can be appended.
4. The final content of `output.txt` will be displayed
