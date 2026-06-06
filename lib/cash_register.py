
class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.previous_transactions = 0

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, discount):
        if 0 <= discount <= 100:
            self._discount = discount

    def add_item(self, item, price, quantity=1):
        self.total += price * quantity
        self.items.extend([item] * quantity)
        self.previous_transactions = price * quantity

    def apply_discount(self):
        if self.discount > 0:
            self.total = self.total * (1 - self.discount / 100)
            print(
                f"After the discount, the total comes to ${int(self.total)}."
            )
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        self.total -= self.previous_transactions