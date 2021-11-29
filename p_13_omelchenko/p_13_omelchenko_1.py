from collections import defaultdict
char_counter = defaultdict(int)
file = open("gadsby.txt", 'r')
text = file.readlines()
number_of_all_letters = 0
for line in text:
    line = line.lower()
    for char in line:
        if char.isalpha():
            char_counter[char] += 1
            number_of_all_letters += 1
sorted_char_counter = sorted(char_counter.items(), key = lambda x: x[1])
sorted_char_counter.reverse()
print(sorted_char_counter)
for i in range(0, 5):
    print(str(sorted_char_counter[i][0]) + " - " + str(round(sorted_char_counter[i][1]/number_of_all_letters*100, 3)) + " %")
print(".\n.\n.\n.")
for i in range(len(sorted_char_counter) - 5, len(sorted_char_counter)):
    print(str(sorted_char_counter[i][0]) + " - " + str(round(sorted_char_counter[i][1]/number_of_all_letters*100, 3)) + " %")
