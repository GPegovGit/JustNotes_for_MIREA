class Service:
	id = None
	name = None
	address = None
	Phone = None
	manager = None

	def __init__(self, id: int, name: str, address: str, Phone: str, manager: str):
		self.id = id
		self.name = name
		self.address = address
		self.Phone = Phone
		self.manager = manager

class Part:
	id = None
	name = None
	price = None
	manufacturer = None

	def __init__(self, id: int, name: str, price: int, manufacturer: str):
		self.id = id
		self.name = name
		self.price = price
		self.manufacturer = manufacturer

class Model:
	id = None
	name = None
	brand_id = None
	model_year = None

	def __init__(self, id: int, name: str, brand_id: int, model_year: int):
		self.id = id
		self.name = name
		self.brand_id = brand_id
		self.model_year = model_year

class Car_brand:
	id = None
	name = None

	def __init__(self, id: int, name: str):
		self.id = id
		self.name = name

class Car:
	license_plate = None
	color = None
	estimated_value = None
	car_model_id = None

	def __init__(self, license_plate: str, color: str, estimated_value: int, car_model_id: int):
		self.license_plate = license_plate
		self.color = color
		self.estimated_value = estimated_value
		self.car_model_id = car_model_id









