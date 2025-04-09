class Car:
    def __init__(self, car_brand, car_model, car_price, car_color, manifacture_year):
        self.car_brand=car_brand
        self.car_model=car_model
        self.car_price=car_price
        self.car_color=car_color
        self.manifacture_year=manifacture_year


    def display_info(self):
        print(f"{self.car_brand}, {self.car_model}, {self.car_price}, {self.car_color}, {self.manifacture_year}")

    
cars_list=[
    Car("Ford", "Fiesta", 1500, "blue", 2003),
    Car("Ford", "Focus", 13000, "grey", 2013),
    Car("Ford", "CMax", 19000, "black", 2016),
    Car("Opel", "Astra", 6000, "green", 2005),
    Car("Mazda", "6", 25000, "red", 2017),
    Car("Shkoda", "Octavia", 40000, "blue", 2019),
    Car("Toyta", "Supra", 3000, "black", 2008)
    ]

def sort_price(cars_list):
    sorted_cars = sorted(cars_list, key=lambda x: x.car_price, reverse=True)
    return sorted_cars

def list_by_brand(cars_list, car_brand):
    cars_by_brand = [car for car in cars_list if car.car_brand == car_brand]
    return cars_by_brand

def search_color(cars_list, car_color):
    expensive_car = max((car for car in cars_list if car.car_color == car_color), key=lambda x: x.car_price, default=None)
    return expensive_car

def newest_cars(cars_list):
    new_cars = [car for car in cars_list if car.manifacture_year > 2020]
    return new_cars
