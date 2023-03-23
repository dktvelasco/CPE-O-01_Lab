file_name = input("Enter filename: ")
try:
    with open(file_name, 'r') as file:
        lines = file.readlines()
except FileNotFoundError:
    print(f"File {file_name} not found.")
    exit()
num_lines = len(lines)
