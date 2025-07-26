import datetime

print("------YourChoice ------")

# -------------------- Classes --------------------

class Customer:
    def __init__(self, name, email, address, phone_number):
        self.name = name
        self.email = email
        self.address = address
        self.phone_number = phone_number

    def show(self):
        print(f"Name : {self.name}")
        print(f"Email :  {self.email}")
        print(f"Address : {self.address}")
        print(f"Phone number : {self.phone_number}")


class Menu:
    def __init__(self, name, description, price, category, availability):
        self.name = name
        self.description = description
        self.price = price
        self.category = category
        self.availability = availability

    def show(self):
        print(f"Name : {self.name}")
        print(f"Description : {self.description}")
        print(f"Price  : ₹{self.price}")
        print(f"Category  : {self.category}")
        print(f"Availability : {self.availability}")


class Category:
    def __init__(self, name, description=""):
        self.name = name
        self.description = description
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def list_items(self):
        return self.items


class Cart:
    def __init__(self, customer):
        self.customer = customer
        self.items = {}
        self.created_time = datetime.datetime.now()
        self.total_price = 0

    def add_item(self, item, quantity=1):
        if item.availability:
            if item in self.items:
                self.items[item] += quantity
            else:
                self.items[item] = quantity
            self.calculate_total()
        else:
            print(f"{item.name} is currently unavailable.")

    def calculate_total(self):
        total = sum(item.price * quantity for item, quantity in self.items.items())
        self.total_price = total

    def show_cart(self):
        print("\n--- Cart Summary ---")
        for item, qty in self.items.items():
            print(f"{item.name} × {qty} = ₹{item.price * qty}")
        print(f"Total Price: ₹{self.total_price}")


class Order:
    order_counter = 1

    def __init__(self, customer, items, total_price):
        self.order_id = Order.order_counter
        Order.order_counter += 1
        self.customer = customer
        self.items = items.copy()
        self.total_price = total_price
        self.status = "Pending"
        self.created_time = datetime.datetime.now()

    def update_status(self, new_status):
        self.status = new_status

    def view_order(self):
        print(f"\nOrder ID: {self.order_id}")
        print(f"Customer: {self.customer.name}")
        print(f"Status: {self.status}")
        print(f"Created: {self.created_time.strftime('%Y-%m-%d %H:%M:%S')}")
        print("Items:")
        for item, qty in self.items.items():
            print(f" - {item.name} × {qty} = ₹{item.price * qty}")
        print(f"Total Price: ₹{self.total_price}")

    def payment(self):
      while True:
        print("\n--- Payment Section ---")
        print("Available methods: Cash / Card")
        method = input("Enter a payment method: ").strip().capitalize()

        if method == 'Cash':
            print("Payment received in cash.")
            self.update_status("Paid - Cash")
            break

        elif method == 'Card':
            card_number = input("Enter your card number (16 digits): ").strip()
            if len(card_number) == 16 and card_number.isdigit():
                print("Card payment successful.")
                self.update_status("Paid - Card")
                break
            else:
                print("Invalid card number. Payment failed.")
        else:
            print("Unsupported payment method. Please choose Cash or Card.")

        # Ask if customer wants to try again
        retry = input("Do you want to try again? (yes/no): ").strip().lower()
        if retry != 'yes':
            print("Payment not completed. You can try again later.")
            break

 

def main():
    # Customer input
    name = input("Enter a name: ")
    email = input("Enter an email: ")
    address = input("Enter an address: ")
    phone_number = input("Enter a phone number: ")

    customer = Customer(name, email, address, phone_number)
    customer.show()

    # Items data
    Items = {
        'name': ["Paneer Tikka", "Veg Manchurian", "Butter Naan", "Dal Makhani", "Gulab Jamun", "Ice Cream"],
        'description': [
            'Grilled cottage cheese cubes marinated in spicy yogurt mix',
            'Crispy vegetable balls tossed in a tangy Indo-Chinese sauce',
            'Soft Indian flatbread brushed with melted butter',
            'Creamy black lentils slow-cooked with spices and butter',
            'Sweet milk dumplings soaked in sugar syrup',
            'Frozen dessert available in vanilla or chocolate flavor'
        ],
        'price': [180, 160, 40, 150, 60, 70],
        'Category': ['Starter', 'Starter', 'Main Course', 'Main Course', 'Dessert', 'Dessert'],
        'availability': [True, True, True, True, False, True]
    }

    # Create Menu objects
    menu_items = []
    for i in range(len(Items['name'])):
        item = Menu(
            Items['name'][i],
            Items['description'][i],
            Items['price'][i],
            Items['Category'][i],
            Items['availability'][i]
        )
        menu_items.append(item)

    # Display menu
    print("\n--- Menu ---")
    for item in menu_items:
        item.show()
        print("-" * 30)

    # Create cart and add items
    cart = Cart(customer)
    print("\nAdd items to cart:")
    for item in menu_items:
        choice = input(f"Do you want to add {item.name}? (yes/no): ").strip().lower()
        if choice == 'yes':
            qty = int(input(f"Enter quantity for {item.name}: "))
            cart.add_item(item, qty)

    cart.show_cart()

    # Place order
    order = Order(customer, cart.items, cart.total_price)
    order.view_order()
    order.payment()



    print("\nThank you for visiting *YourChoice*! We hope to serve you again soon.")

# Run the program
if __name__ == "__main__":
    main()