
users = [("superuser", "123")]
cars = [
        ("Tracker","Chevrolet", "120"), 
        ("Onix","Chevrolet", "90"), 
        ("Spin","Chevrolet", "150"),
        ("HB20","Hyundai", "85"), 
        ("Tucson","Hyundai", "120"), 
        ("Uno","Fiat", "60"), 
        ("Mobi","Fiat", "70"), 
        ("Pulse","Fiat", "130")
        ]
rented = []

def login(name, senha):
    user = (name, senha)
    if user in users:
        return True
    else:
        return False

def add_car(name, mark, price):
    new_car = (name, mark, price)
    cars.append(new_car)

def remove_car():
    pass

def rent_car():
    pass

def return_car():
    pass




