num1=int(input("Enter the first number:"))
num2=int(input("enter the second number:"))

if num1 % 2 == 1 and num2 % 2 == 1:
    sum_of_square = num1 ** 2 + num2 ** 2
    print("The sum of their square is:", "sum_of_squares")
else:
    print("sorry, the calculation cannot be performed because at least one number is even.")


