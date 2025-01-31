import sqlite3
from pathlib import Path
from typing import List
import pandas as pd
from PySide6.QtSql import QSqlDatabase, QSqlTableModel, QSqlQuery
from datafile import *

class Database():
    def __init__(self, data:pd.DataFrame = default_data, dbname: str = "banco.db", tablename: str = 'notas') -> None:
        self.db_path = Path.joinpath(Path(__file__).parent, 'db')
        
        self.conn = None
        self.data = data
        self.dbname = dbname
        self.tablename= tablename
        self.db_file = Path.joinpath(self.db_path, self.dbname)

        self.load_db()
        self.close_initial_conn()
        

    def load_db(self):
        if not self.conn:
            self.connect_db()

        # Verificação da existência prévia do banco e da tabela (para evitar erros de tabela existente)
        cursor = self.conn.cursor()
        ## fetchall() retorna uma lista de tuplas, onde o valor vai estar na posição 0 da tupla... como count só retorna 1 valor, é necessário colocar [0][0]
        count = cursor.execute(f"""SELECT COUNT(*) FROM sqlite_master WHERE type='table' AND name='{self.tablename}'""").fetchall()[0][0]
        
        if not count == 1:
            self.data.to_sql(self.tablename, con=self.conn)

    def connect_db(self):
        if not self.db_path.exists():
            Path.mkdir(self.db_path)
            print('Pasta para banco de dados criada...')
        
        self.conn = sqlite3.connect(self.db_file)
        
    
    def close_initial_conn(self):
        self.conn.close()

    def qsqlDatabase(self):
        db = QSqlDatabase("QSQLITE")
        db.setDatabaseName(self.db_file.as_posix())
        return db
