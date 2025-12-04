import json
import psycopg2
from configparser import ConfigParser

# Загружаем конфигурацию из файла database.ini
def load_config(filename='database.ini', section='postgresql'):
    parser = ConfigParser()
    parser.read(filename, encoding='utf-8')
    config = {}
    if parser.has_section(section):
        items = parser.items(section)
        for item in items:
            config[item[0]] = item[1]
    return config

# Подключение к базе данных
def get_connection():
    config = load_config()
    return psycopg2.connect(**config)


# Функции и процедуры


def create_phonebook_table():
    conn = get_connection()
    try:
        with conn, conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS phonebook (
                    id SERIAL PRIMARY KEY,
                    first_name VARCHAR(50),
                    last_name VARCHAR(50),
                    phone VARCHAR(20) UNIQUE
                );
            """)
        conn.commit()
        print("щцуТаблица PhoneBook создана.")
    except Exception as e:
        print(f"Ошибка при создании таблицы: {e}")
    finally:
        conn.close()

# Функция поиска по шаблону
def search_by_pattern(pattern):
    conn = get_connection()
    try:
        with conn, conn.cursor() as cur:
            cur.execute("SELECT * FROM search_phonebook(%s)", (pattern,))
            rows = cur.fetchall()
        return rows
    except Exception as e:
        print(f"Ошибка при поиске: {e}")
    finally:
        conn.close()

# Процедура для добавления нового пользователя
def add_user(first_name, last_name, phone):
    conn = get_connection()
    try:
        with conn, conn.cursor() as cur:
            cur.execute("CALL add_user(%s, %s, %s)", (first_name, last_name, phone))
        conn.commit()
        print("✔ Контакт добавлен.")
    except Exception as e:
        print(f"Ошибка при добавлении пользователя: {e}")
    finally:
        conn.close()

# Процедура для добавления нескольких пользователей
def add_multiple_users(user_data):
    conn = get_connection()
    try:
        with conn, conn.cursor() as cur:
            json_data = json.dumps(user_data)  
            cur.execute("CALL add_multiple_users(%s)", [json_data]) 
        conn.commit()
        print("✔ Данные из нескольких контактов загружены.")
    except Exception as e:
        print(f"Ошибка при добавлении нескольких пользователей: {e}")
    finally:
        conn.close()

# Функция с пагинацией
def get_phonebook_page(limit, offset):
    conn = get_connection()
    try:
        with conn, conn.cursor() as cur:
            cur.execute("SELECT * FROM get_phonebook_page(%s, %s)", (limit, offset))
            rows = cur.fetchall()
        return rows
    except Exception as e:
        print(f"Ошибка при пагинации: {e}")
    finally:
        conn.close()

# Процедура для удаления записи по имени или телефону
def delete_user_by_phone_or_name(pattern):
    conn = get_connection()
    try:
        with conn, conn.cursor() as cur:
            cur.execute("CALL delete_user_by_phone_or_name(%s)", (pattern,))
        conn.commit()
        print("✔ Контакт удалён.")
    except Exception as e:
        print(f"Ошибка при удалении контакта: {e}")
    finally:
        conn.close()


# Основная программа


def menu():
    create_phonebook_table()
    while True:
        print("""
1) Добавить контакт с консоли
2) Загрузить несколько контактов
3) Поиск контактов по шаблону
4) Пагинация
5) Удалить контакт
0) Выход
""")
        choice = input("Выбор: ")
        if choice == "1":
            first_name = input("First name: ")
            last_name = input("Last name: ")
            phone = input("Phone: ")
            add_user(first_name, last_name, phone)
        elif choice == "2":
            user_data = [
                {"first_name": "John", "last_name": "Doe", "phone": "1234567890"},
                {"first_name": "Jane", "last_name": "Smith", "phone": "9876543210"}
            ]
            add_multiple_users(user_data)
        elif choice == "3":
            pattern = input("Введите шаблон для поиска: ")
            result = search_by_pattern(pattern)
            for r in result:
                print(r)
        elif choice == "4":
            limit = int(input("Введите лимит: "))
            offset = int(input("Введите смещение: "))
            result = get_phonebook_page(limit, offset)
            for r in result:
                print(r)
        elif choice == "5":
            pattern = input("Введите телефон или имя для удаления: ")
            delete_user_by_phone_or_name(pattern)
        elif choice == "0":
            print("Выход...")
            break
        else:
            print("Неверный выбор.")

if __name__ == "__main__":
    menu()

