import os, psycopg2
from dotenv import load_dotenv

load_dotenv()

print(os.environ.get('DB_HOST'), os.environ.get('DB_NAME'), os.environ.get('DB_USER'))

conn = psycopg2.connect(
    host=os.environ.get('DB_HOST'),
    database=os.environ.get('DB_NAME'),
    user=os.environ.get('DB_USER'),
    password=os.environ.get('DB_PASSW')
)
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS users;')
cur.execute(
    'CREATE TABLE users ('
        'id SERIAL PRIMARY KEY,'
        'email VARCHAR(128) NOT NULL UNIQUE,'
        'password VARCHAR(128) NOT NULL,'
        'role INT NOT NULL DEFAULT 0,'
        'created_at TIMESTAMP DEFAULT NOW());'
)
cur.execute(
    "INSERT INTO users(email, password, role) VALUES"
    "('admin@gmail.com', sha256('admin123'), 1),"
    "('test@gmail.com', sha256('test123'), default),"
    "('test1@gmail.com', sha256('test1123'), default);"
)

conn.commit()
cur.close()
conn.close()
