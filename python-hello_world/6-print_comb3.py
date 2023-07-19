for a in range(10):
    for b in range(a+1,10):
        print("{}{}".format(a,b),end=", ")
    if a == 8:
        print("{}{}".format(a,b),end="\n")
