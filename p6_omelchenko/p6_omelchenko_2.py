index_map = {'Newfoundland' : 'A',
             'Nova Scotia' : 'B',
             'Prince Edward Island' : 'C',
             'New Brunswick' : 'E',
             'Quebec' : ('G', 'H', 'J'),
             'Ontario' : ('K', 'L', 'M', 'N', 'P'), 
             'Manitoba' : 'R', 
             'Saskatchewan' : 'S',
             'Alberta' : 'T', 
             'British Columbia' : 'V', 
             'Nunavut' : 'X', 
             'Northwest Territories' : 'X', 
             'Yukon' : 'Y'}
full_index = input("Input your index: ")
if(len(full_index) == 3):
    if(full_index[0].isalpha()):
        index_first_letter = full_index[0].upper()
    else:
        print("Input is invalid(first symbol should be the letter)")
        quit()
    if(full_index[1].isdigit()):
        index_number = int(full_index[1])
    else:
        print("Input is invalid(second symbol should be the number)")
        quit()
    if(full_index[2].isalpha()):
        index_last_letter = full_index[2].upper()
    else:
        print("Input is invalid(last symbol should be the letter)")
        quit()
else: 
    print("Input is invalid(should be 3 symbols)")
    quit()
flag = 0
for region, index in index_map.items():
    if index_first_letter == index:
        flag = 1
        print(region)
if(flag == 0): print("there is no region with this index")
elif index_number == 0: print("Countyside")
else: print("Urban area")
