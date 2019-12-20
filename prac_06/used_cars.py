from prac_06.car import Car


def main():
    """Demo test code to show how to use car class."""
    my_car = Car("my car", 180)
    my_car.drive(30)
    print("fuel =", my_car.fuel)
    print("odo =", my_car.odometer)
    print(my_car)

    print("{}, {}, {}".format(my_car.name, my_car.fuel, my_car.odometer))
    print("{self.name}, {self.fuel}, {self.odometer}".format(self=my_car))

    # 1.Create a new Car object called "limo" that is initialised with 100 units of fuel.
    limo = Car("limo", 100)
    # 2.Add 20 more units of fuel to this new car object using the add method.
    limo.add_fuel(20)
    # 3.Print the amount of fuel in the car.
    print(limo.fuel)
    # 4.Attempt to drive the car 115km using the drive method.
    limo.drive(115)
    # 5.Print the car's odometer reading.
    print(limo.odometer)


if __name__ == '__main__':
    main()
