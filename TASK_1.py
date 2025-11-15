# Task 1: Read a File and Handle Errors

try:
    with open("sample.txt", "r") as file:
        print("File opened successfully!\n")
        for line in file:
            print(line.strip())
except FileNotFoundError:
    print("Error: The file 'sample.txt' does not exist.")
except Exception as e:
    print("An unexpected error occurred:", e)
