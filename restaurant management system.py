import sys

class RestaurantManagementSystem:
    def __init__(self):
        self.menu = {}
        self.orders = []
        self.customers = {}
        self.inventory = {}

    # Menu Management
    def add_menu_item(self, item_name, price):
        self.menu[item_name] = price
        print(f"Added {item_name} to menu.")

    def update_menu_item(self, item_name, price):
        if item_name in self.menu:
            self.menu[item_name] = price
            print(f"Updated {item_name} in menu.")
        else:
            print(f"{item_name} not found in menu.")

    def delete_menu_item(self, item_name):
        if item_name in self.menu:
            del self.menu[item_name]
            print(f"Deleted {item_name} from menu.")
        else:
            print(f"{item_name} not found in menu.")

    # Order Management
    def create_order(self, customer_id, items):
        if customer_id not in self.customers:
            print("Customer not found.")
            return
        order_total = 0
        for item in items:
            if item in self.menu:
                order_total += self.menu[item]
            else:
                print(f"{item} not found in menu.")
        self.orders.append({"customer_id": customer_id, "items": items, "total": order_total})
        print(f"Order created for customer {customer_id}. Total: ${order_total:.2f}")

    # Customer Management
    def add_customer(self, customer_id, name, contact):
        self.customers[customer_id] = {"name": name, "contact": contact}
        print(f"Added customer {name}.")

    def update_customer(self, customer_id, name=None, contact=None):
        if customer_id in self.customers:
            if name:
                self.customers[customer_id]["name"] = name
            if contact:
                self.customers[customer_id]["contact"] = contact
            print(f"Updated customer {customer_id}.")
        else:
            print("Customer not found.")

    def delete_customer(self, customer_id):
        if customer_id in self.customers:
            del self.customers[customer_id]
            print(f"Deleted customer {customer_id}.")
        else:
            print("Customer not found.")

    # Inventory Management
    def add_inventory_item(self, item_name, quantity):
        self.inventory[item_name] = self.inventory.get(item_name, 0) + quantity
        print(f"Added {quantity} of {item_name} to inventory.")

    def update_inventory_item(self, item_name, quantity):
        if item_name in self.inventory:
            self.inventory[item_name] = quantity
            print(f"Updated inventory for {item_name}.")
        else:
            print(f"{item_name} not found in inventory.")

    def delete_inventory_item(self, item_name):
        if item_name in self.inventory:
            del self.inventory[item_name]
            print(f"Deleted {item_name} from inventory.")
        else:
            print(f"{item_name} not found in inventory.")

    # Billing and Payment
    def process_payment(self, order_id, amount_paid):
        if order_id < len(self.orders):
            order = self.orders[order_id]
            if amount_paid >= order["total"]:
                change = amount_paid - order["total"]
                print(f"Payment successful. Change: ${change:.2f}")
            else:
                print("Insufficient payment.")
        else:
            print("Order not found.")

# Example usage
if __name__ == "__main__":
    system = RestaurantManagementSystem()

    # Add menu items
    system.add_menu_item("Burger", 5.99)
    system.add_menu_item("Pizza", 8.99)

    # Add customer
    system.add_customer(1, "John Doe", "123-456-7890")

    # Create order
    system.create_order(1, ["Burger", "Pizza"])

    # Process payment
    system.process_payment(0, 15.00)