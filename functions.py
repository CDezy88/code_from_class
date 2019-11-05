def product(a,b,c,d):
    return a * b * c * d


def add(a,b,c,d):
    return a + b + c + d


def main():
    num1, num2, num3, num4 = eval(input("Please enter 4 numbers of your choice seperated by commas: "))
    additionResult = (num1 + num2 + num3 + num4)
    productResult = (num1 * num2 * num3 * num4)
    subtractionResult = (num1 - num2 - num3 - num4)

    print("The result of your addition is", additionResult)
    print("The result of your multiplication is", productResult)
    print("The result of your subtraction is", subtractionResult)

main()

