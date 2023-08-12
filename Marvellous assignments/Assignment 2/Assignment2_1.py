
import Arithmetic

def main():
    print("Enter first number:")
    num1 = int(input())

    print("Enter second number:")
    num2 = int(input())

    add1 = Arithmetic.add(num1, num2)
    print("Addition is ", add1)

    sub1 = Arithmetic.sub(num1, num2)
    print("subtraction is", sub1)

    mult1 = Arithmetic.mult(num1, num2)
    print("Multiplication is", mult1)

    div1 = Arithmetic.div(num1,num2)
    print("division is", div1)


if __name__ == "__main__":
    main()
