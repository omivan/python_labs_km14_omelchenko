def dec_to_hex(color):
    hex_num = []
    while True:
        remainder = int(color % 16)
        color = int(color / 16)
        if(remainder == 10): hex_num.append("A")
        elif(remainder == 11): hex_num.append("B")
        elif(remainder == 12): hex_num.append("C")
        elif(remainder == 13): hex_num.append("D")
        elif(remainder == 14): hex_num.append("E")
        elif(remainder == 15): hex_num.append("F")
        else: hex_num.append(remainder)
        if(color == 0): break
    hex_num.reverse()
    if(len(hex_num) < 2): hex_num.insert(0, 0)
    return hex_num

try:
    red_color = int(input("Enter index of red color: "))
    if(0 > red_color or red_color > 255): 
        print("Input is invalid. It is should be number in range of [0..255]")
        quit()
    green_color = int(input("Enter index of green color: "))
    if(0 > green_color or green_color > 255): 
        print("Input is invalid. It is should be number in range of [0..255]")
        quit()
    blue_color = int(input("Enter index of blue color: "))
    if(0 > blue_color or blue_color > 255): 
        print("Inputis invalid. It is should be number in range of [0..255]")
        quit()
    red_hex_num = dec_to_hex(red_color)
    green_hex_num = dec_to_hex(green_color)
    blue_hex_num = dec_to_hex(blue_color)

    final_hex_num = (red_hex_num + green_hex_num + blue_hex_num)
    print("Hex representation is: ")
    for x in final_hex_num:
      print(x, end="")
except:
    print("Input is not valid. It should be 3 numbers in range of [0..255]")

   
