import sqlite3
from classes.Company import Company

class Database_cadEmp:
    def __init__(self, name="system.db") -> None:
        self.name = name

    def connect(self):
        self.connection =sqlite3.connect(self.name)

    def close_connection(self):
        try:
            self.connection.close()
        except Exception as e:
            print(e)

    def create_table_company(self):
        cursor = self.connection.cursor()

        cursor.execute("""
                        CREATE TABLE IF NOT EXISTS Empresas(
                            CNPJ TEXT,
                            NOME TEXT,
                            NUMERO TEXT,
                            COMPLEMENTO TEXT,
                            BAIRRO TEXT,
                            MUNICIPIO TEXT,
                            UF TEXT,
                            CEP TEXT,
                            TELEFONE TEXT,
                            EMAIL TEXT,

                            PRIMARY KEY(CNPJ)
                       );
                       """)
        self.close_connection()


    def register_company(self, fullDataSet):
        campos_tabela = (
            'CNPJ',
            'NOME',
            'LOGRADOURO',
            'NUMERO',
            'COMPLEMENTO',
            'BAIRRO',
            'MUNICIPIO',
            'UF',
            'CEP',
            'TELEFONE',
            'EMAIL'
            )

        quantidade = ("?,?,?,?,?,?,?,?,?,?,?")

        cursor = self.connection.cursor()

        try:
            cursor.execute(f"""INSERT INTO Empresas {campos_tabela} VALUES ({quantidade})""", fullDataSet)
            self.connection.commit()
            return "OK"
        except Exception as e:
            print(e)
            return "ERROR"
        finally:
            self.close_connection()

    def select_all_companies(self):
        try:
            self.connect()
            cursor = self.connection.cursor()
            cursor.execute("""SELECT * FROM Empresas ORDER BY NOME""")

            empresas = cursor.fetchall()
            return empresas
        except Exception as e:
            print(e)
        finally:
            self.close_connection()

    def delete_company(self, cnpj: str):
        try:
            self.connect()
            cursor = self.connection.cursor()
            cursor.execute(f"""DELETE * FROM Empresas WHERE CNPJ == '{cnpj}'""")
            self.connection.commit()

            return 'OK'
        except Exception as e:
            print(e)
            return 'ERROR'
        finally:
            self.close_connection()

    def update_company(self, fullDataSet: Company):
        self.connect()

        try:
            cursor = self.connection.cursor()
            cursor.execute(f"""
                                CNPJ = '{fullDataSet.cnpj}',
                                NOME = '{fullDataSet.nome}',
                                LOGRADOURO = '{fullDataSet.nome}',
                                NUMERO = '{fullDataSet.numero}',
                                COMPLEMENTO = '{fullDataSet.complemento}',
                                BAIRRO = '{fullDataSet.bairro}',
                                MUNICIPIO = '{fullDataSet.municipio}',
                                UF = '{fullDataSet.uf}',
                                CEP = '{fullDataSet.cep}',
                                TELEFONE = '{fullDataSet.telefone}',
                                EMAIL = '{fullDataSet.email}'

                                WHERE CNPJ = '{fullDataSet.cnpj}'

                            """)

            self.connection.commit()

        except Exception as e:
            print(e)
        finally:
            self.connection.close()