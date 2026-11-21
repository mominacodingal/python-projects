def recur_factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * recur_factorial(n - 1)

num = int(input("Enter a number: "))
if num < 0:
    print("Sorry!factorial doesnt exist for negative numbers")
elif num == 0:
    print("Factorial of 0 is 1")
else:
    print(f"The factorial of {num} is {recur_factorial(num)}")
    
    
        
        