class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.adometer = 21

    def get_long_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name

    def read_adometer(self):
        print("汽车的里程为：" + str(self.adometer))

    def update_adometer(self, mileage):
        if mileage > self.adometer:
            self.adometer += mileage
        else:
            print("error")


my_car = Car('subaru', 'outback', 2013)
print(my_car.get_long_name())
my_car.read_adometer()
my_car.update_adometer(14)
my_car.read_adometer()



# 继承关系
class ElectricCar(Car):

    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()


    def describe_battery(self):
        print("这辆车还剩下" + str(self.battery) + "电量")


class Battery:
    def __init__(self, battery_size=80):
        self.battery_size = battery_size

    def describe_battery(self):
        print( "this car has a " + str(self.battery_size) + "- kmh battery")


other_car = ElectricCar('china', 'model s', 2020)
other_car.battery.describe_battery()
# print(other_car.get_long_name())
# other_car.describe_battery()





