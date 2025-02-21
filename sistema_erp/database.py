from pathlib import Path
import sqlite3
from typing import List
from classes.Customer import Customer
from classes.DBResults import DBResults

class Database_ERP:
    def __init__(self, name="erp.db") -> None:
        self.name = name
        self.database = self.create_db_path()
        self.create_table()
    
    def connect(self):
        self.connection = sqlite3.connect(self.database)
    
    def close_connection(self):
        try:
            self.connection.close()
        except Exception as e:
            print(e)


    def create_db_path(self):
        database_folder = Path.joinpath(Path(__file__).parent,'data')

        if not database_folder.exists():
            Path.mkdir(database_folder)

        return Path.joinpath(database_folder, self.name).as_posix()

    def create_table(self):
        try:
            self.connect()

            cursor = self.connection.cursor()

            cursor.execute("""
                            CREATE TABLE IF NOT EXISTS Customers(
                                ID_CUSTOMER INTEGER PRIMARY KEY AUTOINCREMENT,
                                NAME TEXT,
                                PHONE TEXT,
                                CITY TEXT
                           )
                            """)
            
        except Exception as e:
            print(e)
        finally:
            self.close_connection()

    def register_customer(self, customer: Customer):

        table_fields = (
                'NAME',
                'PHONE',
                'CITY'
            )

        values_for_query = ("?,?,?")

        values = tuple(
                (
                    customer.name,
                    customer.phone,
                    customer.city
                )
            )
        
        try:
            self.connect()

            cursor = self.connection.cursor()
            cursor.execute(f"""INSERT INTO Customers {table_fields} VALUES ({values_for_query})""", values)

            self.connection.commit()
            
            result = DBResults(type="OK", msg="Cliente cadastrado com sucesso!")
            return result

        except sqlite3.IntegrityError as e:
            result = DBResults(type="ERROR", msg="Cliente já cadastrado")

            self.connection.rollback()

            return result
            
        except Exception as e:
            print(e)

            result = DBResults(type="ERROR", msg="Falha no processo de cadastro do cliente.")
            self.connection.rollback()
            return result

        finally:
            self.close_connection()

    def select_all_customers(self) -> List[Customer]:
        try:
            self.connect()

            cursor = self.connection.cursor()
            cursor.execute("""SELECT * FROM Customers ORDER BY NAME""")

            customers_result = cursor.fetchall()
            customers = List[Customer] = []

            for customer in customers_result:
                c = Customer(
                    name=customer[0],
                    phone=customer[1],
                    city=customer[2]
                )

                customers.append(c)
            
            return customers
        
        except Exception as e:
            print(e)
            return None
        finally:
            self.close_connection()
