
from car import Car

if __name__ == '__main__':
    print('Hola mundo')
    car = Car()
    car.id = 884613265
    car.license = 'AMS234'
    car.driver = 'Andres Herrera'
    print(vars(car))

    car2 = Car()
    car2.license = 'QWE567'
    car2.driver= 'Angel Moreno'
    print(vars(car2))
