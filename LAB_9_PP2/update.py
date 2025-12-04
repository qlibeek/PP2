from database import get_connection

def update_by_phone():
    phone = input("Старый телефон: ")
    new_first_name = input("Новое имя (Enter, если не менять): ")
    new_last_name = input("Новая фамилия (Enter, если не менять): ")
    new_phone = input("Новый телефон (Enter, если не менять): ")

    fields = []
    values = []
    if new_first_name:
        fields.append("first_name = %s")
        values.append(new_first_name)
    if new_last_name:
        fields.append("last_name = %s")
        values.append(new_last_name)
    if new_phone:
        fields.append("phone = %s")
        values.append(new_phone)
    if not fields:
        print("Ничего не изменено")
        return

    values.append(phone)
    conn = get_connection()
    with conn, conn.cursor() as cur:
        cur.execute(
            f"UPDATE phonebook SET {', '.join(fields)} WHERE phone = %s",
            tuple(values)
        )
        print("Updated rows:", cur.rowcount)
    conn.close()

if __name__ == "__main__":
    update_by_phone()
