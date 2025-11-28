import psycopg2

try:
    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        dbname="suppliers",
        user="postgres",
        password="1234"
    )
    print("OK")
    conn.close()
except Exception as e:
    print("Error", repr(e))