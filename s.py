class Order_detail:
    def __init__(self, customer_info, items, shipping_address):
        self.customer_info = customer_info
        self.items = items
        self.shipping_address = shipping_address


class OrderCost:
    def __init__(self, tax_rate, discount):
        self.tax_rate = tax_rate
        self.discount = discount

    def calculate_total(self, cart):
        subtotal = sum(item.price for item in cart.items)

        subtotal = subtotal - (subtotal * self.discount)

        tax = subtotal * self.tax_rate
        return subtotal + tax
    

