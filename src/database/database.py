import sqlite3
import os

#Necessário alterar para o diretório do banco de dados para fazer a conexão.

class Database():
    def __init__(self,) -> None:
        os.chdir('G:\\Meu Drive\\Programas\\Python\\Gerenciador_Tarefas\\src\\database')
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
                            prioridade INTEGER
                            status INTEGER                    
                                                                );""")        
        self.connection.commit()

    def listar_Tarefas(self,dia) -> list:

        cursor = self.connection.cursor()

        try:
            cursor.execute(f"SELECT * FROM tarefas WHERE date LIKE '{dia}%' ORDER BY date")
            return cursor.fetchall()
        except:
            raise ValueError("Erro ao listar tarefas")

    def insere_Tarefa(self,tarefas) -> bool:
        cursor = self.connection.cursor()

        try:
            for i in range(len(tarefas)):
                cursor.execute(f"INSERT INTO tarefas (date,tarefa,prioridade,status) VALUES('{tarefas[i][0]}','{tarefas[i][1]}','{tarefas[i][2]}','{tarefas[i][3]}')")    
            self.connection.commit()
            return True
        except:
            raise ValueError("Erro ao cadastrar tarefa")

    def alterar_Tarefa(self,tarefa) -> bool:
        cursor = self.connection.cursor()

        try:
            cursor.execute(f"UPDATE tarefas SET tarefa = '{tarefa[1]}', prioridade = '{tarefa[2]}', status = '{tarefa[3]}' WHERE date = '{tarefa[0]}'")
            self.connection.commit()
            return True
        except:
           raise ValueError("Erro ao alterar tarefa")

    def concluir_Tarefa(self,data) -> bool:
        cursor = self.connection.cursor()

        try:
            cursor.execute(f"UPDATE tarefas SET status = 1 WHERE date = '{data}'")
            self.connection.commit()
            return True
        except:
            raise ValueError("Erro ao alterar tarefa")

    def excluir_Tarefa(self,data) -> bool:
        cursor = self.connection.cursor()

        cursor.execute(f"DELETE FROM tarefas WHERE date = '{data}'")
        self.connection.commit()



'''bd = Database()
bd.connect()
#print(bd.listar_Tarefas('2022-01-20'))

bd.alterar_Tarefa(['2022-01-20 09:00', 'tarefa alterada', 1, 0])

bd.close()'''