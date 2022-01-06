import sqlite3


class Database():
    def __init__(self,) -> None:
        self.name = 'systemtarefas.db'
        
    def connect(self) -> bool:
        try:
            self.connection = sqlite3.connect(self.name)
            return True
        except:
            return False   
    
    def close(self) -> bool:
        try:
            self.connection.close()
        except:
            return False

    def criar_Tabela(self):
        cursor = self.connection.cursor()
        cursor.execute(f"""CREATE TABLE IF NOT EXISTS tarefas(
                            
                            date DATETIME PRIMARY KEY NOT NULL UNIQUE,
                            tarefa TEXT                      
                                                                );""")        
        self.connection.commit()

    def listar_Tarefas(self) -> list:

        cursor = self.connection.cursor()

        try:
            cursor.execute(f"SELECT * FROM tarefas ORDER BY date")
            print(cursor.fetchall())
        except:
            raise ValueError("Erro ao listar tarefas")

    def insere_Tarefa(self,tarefas) ->  bool:
        cursor = self.connection.cursor()

        try:
            for i in range(len(tarefas)):
                cursor.execute(f"INSERT INTO tarefas (date,tarefa) VALUES('{tarefas[i][0]}','{tarefas[i][1]}')")    
            self.connection.commit()
            return True
        except:
            return False






'''bd = Database()
bd.connect()
bd.criar_Tabela()
bd.insere_Tarefa(tarefa)
bd.listar_Tarefas()
bd.close()'''