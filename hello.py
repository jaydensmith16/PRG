# factorial function limits
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
# Input and first function put into man function
def main():
    n = int(input("Enter a postitive integer: "))
    result = factorial(n)
    print("The factorial of", n, "is:", result)
# calling the main function
main()
