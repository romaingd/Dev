# Process:
#       - Read the file
#       - Convert each line to an integer input
#       - Return the sum of all lines

with open('input.txt', 'r') as input:
    lines = input.readlines()
    num_lines = list(map(int, lines))

num_lines = [+7, +7, -2, -7, -4]

n = len(num_lines)
sum_list = []

count = 0
COUNT_MAX = 1000
while (count < COUNT_MAX):
    print(count)
    for i in range(n):
        sum_list = list(map(lambda x: x + num_lines[i], sum_list + [0]))
        try:
            start = sum_list.index(0)
            stop = count * n + i
            count = COUNT_MAX
            break
        except:
            pass
    count += 1

result = 0
for i in range(start):
    result += num_lines[i % n]

check = 0
for j in range(stop + 1):
    check += num_lines[j % n]

print(start, stop)
print(result, check)