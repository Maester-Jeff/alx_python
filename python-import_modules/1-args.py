'''
import sys

if __name__ == "__main__":
    num_args = len(sys.argv) - 1

    print("Number of argument{}: {}".format('' if num_args == 1 else 's', num_args))

    if num_args == 0:
        print(":")
    else:
        print(":")

        for i, arg in enumerate(sys.argv[1:], start=1):
            print("{}: {}".format(i, arg))
'''
