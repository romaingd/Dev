# Process:
#       - Read the file
#       - Convert each line to an integer input
#       - Return the sum of all lines

with open('input.txt', 'r') as input:
    lines = input.readlines()
    num_lines = list(map(int, lines))
    result = sum(num_lines)

print(result)