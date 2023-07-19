'''
def getSortedNumber(number):
    number = sorted(number)
    number = int(str(number))
for number in range(100):
    print("{:02}".format(number),end=", ")
if number == 99:
    print("{:02}".format(number),end="")
'''

for number in range(100):
  if number == 99:
    print("{:02}".format(number),end=" ")
  else:
    print("{:02}".format(number),end=", ")
    

    


 