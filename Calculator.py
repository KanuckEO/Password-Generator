def Calculator():
    from time import sleep
    answer = 0
    no1 = int(input("First Number: "))
    no2 = int(input("Second Number: "))
    way = input("Choose the way to use those numbers (+ or - or * or /): ")

#functions
    def add():
        answer = no1 + no2
        print("The answer of", no1 ,"+", no2 ,"is", no1 + no2)



    def sub():
        print("The answer of", no1 ,"-", no2 ,"is", no1 - no2)
    def mul():
        print("The answer of", no1 ,"*", no2 ,"is", no1 * no2)
    def div():
        print("The answer of", no1 ,"/", no2 ,"is", no1 / no2) 

    print("Finding the answer")
    sleep(1)
    print(".")
    sleep(1)
    print(".")
    sleep(1)
    print(".")
    sleep(1)

    if way == '+':
        add()
    elif way == '-':
        sub()
    elif way == '*':
        mul()
    elif way == '/':
        div()   