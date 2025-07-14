n = int(input("Enter Number: "))
sum = 0
for i in range(n+1):
  sum += i**2
print("Sum of squares of first {} natural numbers: ".format(n), sum)
