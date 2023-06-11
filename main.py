from woocommerce_handler import retrieve_orders
from excel_handler import append_orders_to_excel
from db_handler import get_file_path, set_file_path

def main():
    product_name = input("Enter the product name: ")
    display_value = input("Enter the display value (DD/MM/YY @ HH:MM - HH:MM): ")

    file_path = get_file_path(product_name)

    if file_path is None:
        file_path = input("Enter the file path to save the file: ")
        set_file_path(product_name, file_path)
    else:
        print("File path found in the database.")

    orders = retrieve_orders(product_name, display_value)
    append_orders_to_excel(product_name, file_path, orders)

if __name__ == "__main__":
    main()
