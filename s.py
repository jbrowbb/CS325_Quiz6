class OrderDetail:
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
    

class OrderValidation:
    def __init__(self, inventory):
        self.inventory = inventory
    
    def validate_order(self, order_details):
        for item in order_details.items:
            if item not in self.inventory:
                return False
            
        return True
    

class OrderConfirmation:
    def send_email_confirmation(self, order_details):
        customer_email = order_details.customer_info["email"]       # gets customer email address

        body = "Dear {customer_info.firstName},\n\nYour order has been successfully processed. Thank you for shopping with us!"

        print(f"Sending order confirmation email to: {customer_email}")
        print("Email body:")
        print(body)


class InventoryUpdate:
    def __init__(self, inventory_database):
        self.inventory_database = inventory_database

    def update_inventory(self, order_details):
        for item in order_details.items:
            self.items.remove(item)