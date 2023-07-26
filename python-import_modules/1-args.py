import sys
if __name__ == "__main__":
    argv = sys.argv[1:]
    def highlight_list(*argv):
        if len(argv) == 0:
            print(len(argv), "arguments.")
        elif len(argv) == 1:
            print(len(argv), "argument:")
        else:
            print(len(argv), "arguments:")
            for i, arg in enumerate(argv, 1):
                print(f"{i}: {arg}")