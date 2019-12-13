def main():
    try:
        numerator = int(input("Please enter the numerator: "))
        denominator = int(input("Please enter the denominator: "))

        while denominator == 0:
            denominator = int(input("Cannot divide by zero! Please enter another denominator: "))

        fraction = numerator / denominator
        print(fraction)

    except ValueError:
        print("Numerator and denominator must be valid numbers!")

    print("Finished.")


main()
