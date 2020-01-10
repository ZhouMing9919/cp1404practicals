from prac_08.unreliable_car import UnreliableCar


def main():
    """Test UnreliableCars."""

    # create cars with different reliabilities
    car1 = UnreliableCar("Car 1", 100, 90)
    car2 = UnreliableCar("Car 2", 100, 1)

    car1.drive(50)
    car2.drive(50)
    print(car1)
    print(car2)

    car1.drive(30)
    car2.drive(30)
    print(car1)
    print(car2)


main()
