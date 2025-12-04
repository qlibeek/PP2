from database import get_connection

def insert_from_console():
    first_name = input("First name: ")
    last_name = input("Last name: ")
    phone = input("Phone: ")
    conn = get_connection()
    with conn, conn.cursor() as cur:
        cur.execute(
            "INSERT INTO phonebook(first_name, last_name, phone) VALUES (%s, %s, %s)",
            (first_name, last_name, phone)
        )
    conn.close()

if __name__ == "__main__":
    insert_from_console()
