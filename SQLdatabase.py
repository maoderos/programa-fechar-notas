#cria o banco
import sqlite3

con = sqlite3.connect('alunos.sqlite')
cursor = con.cursor()

cursor.execute("""CREATE TABLE notas (
                aluno TEXT NOT NULL,
                primeirotrimestre TEXT NOT NULL,
                segundotrimestre TEXT NOT NULL,
                terceirotrimestre TEXT NOT NULL,
                mediafinal TEXT NOT NULL)""")

con.commit()
print("OK")
con.close()
