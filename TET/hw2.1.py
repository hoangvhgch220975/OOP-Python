class Vehicle:
    def __init__(self, vehicle_id, brand, model, mileage):
        self.vehicle_id = vehicle_id
        self.set_brand(brand)
        self.set_model(model)
        self.update_mileage(mileage)

    def set_brand(self, brand):
        if not brand or not isinstance(brand, str):
            raise ValueError("Invalid brand")
        self.brand = brand

    def set_model(self, model):
        if not model or not isinstance(model, str):
            raise ValueError("Invalid model")
        self.model = model

    def update_mileage(self, mileage):
        if not isinstance(mileage, (int, float)) or mileage < 0:
            raise ValueError("Invalid mileage")
        self.mileage = mileage

    def show_info(self):
        print(f"Vehicle ID: {self.vehicle_id}")
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Mileage: {self.mileage} km")

# Test the class
try:
    # Creating Vehicle objects
    vehicle1 = Vehicle(vehicle_id=1, brand="Toyota", model="Camry", mileage=50000)
    vehicle2 = Vehicle(vehicle_id=2, brand="Honda", model="Civic", mileage=60000)

    # Displaying initial info
    print("Initial Information:")
    vehicle1.show_info()
    vehicle2.show_info()

    # Updating mileage
    vehicle1.update_mileage(55000)
    vehicle2.update_mileage(65000)

    # Displaying updated info
    print("\nUpdated Information:")
    vehicle1.show_info()
    vehicle2.show_info()

except ValueError as e:
    print(f"Error: {e}")
