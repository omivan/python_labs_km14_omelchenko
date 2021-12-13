import math

def c(n, k):
    return int((math.factorial(k))/((math.factorial(k-n))*(math.factorial(n))))

def binom(n):
    for i in range(n+1):
        my_list = [c(j, i) for j in range(i+1)]
        yield(my_list)
    

while True:
    try:
        n = int(input("input rang: "))
        if(n < 0): raise Exception
        break
    except:
        print("input is not valid")
    
for i in binom(n):
    for x in i:
        print(x, end=" ")
    print()