class House:
    def __init__(self, owner, address, bedrooms):
        self.owner = owner
        self.address = address
        self.bedrooms = bedrooms
        self.price = None
        self.sale = False
    def advertise(self):
        self.sale = True
    def sell(self,newOwner,lastPrice):
        if self.sale == True:
            self.owner = newOwner
            self.price = lastPrice
            self.sale = False
        else:
            raise Exception("The house is no longer for sale")

# Rob built a mansion with 6 bedrooms
mansion = House("Rob", "123 Fake St, Kensington", 6)

# Viv built a 3 bedroom bungalow
bungalow = House("Viv", "42 Wallaby Way, Sydney", 3)

# The bungalow is advertised for sale
bungalow.advertise()

# Hayden tries to buy the mansion but can't
try:
    mansion.sell("Hayden", 3000000)
except Exception:
    print("Hayden is sad")

# He settles for buying the Bungalow instead
bungalow.sell("Hayden", 1000000)