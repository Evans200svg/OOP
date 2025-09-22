# Parent class
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def power_on(self):
        print(f"{self.brand} {self.model} is now ON.")

    def power_off(self):
        print(f"{self.brand} {self.model} is shutting down...")

# Child class 
class Smartphone(Device):
    def __init__(self, brand, model, os, storage):
        # Initialize parent attributes
        super().__init__(brand, model)
        # Add unique attributes
        self.os = os
        self.storage = storage
    
    def take_photo(self):
        print(f"{self.brand} {self.model} is taking a photo 📸")

    def install_app(self, app_name):
        print(f"Installing {app_name} on {self.brand} {self.model}...")

# objects
phone1 = Smartphone("Apple", "iPhone 15", "iOS", "256GB")
phone2 = Smartphone("Samsung", "Galaxy S24", "Android", "512GB")

phone1.power_on()
phone1.take_photo()
phone1.install_app("WhatsApp")
phone1.power_off()

phone2.power_on()
phone2.install_app("Spotify")
