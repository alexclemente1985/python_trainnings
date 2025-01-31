import sqlite3
from pathlib import Path
from typing import List
import pandas as pd
from PySide6.QtSql import QSqlDatabase, QSqlTableModel

#db = QSqlDatabase("QSQLITE")


default_data= pd.DataFrame([
            ['001', 'R$100,00','R$ 18,00','R$ 5,00'],
            ['002', 'R$100,00','R$ 18,00','R$ 5,00'],
            ['003', 'R$100,00','R$ 18,00','R$ 5,00'],
            ['004', 'R$100,00','R$ 18,00','R$ 5,00'],
            ['005', 'R$100,00','R$ 18,00','R$ 5,00'],
            ['006', 'R$100,00','R$ 18,00','R$ 5,00'],
            ['007', 'R$100,00','R$ 18,00','R$ 5,00'],
            ['008', 'R$100,00','R$ 18,00','R$ 5,00'],
            ['009', 'R$100,00','R$ 18,00','R$ 5,00'],
        ], columns=['Notas','Valor','ICMS','IPI'])

class Database():
    def __init__(self, data:pd.DataFrame = default_data, dbname: str = "banco.db", tablenames: List[str] = ['notas']) -> None:
        self.db_path = Path.joinpath(Path(__file__).parent, 'db')
        
        #db.setDatabaseName(dbname)

        self.conn = None
        self.data = data
        self.dbname = dbname
        self.tablenames = tablenames

        self.load_db()
        

    def load_db(self):
        if not self.conn:
            self.connect_db()

        # Criação da tabela "notas" e outras no banco de dados
        for t in self.tablenames:
            self.data.to_sql(t, con=self.conn, if_exists='replace')

    def connect_db(self):
        if not self.db_path.exists():
            Path.mkdir(self.db_path)
            print('Pasta para banco de dados criada...')
        
        db = Path.joinpath(self.db_path, self.dbname)
        self.conn = sqlite3.connect(db)
