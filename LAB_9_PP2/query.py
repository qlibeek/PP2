from database import get_connection

def query_contacts():
    print("1) Найти по имени\n2) Найти по телефону\n3) Показать всех")
    choice = input("Выбор: ")
    conn = get_connection()
    with conn, conn.cursor() as cur:
        if choice == "1":
            name = input("Часть имени: ")
            cur.execute(
                "SELECT * FROM phonebook WHERE first_name ILIKE %s OR last_name ILIKE %s",
                (f"%{name}%", f"%{name}%")
            )
        elif choice == "2":
            phone = input("Часть телефона: ")
            cur.execute(
                "SELECT * FROM phonebook WHERE phone LIKE %s",
                (f"%{phone}%",)
            )
        else:
            cur.execute("SELECT * FROM phonebook")
        rows = cur.fetchall()
    conn.close()
    for r in rows:
        print(r)

if __name__ == "__main__":
    query_contacts()
