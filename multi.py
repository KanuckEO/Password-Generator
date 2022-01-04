def multi():
    multi1 = int(input("Put in the Number you would like to see the multiplication tables of: "))

    for multi2 in range (1,11):
        ans = multi1 * multi2
        print(multi1, "x", multi2, "=", ans)