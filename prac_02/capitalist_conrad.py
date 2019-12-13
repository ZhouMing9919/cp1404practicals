import random


def main():
    MAX_INCREASE = 0.1
    MAX_DECREASE = 0.05
    MIN_PRICE = 0.01
    MAX_PRICE = 1000

    file_output = "output.txt"
    out_file = open(file_output, 'w')

    price = 10
    day = 0
    print("Starting price: $10.00", file=out_file)

    while MIN_PRICE <= price <= MAX_PRICE:

        day = day + 1

        if random.randint(1, 2) == 1:
            change = random.uniform(0, MAX_INCREASE)
        else:
            change = random.uniform(-MAX_DECREASE, 0)

        price = price * (change + 1)

        print("On day {}, the price is: ${:,.2f}".format(day, price), file=out_file)

    out_file.close()


main()
