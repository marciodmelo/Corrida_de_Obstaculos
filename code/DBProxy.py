import sqlite3

class DBProxy:
    def __init__(self, db_name: str):
        self.db_name = db_name
        self.connection = sqlite3.connect(self.db_name)
        self._create_table()

    def _create_table(self):
        """Cria a tabela se ela não existir."""
        with self.connection:
            self.connection.execute('''
                CREATE TABLE IF NOT EXISTS dados(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    score INTEGER NOT NULL,
                    date TEXT NOT NULL
                )
            ''')

    def save(self, score_dict: dict):
        """Salva um novo registro na tabela."""
        try:
            with self.connection:
                self.connection.execute(
                    'INSERT INTO dados (name, score, date) VALUES (:name, :score, :date)',
                    score_dict
                )
        except sqlite3.Error as e:
            print(f"Erro ao salvar os dados: {e}")

    def retrieve_top10(self) -> list:
        """Recupera os 10 melhores registros ordenados por score."""
        try:
            with self.connection:
                return self.connection.execute(
                    'SELECT * FROM dados ORDER BY score DESC LIMIT 10'
                ).fetchall()
        except sqlite3.Error as e:
            print(f"Erro ao recuperar os dados: {e}")
            return []

    def close(self):
        """Fecha a conexão com o banco de dados."""
        if self.connection:
            self.connection.close()