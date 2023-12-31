#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        output = a / b
    except ZeroDivisionError:
        print("Inside result: {}".format("None"))
    else:
        print("Inside result: {}".format(output))
    finally:
        return output if 'output' in locals() else None
