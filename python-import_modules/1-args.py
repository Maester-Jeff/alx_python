if __name__ == "__main__":
    def highlight_list(*argv):
        number_argv = len(argv)
        if number_argv == 0:
            print (number_argv,'arguments.')
        elif number_argv == 1:
            print (number_argv, 'argument:')
        else:
            print (number_argv,'arguments:')
        for i, arg in enumerate(argv, 1):
            print("{}: {}".format(i, arg))
