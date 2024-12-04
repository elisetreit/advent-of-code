import re
data = ""
with open('input.txt', "r") as file:
    data = file.read()

# PART 1
p = re.compile(r'mul\((\d*,\d*)\)')
matches = re.findall(p, data)
total = 0
for match in matches:
    a = match.split(",")
    total += int(a[0]) * int(a[1])

print(f"Total Score: {total} (Part 1)")

# PART 2

def get_score(chunk, pattern):
    total = 0
    matches = re.findall(pattern, chunk)
    for match in matches:
        a = match.split(",")
        total += int(a[0]) * int(a[1])
    return total

should_execute = True
remainder = data
total = 0
while ("do()" in remainder):
    next_command = re.search(r"do\(\)|don't\(\)", remainder).group()
    split = remainder.split(next_command, 1)
    remainder = split[1]
    if should_execute:
        total += get_score(split[0], p)
    if next_command == "do()":
        should_execute = True
    if next_command == "don't()":
        should_execute = False
if should_execute:
    total += get_score(remainder, p)

print(f"Total Score: {total} (Part 2)")