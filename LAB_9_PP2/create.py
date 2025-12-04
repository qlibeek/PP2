from database import get_connection

def create_table():
    conn = get_connection()
    with conn, conn.cursor() as cur:
        cur.execute("""
            CREATE TABLE IF NOT EXISTS phonebook (
                id SERIAL PRIMARY KEY,
                first_name VARCHAR(50),
                last_name VARCHAR(50),
                phone VARCHAR(20) UNIQUE
            )
        """)
    conn.close()

if __name__ == "__main__":
    create_table()
