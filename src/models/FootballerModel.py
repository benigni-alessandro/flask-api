from database.db import get_connection
from .entities.Footballer import Footballer
from flask import jsonify

class FootballerModel:
    @classmethod
    def get_footballers(self):
        try:
            connection = get_connection()
            footballers=[]
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM  footballer")
                resultset = cursor.fetchall()
                for row in resultset:
                    cursor.execute(f"SELECT * FROM  role WHERE id = {row[2]}")
                    role = cursor.fetchone()
                    cursor.execute(f"SELECT * FROM  rarity WHERE id = {row[3]}")
                    rarity = cursor.fetchone()
                    footballer = Footballer(row[0],row[1],role[1],rarity[1],row[4],row[5])
                    footballers.append(footballer.convert_to_json())
                connection.close()    
                return footballers
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def get_footballer(self, id):
        try:
            connection = get_connection()
            footballers=[]
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM  footballer WHERE id = %s", (str(id)))
                row = cursor.fetchone()
                footballer = None
                if row != None:
                    cursor.execute(f"SELECT * FROM  role WHERE id = {row[2]}")
                    role = cursor.fetchone()
                    cursor.execute(f"SELECT * FROM  rarity WHERE id = {row[3]}")
                    rarity = cursor.fetchone()
                    footballer = Footballer(row[0],row[1],role[1],rarity[1],row[4],row[5])   
                    footballer.convert_to_json()
                connection.close()    
                return footballer
        except Exception as ex:
            raise Exception(ex)


    @classmethod
    def add_footballer(self, nombre, role, rarity, precio, cantidad):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute('''INSERT INTO footballer (name, role_id, rarity_id, price, quantity) VALUES(%s, %s, %s, %s, %s)''',(nombre, role, rarity, precio, cantidad))
                affected_rows = cursor.rowcount
                connection.commit()
                connection.close()    
                return affected_rows
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def get_footballers_prices_disc(self):
        try:
            connection = get_connection()
            footballers=[]
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM  footballer ORDER BY price DESC")
                resultset = cursor.fetchall()
                for row in resultset:
                    cursor.execute(f"SELECT * FROM  role WHERE id = {row[2]}")
                    role = cursor.fetchone()
                    cursor.execute(f"SELECT * FROM  rarity WHERE id = {row[3]}")
                    rarity = cursor.fetchone()
                    footballer = Footballer(row[0],row[1],role[1],rarity[1],row[4],row[5])
                    footballers.append(footballer.convert_to_json())
                connection.close()    
                return footballers
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def get_footballers_prices_asc(self):
        try:
            connection = get_connection()
            footballers=[]
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM  footballer ORDER BY price ASC")
                resultset = cursor.fetchall()
                for row in resultset:
                    cursor.execute(f"SELECT * FROM  role WHERE id = {row[2]}")
                    role = cursor.fetchone()
                    cursor.execute(f"SELECT * FROM  rarity WHERE id = {row[3]}")
                    rarity = cursor.fetchone()
                    footballer = Footballer(row[0],row[1],role[1],rarity[1],row[4],row[5])
                    footballers.append(footballer.convert_to_json())
                connection.close()    
                return footballers
        except Exception as ex:
            raise Exception(ex)


    @classmethod
    def get_footballers_quantity_disc(self):
        try:
            connection = get_connection()
            footballers=[]
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM  footballer ORDER BY quantity DESC")
                resultset = cursor.fetchall()
                for row in resultset:
                    cursor.execute(f"SELECT * FROM  role WHERE id = {row[2]}")
                    role = cursor.fetchone()
                    cursor.execute(f"SELECT * FROM  rarity WHERE id = {row[3]}")
                    rarity = cursor.fetchone()
                    footballer = Footballer(row[0],row[1],role[1],rarity[1],row[4],row[5])
                    footballers.append(footballer.convert_to_json())
                connection.close()    
                return footballers
        except Exception as ex:
            raise Exception(ex)


    @classmethod
    def get_footballers_quantity_asc(self):
        try:
            connection = get_connection()
            footballers=[]
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM  footballer ORDER BY quantity ASC")
                resultset = cursor.fetchall()
                for row in resultset:
                    cursor.execute(f"SELECT * FROM  role WHERE id = {row[2]}")
                    role = cursor.fetchone()
                    cursor.execute(f"SELECT * FROM  rarity WHERE id = {row[3]}")
                    rarity = cursor.fetchone()
                    footballer = Footballer(row[0],row[1],role[1],rarity[1],row[4],row[5])
                    footballers.append(footballer.convert_to_json())
                connection.close()    
                return footballers
        except Exception as ex:
            raise Exception(ex)
    
    
    
    @classmethod
    def get_footballers_role(self, roles):
        try:
            connection = get_connection()
            footballers=[]
            with connection.cursor() as cursor:
                for role in roles:
                    cursor.execute(f"SELECT * FROM  footballer WHERE footballer.role_id = {role}")
                    resultset = cursor.fetchall()
                    for row in resultset:
                        cursor.execute(f"SELECT * FROM  role WHERE id = {row[2]}")
                        role = cursor.fetchone()
                        cursor.execute(f"SELECT * FROM  rarity WHERE id = {row[3]}")
                        rarity = cursor.fetchone()
                        footballer = Footballer(row[0],row[1],role[1],rarity[1],row[4],row[5])
                        footballers.append(footballer.convert_to_json())
                connection.close()
                return footballers    
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_footballers_rarity(self, rarities):
        try:
            connection = get_connection()
            footballers=[]
            with connection.cursor() as cursor:
                for rarity in rarities:
                    cursor.execute(f"SELECT * FROM  footballer WHERE footballer.rarity_id = {rarity}")
                    resultset = cursor.fetchall()
                    for row in resultset:
                        cursor.execute(f"SELECT * FROM  role WHERE id = {row[2]}")
                        role = cursor.fetchone()
                        cursor.execute(f"SELECT * FROM  rarity WHERE id = {row[3]}")
                        rarity = cursor.fetchone()
                        footballer = Footballer(row[0],row[1],role[1],rarity[1],row[4],row[5])
                        footballers.append(footballer.convert_to_json())
                connection.close()
                return footballers    
        except Exception as ex:
            raise Exception(ex)


    