def divis():
    k = 0
    number = int(input("Add number to check divisibility: "))
    print("The number is", number)
    for x in range(2,number):    
        ans = number%x
        if ans == 0:
            print (number,  " is divisible by " , x)
            k = k + 1
    
    if k == 0:
        print("This number is not divisible by anything.")