num = int(input("enter a number:"))

if num < 0:
    print("Factorial cannot be calculated for negative numbers:")
else:
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
print("The factorial of",num,"is:", factorial)
