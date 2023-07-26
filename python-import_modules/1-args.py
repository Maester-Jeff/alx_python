if __name__ == "__main__":
    def highlight_list(*argv):
        if len(argv) == 0:
            print (len(args),'arguments.')
        elif len(argv) == 1:
            print (len(argv), 'argument:')
        else:
            print (len(argv),'arguments:')
        for i, arg in enumerate(argv, 1):
            print("{}: {}".format(i, arg))
