# Odd or Even
print("-- CHECK TO SEE IF A NUMBER IS ODD OR EVEN --")
userNum = int(input("Enter a number: "))
if(userNum % 2) == 0: 
  print("{0} is an Even number".format(userNum))
else:
   print("{0} is an Odd number".format(userNum)) 




# ----------------------------------------------------------------  Extras  -------------------------------------------------------------------------------


# Is the number a mulitple of 4?
print("-- CHECK TO SEE IF A NUMBER IS A MULTIPLE OF 4 --")
n = int(input("Enter another number to check if it is a multiple of 4: "))
def isAMultipleOf4(n):
    if ((n & 3) == 0):
        return "This number IS a multiple of 4"
 
    return "This number IS NOT a multiple of 4"

if __name__ == "__main__":
 
    print (isAMultipleOf4(n))


# Do the numbers devide envenly?
print("-- CHECK TO SEE IF TWO NUMBERS DIVIDE EVENLY OR NOT --")
num = int(input("Enter first number: "))
check = int(input("Enter second number: "))
z = int(num % check)
if(z == 0):
  print("These numbers divide evenly")
else:
  print("These numbers do not divide evenly")