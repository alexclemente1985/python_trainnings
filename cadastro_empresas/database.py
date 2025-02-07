import sqlite3
from typing import List
from classes.Company import Company
from classes.DbResults import DbResults
from pathlib import Path

class Database_cadEmp:
    def __init__(self, name="system.db") -> None:
        self.name = name
        self.database = self.create_db_path()
        self.create_table_company()


    def create_db_path(self):
        database_folder = Path.joinpath(Path(__file__).parent,'data')

        if not database_folder.exists():
            Path.mkdir(database_folder)

        return Path.joinpath(database_folder, self.name).as_posix()

    def connect(self):
        self.connection =sqlite3.connect(self.database)

    def close_connection(self):
        try:
            self.connection.close()
        except Exception as e:
            print(e)

    def create_table_company(self):
        self.connect()
        cursor = self.connection.cursor()

        cursor.execute("""
                        CREATE TABLE IF NOT EXISTS Empresas(
                            CNPJ TEXT,
                            NOME TEXT,
                            NUMERO TEXT,
                            LOGRADOURO TEXT,
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


    def register_company(self, fullDataSet: Company) -> DbResults:
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

        values = tuple(
                        (
                            fullDataSet.cnpj,
                            fullDataSet.nome,
                            fullDataSet.logradouro,
                            fullDataSet.numero,
                            fullDataSet.complemento,
                            fullDataSet.bairro,
                            fullDataSet.municipio,
                            fullDataSet.uf,
                            fullDataSet.cep,
                            fullDataSet.telefone,
                            fullDataSet.email
                        )
                    )

        try:
            self.connect()

            cursor = self.connection.cursor()
            cursor.execute(f"""INSERT INTO Empresas {campos_tabela} VALUES ({quantidade})""", values)

            self.connection.commit()
            result = DbResults(type="OK", msg="Empresa cadastrada com sucesso!")
            return result
        except sqlite3.IntegrityError as e:
            result = DbResults(type="ERRO", msg="CNPJ já cadastrado!")
            # Para evitar corrupção dos dados
            self.connection.rollback()
            return result
        except Exception as e:
            print(e)
            result = DbResults(type="ERRO", msg=f"Falha no processo de cadastro da empresa: {e}")
            self.connection.rollback()
            return result
        finally:
            self.close_connection()

    def select_all_companies(self) -> Company:
        try:
            self.connect()
            cursor = self.connection.cursor()
            cursor.execute("""SELECT * FROM Empresas ORDER BY CNPJ""")

            comp_result = cursor.fetchall()
            companies: List[Company] = []

            for company in comp_result:
                c = Company(
                    cnpj=company[0],
                    nome=company[1],
                    numero=company[2],
                    logradouro=company[3],
                    complemento=company[4],
                    bairro=company[5],
                    municipio=company[6],
                    uf=company[7],
                    cep=company[8],
                    telefone=company[9],
                    email=company[10]
                )
                companies.append(c)
            return companies

        except Exception as e:
            print(e)
            return None
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
        try:
            self.connect()

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