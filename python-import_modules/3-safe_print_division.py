def safe_print_division(a, b):
    try:
        output = a / b
    except ZeroDivisionError:
        print("Inside result: None")
        print("{} / {} = None".format(a, b))
    else:
        print("Inside result: {}".format(output))
    finally:
        return output if 'output' in locals() else None



''''

    finally:
        return result if 'result' in locals() else None
'''