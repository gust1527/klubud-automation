import sqlite3

def initialize_database():
    # Create a connection to the SQLite database
    conn = sqlite3.connect('product_mapping.db')
    cursor = conn.cursor()

    # Create the product_mapping table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS product_mapping (
            product_name TEXT PRIMARY KEY,
            file_path TEXT
        )
    ''')

    # Commit the changes and close the database connection
    conn.commit()
    conn.close()

def get_file_path(product_name):
    # Create a connection to the SQLite database
    conn = sqlite3.connect('product_mapping.db')
    cursor = conn.cursor()

    # Execute the SQL query to retrieve the file path
    cursor.execute('SELECT file_path FROM product_mapping WHERE product_name = ?', (product_name,))
    result = cursor.fetchone()

    # Close the database connection
    conn.close()

    if result:
        return result[0]
    else:
        # Default file path if product name is not found
        return None

def set_file_path(product_name, file_path):
    # Create a connection to the SQLite database
    conn = sqlite3.connect('product_mapping.db')
    cursor = conn.cursor()

    # Execute the SQL query to insert or update the file path
    cursor.execute('INSERT OR REPLACE INTO product_mapping (product_name, file_path) VALUES (?, ?)', (product_name, file_path))

    # Commit the changes and close the database connection
    conn.commit()
    conn.close()
