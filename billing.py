from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os

def generate_receipt(customer_name, items, total_amount, filename):
    try:
        c = canvas.Canvas(filename, pagesize=letter)
        c.setFont("Helvetica", 12)
        c.drawString(50, 750, "Receipt")
        c.drawString(50, 730, "-----------------------------")
        c.drawString(50, 710, f"Customer Name: {customer_name}")
        y = 690
        for item, price in items.items():
            c.drawString(50, y, f"{item}: ${price:.2f}")
            y -= 20
        c.drawString(50, y - 20, "-----------------------------")
        c.drawString(50, y - 40, f"Total Amount: ${total_amount:.2f}")
        c.save()
        print("Receipt generated successfully!")
    except Exception as e:
        print(f"Error generating receipt: {e}")

def get_user_input():
    try:
        customer_name = input("Enter customer name: ").strip()
        items = {}
        num_items = int(input("Enter the number of items: "))
        for i in range(num_items):
            item_name = input(f"Enter name of item {i+1}: ").strip()
            item_price = float(input(f"Enter price of item {i+1}: "))
            items[item_name] = item_price
        total_amount = sum(items.values())
        filename = input("Enter filename for receipt (with .pdf extension): ").strip()
        if not filename.endswith('.pdf'):
            filename += '.pdf'
        return customer_name, items, total_amount, filename
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return get_user_input()
    except Exception as e:
        print(f"An error occurred: {e}")

def cal():
    print("Welcome to the receipt generator!")
    try:
        customer_name, items, total_amount, filename = get_user_input()
        generate_receipt(customer_name, items, total_amount, filename)
    except KeyboardInterrupt:
        print("\nReceipt generation cancelled.")
    except Exception as e:
        print(f"An error occurred: {e}")
cal()

