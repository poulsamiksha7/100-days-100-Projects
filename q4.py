# 4. Build a Product class for a shop:
#    Attributes: name, price, quantity
#    Methods:
#    - total_value() → price × quantity
#    - apply_discount(percent) → reduces price by percent
#    - is_available() → True if quantity > 0
#    Create 3 products, find the most expensive one

class Product():
    def __init__(self,name,price, quantity):
        self.name=name
        self.price=price
        self.quantity=quantity

    def total_value(self):
        return self.price*self.quantity
    def apply_discount(self,percent):
        discount_amount = self.price * percent / 100
        self.price -= discount_amount
        return self.price
    
    def is_available(self):
        if self.quantity>0:
            return True
        else:
            return False
p1=Product(name="ABC",price=45,quantity=1)
print(p1.total_value())
print(p1.apply_discount(10))
print(p1.is_available())
p2=Product(name="ABCD",price=450,quantity=12)
print(p2.total_value())
print(p2.apply_discount(5))
print(p2.is_available())
p3=Product(name="ABCDE",price=4500,quantity=1200)
print(p3.total_value())
print(p3.apply_discount(7))
print(p3.is_available())
if p1.price > p2.price and p1.price > p3.price:
    print(p1.name)
elif p2.price>p1.price and p2.price>p3.price:
    print(p2.name)
else:
    print(p3.name)
        