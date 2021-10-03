try:
    tornado_speed = int(input("Enter tornado speed(km/h) "))
    if(tornado_speed >= 0):
        if(tornado_speed <= 137): print("Minor")
        elif(tornado_speed <= 177): print("Moderate")
        elif(tornado_speed <= 217): print("Considerable")
        elif(tornado_speed <= 266): print("Severe")
        elif(tornado_speed <= 322): print("Devastating")
        else: print("Incredible")
    else:

     print("input is not valid, input should be more than 0")    
except:
    print("input is not valid")