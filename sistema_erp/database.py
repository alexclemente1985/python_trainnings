from pathlib import Path
import sqlite3
from typing import List
from classes.Customer import Customer
from classes.DBResults import DBResults
import pandas as pd

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
            customers: List[Customer] = []

            for customer in customers_result:
                c = Customer(
                    id_customer=customer[0],
                    name=customer[1],
                    phone=customer[2],
                    city=customer[3]
                )

                customers.append(c)

            return customers

        except Exception as e:
            print(e)
            return None
        finally:
            self.close_connection()

    def delete_customer(self, id_customer):
        try:
            self.connect()
            cursor = self.connection.cursor()
            cursor.execute(f"""DELETE FROM Customers WHERE ID == '{id_customer}'""")
            self.connection.commit()

            return DBResults(type='OK', msg='Cliente removido com sucesso!')
        except sqlite3.Error as e:
            print(e)
            result = DBResults(type="ERROR", msg=f"Falha na remoção dos dados: {e}.")
            self.connection.rollback()
            return result
        except Exception as e:
            print(e)
            result = DBResults(type="ERROR", msg=f"Falha na remoção do registro do cliente id {id_customer}")
            self.connection.rollback()
            return result

        finally:
            self.close_connection()

    def update_customer(self, customers: List[Customer]):
        try:
            self.connect()

            cursor = self.connection.cursor()

            for customer in customers:
                cursor.execute(f"""
                                UPDATE Customers

                                SET
                                NAME = '{customer.name}',
                                PHONE = '{customer.phone}',
                                CITY = '{customer.city}'

                                WHERE ID_CUSTOMER = '{customer.id_customer}'
                                """)

                self.connection.commit()

            result = DBResults(type='OK', msg="Cliente(s) atualizado(s) com sucesso!")
            return result

        except sqlite3.Error as e:
            print(e)
            result = DBResults(type="ERROR", msg=f"Erro na atualização dos dados: {e}")
            self.connection.rollback()
            return result
        except Exception as e:
            print(e)
            result = DBResults(type="ERROR", msg=f"Falha no processo de atualização: {e}")
            self.connection.rollback()
            return result
        finally:
            self.connection.close()

    def excel_report(self):
        try:
            self.connect()
            customers = pd.read_sql_query("""SELECT * FROM Customers""", con = self.connection)
            reports_path = Path.joinpath(Path(__file__).parent, "reports")

            if not reports_path.exists():
                Path.mkdir(reports_path)

            xlsx_path = Path.joinpath(reports_path, "customers.xlsx")
            customers.to_excel(xlsx_path, sheet_name="Clientes", index=False)

            return DBResults(type="OK", msg="Relatório gerado com sucesso!")
        except Exception as e:
            print(e)
            return DBResults(type="ERROR", msg="Erro na geração de relatório.")


if __name__ == '__main__':
   database = Database_ERP()
   #customer: Customer = Customer(name="Jonas", phone="21 99226-6455", city="Paris")

   #database.register_customer(customer=customer)

   print(database.select_all_customers())