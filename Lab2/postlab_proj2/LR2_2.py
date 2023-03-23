file_name = input("Enter filename: ")
try:
    with open(file_name, 'r') as file:
        lines = file.readlines()
except FileNotFoundError:
    print(f"File {file_name} not found.")
    exit()
num_lines = len(lines)

print(f"The file {file_name} contains {num_lines} lines.")
while True:
    line_num = input(f"Enter a line number (1 to {num_lines}, or 0 to quit): ")

    if line_num == '0':
        break
    try:
        line_num = int(line_num)
