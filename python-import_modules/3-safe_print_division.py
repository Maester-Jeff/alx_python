def safe_print_division(a, b):
    try:
        output = a / b
    except ZeroDivisionError:
        print("Inside result: {}".format("None"))
        print("{} / {} = None".format(a, b))
    else:
        print("Inside result: {}".format(output))
    finally:
        return print("{} / {} = {}".format(a, b, output))
