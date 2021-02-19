import car_class


def main():
    model_year = input("Enter the Car Year Model: ")
    make = input("Enter the car Make:")
    car = car_class.Car(model_year, make)
    accele(car)
    brake(car)


def accele(car):

    for count in range(1, 6):
        car.accelerate()
        print(car.get_speed())


def brake(car):
    for count in range(5):
        car.brake()
        print(car.get_speed())


main()