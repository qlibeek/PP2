from database import get_connection

def delete_contact():
    print("1) Удалить по имени\n2) Удалить по телефону")
    choice = input("Выбор: ")
    conn = get_connection()
    with conn, conn.cursor() as cur:
        if choice == "1":
            name = input("Имя или часть имени: ")
            cur.execute(
                "DELETE FROM phonebook WHERE first_name ILIKE %s OR last_name ILIKE %s",
                (f"%{name}%", f"%{name}%")
            )
        else:
            phone = input("Телефон или часть телефона: ")
            cur.execute(
                "DELETE FROM phonebook WHERE phone LIKE %s",
                (f"%{phone}%",)
            )
        print("Deleted rows:", cur.rowcount)
    conn.close()

if __name__ == "__main__":
    delete_contact()
