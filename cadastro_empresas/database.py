import sqlite3
from typing import List
from classes.Company import Company
from classes.DbResults import DbResults
from pathlib import Path
import pandas as pd

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
            cursor.execute(f"""DELETE FROM Empresas WHERE CNPJ == '{cnpj}'""")
            self.connection.commit()

            return DbResults(type='OK',msg="Empresa removida com sucesso!")
        except sqlite3.Error as e:
            print(e)
            result = DbResults(type="ERRO", msg=f"Erro na remoção dos dados: {e}")
            self.connection.rollback()
            return result
        except Exception as e:
            print(e)
            self.connection.rollback()
            return DbResults(type='ERRO', msg=f"Falha na remoção do registro da empresa de cnpj {cnpj}.")
        finally:
            self.close_connection()

    def update_company(self, fullDataSets: List[Company]):
        try:
            self.connect()

            cursor = self.connection.cursor()
            for company in fullDataSets:
                cursor.execute(f"""
                                UPDATE Empresas

                                SET
                                CNPJ = '{company.cnpj}',
                                NOME = '{company.nome}',
                                LOGRADOURO = '{company.logradouro}',
                                NUMERO = '{company.numero}',
                                COMPLEMENTO = '{company.complemento}',
                                BAIRRO = '{company.bairro}',
                                MUNICIPIO = '{company.municipio}',
                                UF = '{company.uf}',
                                CEP = '{company.cep}',
                                TELEFONE = '{company.telefone}',
                                EMAIL = '{company.email}'

                                WHERE CNPJ = '{company.cnpj}'

                            """)

                self.connection.commit()

            result = DbResults(type="OK", msg="Empresa(s) atualizada(s) com sucesso!")
            return result

        except sqlite3.Error as e:
            print(e)
            result = DbResults(type="ERRO", msg=f"Erro na atualização dos dados: {e}")
            self.connection.rollback()
            return result

        except Exception as e:
            print(e)
            result = DbResults(type="ERRO", msg=f"Falha no processo de atualização: {e}")
            self.connection.rollback()
            return result
        finally:
            self.connection.close()


    def excel_report(self):
        try:
            self.connect()

            companies = pd.read_sql_query("""SELECT * FROM Empresas""", con = self.connection)

            reports_path = Path.joinpath(Path(__file__).parent, "reports")

            if not reports_path.exists():
                Path.mkdir(reports_path)

            xlsx_path = Path.joinpath(reports_path,"companies.xlsx")

            companies.to_excel(xlsx_path, sheet_name="Empresas", index=False)

            return DbResults(type="OK", msg="Relatório gerado com sucesso!")
        except Exception as e:
            print(e)
            return DbResults(type="Erro", msg="Erro na geração do relatório.")