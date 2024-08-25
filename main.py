# Jeremy Clark
# Codecademy Furniture Store Receipts
# 2024-08-25


salesTax = 0.088

class Product:

    def __init__(self, name):
        self.name = name

    def __init__(self, name, category, material, height, width, depth, color, price):
        self.name = name
        self.category = category
        self.material = material
        self.height = height
        self.width = width
        self.depth = depth
        self.color = color
        self.price = price

    def get_price(self):
        return self.price

    def set_price(self):
        while True:
            try:
                newPrice = input("What is the new price of " + self.name + "?: ")
                if newPrice.isnumeric():
                    self.price = newPrice
                    break
                else:
                    raise TypeError
            except TypeError:
                print("Please only enter numeric values")
                continue

    def productDescription(self):
        dString = "The " + self.name + " is crafted from " + self.material + " It stands " + str(self.height) + \
                  " inches tall, by " + str(self.width) + " inches wide and " + str(self.depth) + \
                  " inches deep. Availble in " + self.color + " Starting at $" + str(self.price) + "\n"
        return dString


LovelyLoveseat = Product("Lovely Loveseat", "Furniture", "Tufted polyester blend on wood.", 32, 40, 30, "Red or White.", 400)
StylishSettee = Product("Stylish Settee", "Furniture", "Faux leather on birch.", 29.50, 54.75, 28, "Black.", 599)
LuxuriousLamp = Product("Luxurious Lamp", "Decor", "Glass and iron.", 36, 8, 8, "Brown with cream shade. ", 53)


class Customer:

    def __init__(self, name):
        self.name = name
        self.itemization = []
        self.subTotal = float(0.00)
        self.sTax = 0.00
        self.Total = 0.00

    def add_item(self, item, qty):
        cost = float(qty) * float(item.price)
        entry = [item.name, qty, item.price, cost]
        self.itemization.append(entry)
        self.subTotal += cost
        self.sTax = round(self.subTotal * salesTax, 2)
        self.Total = round(self.subTotal + self.sTax, 2)

    def print_cart(self):
        print(self.name)
        print("========================")
        print("\nItemization:\n")
        for i in self.itemization:
            print(i[0], "\t$", i[3])
        print("\n SubTotal: \t\t\t$"+str(self.subTotal))
        print(" Tax: \t\t\t\t$" + str(self.sTax))
        print(" Total: \t\t\t$" + str(self.Total), "\n")


Customer1 = Customer("Shina Nagains")
Customer2 = Customer("Fae Kai Dentidee")

def main():
    print(LovelyLoveseat.color)
    print("The price of Lovely Loveseat is $" + str(LovelyLoveseat.get_price()) + ".")
    LovelyLoveseat.set_price()
    print("The price of Lovely Loveseat is $" + str(LovelyLoveseat.get_price()) + ".")
    print(LovelyLoveseat.productDescription())
    Customer1.add_item(LovelyLoveseat, 2)
    Customer1.add_item(LuxuriousLamp, 1)
    Customer2.add_item(StylishSettee, 3)
    Customer1.print_cart()
    Customer2.print_cart()



main()
