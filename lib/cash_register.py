#!/usr/bin/env python3
# Building a cash register, add items, apply discounts and void prvious transactions

class CashRegister:
    def __init__(self, discount, total=0):
        self.discount = discount
        self.total = total
        self.items = []
        self.previous_transactions = []
    
    @property
    def discount(self):
        return self._discount
    @discount.setter
    def discount(self, discount: int):
        if  0 <= discount <= 100:
            self._discount = discount
        else:
            print("Not valid discount")

    def add_item(self, item, price, quantity):
      self.total += price * quantity
      self.items.append(item)

      self.previous_transactions.append({
            "item": item,
            "price": price,
            "quantity": quantity
        })


    def apply_discount(self):
      if len(self.previous_transactions) > 0:
        self.total = self.total * (1 - self.discount / 100)

        self.previous_transactions.pop()

        if len(self.items) > 0:
            self.items.pop()
        else:
           print("There is no discount to apply.")


    def void_previous_transaction(self):
        if len(self.previous_transactions) > 0:
            last_transaction = self.previous_transactions.pop()
            self.total -= last_transaction["price"] * last_transaction["quantity"]
        else:
            print("There are no previous transactions to void.")


register = CashRegister(10)

register.add_item("Apple", 10, 2)    # 20
register.add_item("Banana", 5, 4)    # 20

print(register.total)                # 40
print(register.items)                # ['Apple', 'Banana']

register.apply_discount()

print(register.total)                # 36.0
print(register.items)                # ['Apple']
print(register.previous_transactions)