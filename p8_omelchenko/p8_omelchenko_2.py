import math
try:
    a = float(input())
    b = float(input())
    c = float(input())
    d = b*b - 4*a*c
    if(d < 0): raise Exception("discriminant is less than 0, there are no roots")
    x1 = (-b + math.sqrt(d))/(2 * a)
    x2 = (-b - math.sqrt(d))/(2 * a)
    if(x2 == x1): 
        print("x = " + str(format(x1, ".2f")))
    else: 
        print("x1 = " + str(format(x1, ".2f")) + '\n' + ("x2 = " + str(format(x2, ".2f"))))
except ValueError: 
    print("Input is invalid, it should be 3 number")
except ZeroDivisionError: 
    print("There is zero devision error, 'a' should be not equal to zero")
    try:
        print("x = " + str(format(c/b, ".2f")))
    except ZeroDivisionError: 
        print("There is zero devision error, 'b' should be not equal to zero")
except Exception as exp:
    print(exp)

