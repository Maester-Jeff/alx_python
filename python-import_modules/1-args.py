import sys
def highlight_list(*argv):
    number_arguements = len(argv)
    if number_arguements == 0:
        print (number_arguements, "arguments.")
    elif number_arguements == 1:
        print (number_arguements, "argument:")
    else:
        print (number_arguements, "arguments:")
    for i, arg in enumerate(argv, 1):
        print(f"{i}: {arg}")
if __name__ == "__main__":
    arguements = sys.argv[1:]
