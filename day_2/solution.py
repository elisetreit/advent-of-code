reports = []
with open('input.txt', "r") as file:
    for line in file.readlines():
        reports.append([int(a) for a in line.strip().split(" ")])

# PART 1 SOLUTION
report_num = len(reports)
min_step = 1
max_step = 3
step_range = range(min_step, max_step + 1)

def is_safe_part1(report):
    level_num = len(report)
    safety_diff_range = range(min_step * level_num-1, max_step * level_num + 1)
    level_range = range(0, level_num - 1)
    # we don't actually need to check all levels, if first and last levels have a difference greater than 3*level_num 
    # or difference less than level_num, it cannot be safe
    if abs(report[0] -report[level_num - 1]) in safety_diff_range:
        # now we can actually check if it is safe
        # case 1: increasing
        if report[0] < report[level_num - 1]:
            for i in level_range:
                if not(report[i+1] - report[i] in step_range):
                    return False
            # if we've gotten here, we know we haven't seen any unsafe conditions
            return True
        # case 2: decreasing
        else: 
            for i in level_range:
                if not(report[i] - report[i+1] in step_range):
                    return False
            return True        
    else:
        return False
safe_report_num = 0
for report in reports:
    safe_report_num += is_safe_part1(report)
print(f"There are {safe_report_num} safe reports (PART 1)")

# PART 2
# let's do this the dumb way

def is_safe_part2(report):
    removed_level = False
    level_num = len(report)
    valid_step = [1,2,3]
    # check to see if it is ascending
    if not(is_mostly_ascending(report, level_num)):
        # if not, reverse it so it is ascending
        report = list(reversed(report))
    level_num = len(report)
    valid_step = [1,2,3]
    skipped_level = False
    i = 0
    while (i < level_num):
        is_safe_i = is_safe_index(i, report, valid_step)
        if not(skipped_level) and not(is_safe_i):
            report.pop(i)
            level_num = len(report)
            skipped_level = True
            i = i-1
        elif skipped_level and not(is_safe_i):
            return False
        i = i+1
    return True

def is_mostly_ascending(report, level_num):
    if (report[1] < report[level_num -2]): 
        return True
    elif(report[2] < report[level_num - 1]):
        return True
    else:
        return False
    
def is_safe_index(index, report, valid_step):
    if (index == 0):
        if (report[1] - report[0]) in valid_step:
            return True
        elif(report[2] - report[0]) in valid_step:
            # this indicates that while index 2 is not valid, index 1 is valid
            return True
        else: 
            return False   
    else:
        # middle case
        return  (report[index] - report[index -1] in valid_step)
    
safe_report_num = 0
for report in reports:
    safe_report_num += is_safe_part2(report)
print(f"There are {safe_report_num} safe reports (PART 2)")