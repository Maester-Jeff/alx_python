def List_args(*args):
    num_args = len(args)
    if num_args == 0:
        print(num_args, "arguements.")
    elif num_args == 1:
        print(num_args, "arguement:")
        print("{}: {}".format(num_args, args))
    else:
        print(num_args, "arguements:")
        for i, arg in enumerate(args, 1):
            print(f"{i}: {arg}")

# Test the function
List_args(1,4,5)



