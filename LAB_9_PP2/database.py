import psycopg2
from config import load_config

def get_connection():
    config = load_config()
    return psycopg2.connect(**config)

if __name__ == '__main__':
    try:
        conn = get_connection()
        print("Connected to PostgreSQL.")
    except Exception as e:
        print("Ошибка подключения:", repr(e))
    finally:
        if 'conn' in locals():
            conn.close()

