with open("carsale.csv", "") as eff:

    class Inventory:

        def __init__(self, make, model, year, color, price, instock):
            self.make = make
            self.model = model
            self.year = year
            self.color = color
            self.price = price
            self.instock = instock
            self.instock = True

        def discount(self):
            if self.instock:
                self.price = self.price * 0.80
                print(f"After discount {self.model} now costs {self.price} ")
            else :
                self.instock = False
                print(f"{self.make} {self.model} {self.year} unavailable! ")

        def carcost(self):
            print(f"{self.make} {self.model} {self.year} costs ${self.price}!")

    ford = Inventory("Ford", "Mustang", 1999, "red", 230000, False)
    ford.carcost()
    ford.discount()
