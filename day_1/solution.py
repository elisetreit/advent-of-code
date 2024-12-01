import pandas as pd
from collections import Counter

# PART 1 SOLUTION
# Read in the data
list1 = []
list2 = []
with open('input.txt', "r") as file:
    for line in file.readlines():
        a = line.strip().split()
        list1.append(int(a[0]))
        list2.append(int(a[1]))

# I'm sure there is a smarter solution but... 
list1.sort()
list2.sort()
sum = 0
for i in range(0,len(list1)):
    sum += abs(list1[i] - list2[i])
print(f"The sum of the differences (Part 1 Solution) is {sum}")

# PART 2 SOLUTION

# Counter is super helpful for getting counts and is O(n) usually
counts_list1 = Counter(list1)
counts_list2 = Counter(list2)

similarity_index = 0
# we only need to add a value if it appears in both lists
# YAY SETS
keys = set(counts_list1.keys()).intersection(set(counts_list2.keys()))
for key in keys:
    # we just need to know the key value and the number of times it appears in each list
    # this allows for a "1 pass" solution so we don't need to revisit every value multiple times :)
    similarity_index += key * counts_list1[key] * counts_list2[key]

print(f"The similarity index (Part 2 Solution) is {similarity_index}")


