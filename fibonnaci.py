import math
def isperfectsquare(num):
    s = int(math.sqrt(num))
    return s*s == num
def isfibonnaci(n):
    return isperfectsquare(5*n*n + 4) or isperfectsquare(5*n*n - 4)
number_1 = int(input("Enter a number you want to find out if it is fibonnaci or not: "))

if isfibonnaci(number_1) == True:
    print(number_1,"belongs to the fibonnaci sequence")
else:
    print(number_1,"does not belong to the fibonnaci sequence")

# just in case you dont want any user input
"""for i in range(1, 8):
    if isfibonnaci(i) == True:
      print(i," is fibonnaci")
   else:
      print(i,"is not fibonnaci")"""
