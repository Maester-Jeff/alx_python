from sys import argv
if __name__ == "__main__":
  def highlight_list(*argv):
    num_args = len(argv)
    if num_args == 0:
      print(num_args, "arguments.")
    elif num_args == 1:
      print(num_args, "argument:")
    else:
      print(num_args, "arguments:")
    for i, arg in enumerate(argv, 1):
      print(f"{i}: {arg}")