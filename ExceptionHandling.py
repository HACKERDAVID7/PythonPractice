def DivideByZero(b, a=10):
    try:
        numerator = a
        denominator = b

        result = numerator/denominator

        print(result)
    except:
        print("Error: Denominator cannot be 0.")

    finally:
        print("This is finally block.")

def IndexOutOfBound():
    try:
    
        even_numbers = [2,4,6,8]
        print(even_numbers[5])

    except ZeroDivisionError:
        print("Denominator cannot be 0.")
    
    except IndexError:
        print("Index Out of Bound.")


def Reciprocal():
    # program to print the reciprocal of even numbers
    try:
        num = int(input("Enter a number: "))
        assert num % 2 == 0
    except:
        print("Not an even number!")
    else:
        reciprocal = 1/num
        print(reciprocal)


if __name__ == "__main__":
    # divide_numbers = 7 / 0
    # print(divide_numbers)

    # print(dir(locals()['__builtins__']))

    DivideByZero(0, 7)
    IndexOutOfBound()

    Reciprocal()


