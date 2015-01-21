import sqlite3

con = sqlite3.connect('alunos.sqlite')
cursor = con.cursor()

cursor.execute("""CREATE TABLE notas (
                aluno TEXT NOT NULL,
                primeirotrimestre REAL NOT NULL,
                segundotrimestre REAL NOT NULL,
                terceirotrimestre REAL NOT NULL,
                mediafinal REAL NOT NULL)""")

con.commit()
print("OK")
con.close()
