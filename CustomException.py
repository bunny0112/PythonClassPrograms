class CustomError(Exception):
    pass

try:
    a = int(input("Enter the value of a: "))
    b = int(input("Enter the value of b: "))

    if b == 0:
        raise CustomError("Division by zero is not allowed.")
    else:
        print(a / b)

except CustomError as e:
    print("CustomError:", e)
#except ValueError:
 #   print("Please enter valid integer values for a and b.")