class Vechile:
    brand = None
    model = None
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

x = hasattr(Vechile,'brand')
print(x)


v1 = Vechile('bajaj','auto')

theBrand = getattr(Vechile, 'brand')
print("Brand: ", theBrand)

setattr(v1, 'color', 'white')

print(v1.__dict__)