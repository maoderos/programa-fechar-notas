from tkinter import *
import sqlite3


def get_students_data():
    con = sqlite3.connect('dados_alunos.sqlite')
    cursor = con.cursor()
    cursor.execute("SELECT primeirotrimestre FROM notas WHERE aluno = '%s'"
                   % aluno.get())
    
    primeiro_trimestre = cursor.fetchall()
    primeiro = str(primeiro_trimestre)
    print(primeiro)
    trimestre1.set(primeiro)
    cursor.execute("SELECT segundotrimestre FROM notas WHERE aluno = '%s'" %
                   aluno.get())
    segundo_trimestre = cursor.fetchall()
    segundo = str(segundo_trimestre)
    trimestre2.set(segundo)
    cursor.execute("SELECT terceirotrimestre FROM notas WHERE aluno = '%s'" %
                   aluno.get())
    terceiro_trimestre = cursor.fetchall()
    terceiro = str(terceiro_trimestre)
    trimestre3.set(terceiro)
    cursor.execute("SELECT mediafinal FROM notas WHERE aluno = '%s'" %
                   aluno.get())
    media = cursor.fetchall()
    final = str(media)
    media_final.set(final)
    

  
    con.close()

    

root = Tk()
root.title('Dados dos alunos')
Label(root, text="digie o nome do aluno que voce deseja procurar").pack()
aluno = StringVar()
Entry(root, textvariable=aluno).pack()
Label(root, text="PRIMEIRO TRIMESTRE:").pack()
trimestre1 = StringVar()
Label(root, textvariable=trimestre1).pack()
Label(root, text="SEGUNDO TRIMESTRE:").pack()
trimestre2 = StringVar()
Label(root, textvariable=trimestre2).pack()
Label(root, text="TERCEIRO TRIMESTRE:").pack()
trimestre3 = StringVar()
Label(root,textvariable=trimestre3).pack()
Label(root, text="MEDIA FINAL:").pack()
media_final = StringVar()
Label(root, textvariable= media_final)
Button(root, text='procurar', command= get_students_data).pack(side=RIGHT)
Button(root, text='sair', command=root.destroy).pack(side=LEFT)
root.mainloop()
