def no_c(my_string):
  output = ""
  for char in my_string:
    if char != "C" and char != "c":
       output = output + char
  return output
print(no_c("Character"))