# Task 2: Write and Append Data to a File

filename = "output.txt"

# Step 1: Write user input to file
user_text = input("Enter text to write into the file: ")

with open(filename, "w") as file:
    file.write(user_text + "\n")

# Step 2: Append additional data
with open(filename, "a") as file:
    file.write("This is appended text.\n")

# Step 3: Read and show final content
print("\nFinal content of output.txt:")
with open(filename, "r") as file:
    print(file.read())
