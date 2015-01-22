#fecha as notas e salva no banco
from tkinter import *
from tkinter.messagebox import showerror
import sqlite3

def sum_media_final():
    notaP = numeroPrimeiro.get() 
    nota_S = numeroSegundo.get()  
    notaT = numeroTerceiro.get() 
    multiplicaçaoPri = notaP * 1
    multiplicaçaoSeg = nota_S * 2
    multiplicaçaoTer = notaT * 3

    soma = multiplicaçaoPri + multiplicaçaoSeg + multiplicaçaoTer
    media_final = soma / 6
    print(media_final)
    
    mediaVar.set(media_final)
    
    if save_check.get() == 1:
        try:
            con = sqlite3.connect('alunos.sqlite')
            cursor = con.cursor()
            cursor.execute("""
                    INSERT INTO notas(aluno,primeirotrimestre,segundotrimestre,
                    terceirotrimestre,mediafinal)
                    VALUES (?,?,?,?,?)""",
                   (nomeAluno.get(), numeroPrimeiro.get(),
                    numeroSegundo.get(), numeroTerceiro.get(), media_final))
 
            con.commit()
            con.close()
        except Exception as err:
               mediaVar.set(str(err))
    else:
        pass
            
def limpar_espaços():
    description.delete(0, END)
    primeiroTri.delete(0, END)
    segundoTri.delete(0, END)
    terceiroTri.delete(0, END)
    mediaVar.set(0.0)


app = Tk()
app.title("Fechamento de notas")

Label(app, text = "REPRESENTE A VIRGULA POR PONTO. EX: 8.5").pack()

Label(app, text = "Nome do Aluno:").pack()
nomeAluno = StringVar()
description = Entry(app, textvariable = nomeAluno)
description.pack()

Label(app, text = "Nota do Primeiro Trimestre:").pack()
numeroPrimeiro = DoubleVar()
primeiroTri = Entry(app, textvariable =  numeroPrimeiro)
primeiroTri.pack()


Label(app, text = "Nota do Segundo Trimestre:").pack()
numeroSegundo = DoubleVar()
segundoTri = Entry(app, textvariable = numeroSegundo)
segundoTri.pack()


Label(app, text = "Nota do Terceiro Trimestre:").pack()
numeroTerceiro = DoubleVar()
terceiroTri = Entry(app, textvariable = numeroTerceiro)
terceiroTri.pack()

mediaFinal = 0 
mediaVar = DoubleVar()
Button(app, text = "Fechar Nota", command = sum_media_final).pack()
Label(app, text = "Media Final:").pack()
Label(app, textvariable = mediaVar).pack()


save_check = BooleanVar()
Checkbutton(app, text="Salvar dados dos alunos",
                         variable=save_check, onvalue=True, offvalue=False).pack(side=LEFT)

Button(app, text = "Sair", command = app.destroy).pack(side = LEFT)
Button(app, text = "Limpar", command = limpar_espaços).pack(side = RIGHT)



app.mainloop()


