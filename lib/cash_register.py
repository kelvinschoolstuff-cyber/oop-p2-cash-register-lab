#!/usr/bin/env python3


class CashRegister:
  def __init__(self, discount=0):
    self._discount = 0
    self.discount = discount
    self.total = 0
    self.items = []
    self.previous_transactions = []

  @property
  def discount(self):
    return self._discount

  @discount.setter
  def discount(self, value):
    if isinstance(value, bool) or not isinstance(value, int) or not 0 <= value <= 100:
      print("Not valid discount")
      return
    self._discount = value

  def add_item(self, item, price, quantity=1):
    """Add a purchase to the register and record it for later voiding."""
    self.total += price * quantity
    self.items.extend([item] * quantity)
    self.previous_transactions.append({
      "item": item,
      "price": price,
      "quantity": quantity,
    })

  def apply_discount(self):
    """Apply the configured percentage discount to the current total."""
    if not self.previous_transactions or self.total == 0:
      print("There is no discount to apply.")
      return

    self.total *= (100 - self.discount) / 100
    print(f"After the discount, the total comes to ${self.total:g}.")

  def void_last_transaction(self):
    """Remove the most recently added purchase from the register."""
    if not self.previous_transactions:
      print("There is no transaction to void.")
      return

    transaction = self.previous_transactions.pop()
    quantity = transaction["quantity"]
    self.total -= transaction["price"] * quantity
    del self.items[-quantity:]
