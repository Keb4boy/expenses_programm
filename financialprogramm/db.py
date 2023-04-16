import psycopg2
import dotenv
import os


dotenv.load_dotenv()

def connection():

    conn = psycopg2.connect(dbname=os.environ.get('database'), 
                            host=os.environ.get('host'), 
                            password=os.environ.get('password'), 
                            port=os.environ.get('port'),
                            user=os.environ.get('user')
    )
    return conn


def make_tables():
    conn = connection()
    cur = conn.cursor()

    cur.execute("""CREATE TABLE categories (
        id bigint PRIMARY KEY GENERATED ALWAYS AS IDENTITY, 
        category varchar(255))"""
        )

    cur.execute("""CREATE TABLE names (
        id bigint PRIMARY KEY GENERATED ALWAYS AS IDENTITY, 
        name varchar(255))"""
        )

    cur.execute("""CREATE TABLE finance (
        id bigint PRIMARY KEY GENERATED ALWAYS AS IDENTITY, 
        name_id bigint REFERENCES names (id), 
        category_id bigint REFERENCES categories (id), 
        date date, 
        amount numeric)"""
        )

    conn.commit()
    conn.close()


def insert_categories(value):
    
    conn = connection()
    cur = conn.cursor()
    cur.execute(f"INSERT INTO categories (category) VALUES (%s)", [value])
    conn.commit()
    conn.close()


def insert_names(value):
    
    conn = connection()
    cur = conn.cursor()
    cur.execute(f"INSERT INTO names (name) VALUES (%s)", [value])
    conn.commit()
    conn.close()
    

def insert_all(name_id, category_id, date, amount):

    conn = connection()
    cur = conn.cursor()
    cur.execute(f"INSERT INTO finance (name_id, category_id, date, amount) VALUES (%s, %s, %s, %s)", [name_id, category_id, date, amount])
    conn.commit()
    conn.close()


def select_finance():

    conn = connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM finance")
    records = cur.fetchall()
    conn.close()

    return records

    


