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
'''
from reportlab.lib.pagesizes import letter: This imports the letter size from the ReportLab library, which is commonly used for US letter-sized pages in PDF documents.
from reportlab.pdfgen import canvas: This imports the canvas module from ReportLab, which allows us to create PDF documents and draw various elements on them.
generate_receipt Function:

This function takes four parameters: customer_name, items, total_amount, and filename.
Inside the function:
It opens a canvas for drawing on a PDF with the specified filename.
Sets the font to "Helvetica" with a size of 12 points.
Draws the receipt title and separates it from the rest of the content with a horizontal line.
Writes the customer's name on the receipt.
Iterates through the items dictionary, drawing each item name and price on the receipt.
Draws another horizontal line to separate the items from the total amount.
Writes the total amount at the bottom of the receipt.
Saves the PDF file.
Prints a success message if the receipt is generated successfully.
It includes error handling using a try-except block to catch any exceptions that might occur during the generation process.
get_user_input Function:

This function prompts the user to input necessary details for the receipt generation.
It retrieves and returns the customer's name, item details (as a dictionary), total amount, and filename.
Error handling is implemented to ensure valid inputs and handle potential exceptions such as ValueError (e.g., when converting inputs to integers or floats).
cal Function:

This function serves as the main entry point of the program.
It welcomes the user and calls get_user_input to get the necessary information for receipt generation.
Then, it calls generate_receipt with the obtained information to create the receipt.
Error handling is implemented to catch any exceptions that might occur during the process, including KeyboardInterrupt (e.g., if the user interrupts the program).
Main Block:

The if __name__ == "__main__": block ensures that the cal function is called only if the script is executed directly (not imported as a module).
'''