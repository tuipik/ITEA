# Создайте класс, описывающий автомобиль. Создайте класс автосалона, содержащий в себе список
# автомобилей, доступных для продажи, и функцию продажи заданного
# if автомобиля:

class Auto:
	def __init__(self, brand, model, year, fuel, engine_size, price):
		self.brand = brand
		self.model = model
		self.year = year
		self.fuel = fuel
		self.engine_size = engine_size
		self.price = price

	def __repr__(self):
		return f"<Automobile>:\n{self.brand} {self.model} {self.year}"


class Salon:
	def __init__(self):
		self.autos = []



car_1 = Auto('Toyota', 'Camry', 2018, 'Gasoline', 2000, 45000)
car_2 = Auto('VolksWagen', 'Passat', 2016, 'Diesel', 2200, 26000)
car_3 = Auto('Ford', 'Kuga', 2017, 'Gasoline', 1600, 20000)

print(car_1)