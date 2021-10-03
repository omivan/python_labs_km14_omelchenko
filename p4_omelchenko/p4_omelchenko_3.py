try:
    calendar_years = int(input("Enter calendar years "))
    dog_years = 0.0
    if(calendar_years >= 0):
        for i in range(1, calendar_years + 1, 1):
            if(i == 1 or i == 2): 
                dog_years += 10.5
            else: 
                dog_years += 4.0
        print("Dog years " + str(dog_years))
    else: print("input is not valid, input should be more than 0")
   
except: 
    print("input is not valid")
    