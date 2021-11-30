import fileinput
from os import name
files = list()
for i in range(1880, 2020):
    files.append("yob" + str(i) + ".txt")
male_names = list()
female_names = list()
for f in files:
    file = open(f)
    male_flag = False
    female_flag = False
    text = file.readlines()
    for line in text:
        line = line.strip()
        line = line.split(',')
        if line[1] == 'M' and not male_flag:
                male_names.append(line[0])
                male_flag = True
        elif line[1] == 'F' and not female_flag:
                female_names.append(line[0])
                female_flag = True
male_names_set = set(male_names)
male_result = list()
for x in male_names_set:
    male_result.append([male_names.count(x), x])
male_result.sort()
male_result.reverse()
female_names_set = set(female_names)
female_result = list()
for x in female_names_set:
    female_result.append([female_names.count(x), x])
female_result.sort()
female_result.reverse()
for x in male_result:
    print(str(x[1]) + " " + str(x[0]))
print()
for x in female_result:
    print(str(x[1]) + " " + str(x[0]))

