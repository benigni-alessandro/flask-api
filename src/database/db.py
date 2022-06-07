import psycopg2
from psycopg2 import DatabaseError
from decouple import config

def get_connection():
    try:
        return psycopg2.connect(
            host=config('PGSQL_HOST'),
            user=config('PGSQL_USER'),
            password=config('PGSQL_PASSWORD'),
            database=config('PGSQL_DATABASE'),
            port="5432"
        )
        
    except DatabaseError as ex:
        raise ex
# def create_table_footballer():
#     connection = get_connection()
#     cursor = connection.cursor()
#     query = """CREATE TABLE footballer (id SERIAL PRIMARY KEY, name varchar(30), role_id integer REFERENCES role , rarity_id integer REFERENCES rarity,Price integer, Quantity integer)"""
#     try:
#         cursor.execute(query)
#         print('Table created')
#         connection.commit()
#         insertar_jugador()
#     except:
#         print('Error')
   
# def create_table_role():
#     connection = get_connection()
#     cursor = connection.cursor()
#     query = """CREATE TABLE role (id SERIAL PRIMARY KEY, val varchar(30)"""
#     try:
#         cursor.execute(query)
#         print('Table created')
#         connection.commit()
#     except:
#         print('Error')

def insertar_roles():
    connection = get_connection()
    cursor = connection.cursor()
    n = cursor.lastrowid + 1
    query1 = f'''INSERT INTO role (val) VALUES('POR')'''
    query2 = f'''INSERT INTO role (val) VALUES('DIF')'''
    query3 = f'''INSERT INTO role (val) VALUES('CC')'''
    query4 = f'''INSERT INTO role (val) VALUES('ATT')'''
    cursor.execute(query1)
    cursor.execute(query2)
    cursor.execute(query3)
    cursor.execute(query4)
    connection.commit()

# def create_table_rarity():
#     connection = get_connection()
#     cursor = connection.cursor()
#     query = """CREATE TABLE rarity (id SERIAL PRIMARY KEY, valor varchar(30)"""
#     try:
#         cursor.execute(query)
#         print('Table created')
#         connection.commit()
#     except:
#         print('Error')
def insertar_rarities():
    connection = get_connection()
    cursor = connection.cursor()
    n = cursor.lastrowid + 1
    query1 = f'''INSERT INTO rarity (valor) VALUES('EPIC')'''
    query2 = f'''INSERT INTO rarity (valor) VALUES('LEGEND')'''
    query3 = f'''INSERT INTO rarity (valor) VALUES('RARE')'''
    cursor.execute(query1)
    cursor.execute(query2)
    cursor.execute(query3)
    connection.commit()


def insertar_jugador():
    connection = get_connection()
    cursor = connection.cursor()
    n = cursor.lastrowid + 1
    query1 = f'''INSERT INTO footballer (name, role_id, rarity_id, price, quantity) VALUES('andres', 3, 2, 30, 1)'''
    query2 = f'''INSERT INTO footballer (name, role_id, rarity_id, price, quantity) VALUES('alessandro', 1, 1, 10, 3)'''
    query3 = f'''INSERT INTO footballer (name, role_id, rarity_id, price, quantity) VALUES('edgar', 2, 3, 100, 1)'''
    query4 = f'''INSERT INTO footballer (name, role_id, rarity_id, price, quantity) VALUES('boh', 1, 2, 40, 2)'''
    cursor.execute(query1)
    connection.commit()
    cursor.execute(query2)
    connection.commit()
    cursor.execute(query3)
    connection.commit()
    cursor.execute(query4)
    connection.commit()
    

# create_table_footballer()

  
def create_tables(): 
    query1='''CREATE TABLE role (id SERIAL PRIMARY KEY, val varchar(30))'''
    query2='''CREATE TABLE rarity (id SERIAL PRIMARY KEY, valor varchar(30))'''
    query3='''CREATE TABLE footballer (id SERIAL PRIMARY KEY, name varchar(30), role_id integer REFERENCES role , rarity_id integer REFERENCES rarity,Price integer, Quantity integer)'''

    commands = []
    connection = None
    commands.append(query1)
    commands.append(query2)
    commands.append(query3)
    connection = get_connection()
    cursor = connection.cursor()
    try: 
        cursor.execute(query1)        
        connection.commit()
        cursor.execute(query2)        
        connection.commit() 
        cursor.execute(query3)        
        connection.commit()
        insertar_roles()
        insertar_rarities()
        insertar_jugador()
        
        
    except (Exception, psycopg2.DatabaseError) as error: 
        print(error) 
    finally: 
        if connection is not None: 
            connection.close() 
  
  

create_tables()