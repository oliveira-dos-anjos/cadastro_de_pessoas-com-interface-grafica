from dependências.arquivo import *
from datetime import *
from tkinter import *




def segunda_janela():
    janela2 = Toplevel()
    janela2.title('dados cadastrados')
    janela2.geometry('600x300+200+200')
    janela2['bg'] = 'gray'
    janela2.resizable(False,False)

    h = Scrollbar(janela2, orient = 'horizontal') 

    h.pack(side = BOTTOM, fill = X) 


    v = Scrollbar(janela2) 

    v.pack(side = RIGHT, fill = Y) 

    t = Text(janela2, width = 10, height = 10, wrap = NONE, 
    xscrollcommand = h.set,  
    yscrollcommand = v.set) 

    try:
        a = open(arq, "rt")
    except:
        t.insert(END,"Erro ao ler o arquivo")
    else:
        t.insert(END,"NOME           | SEXO| NASCIMENTO  | PESO  | CONTATO    \n")
        t.insert(END,"__" * 28)
        t.insert(END, "\n")
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace("\n", "")
            t.insert(END,f"{dado[0]:<15}| {dado[1]:<4}| {dado[2]:<12}| {dado[3]:<6}| {dado[4]}\n")
            
    finally:
        a.close()

    t.pack(side=LEFT, ipadx=200, ipady=200, padx=10, pady=10) 


    h.config(command=t.xview) 


    v.config(command=t.yview) 


    btn = Button(janela2, text= 'fechar janela3', command= janela2.destroy, bg= 'red')
    btn.place(x=500, y=250)


def terceira_janela():
    janela3 = Toplevel()
    janela3.geometry('500x250')
    janela3['bg'] = 'cyan'
    janela3.title('adicionar novos dados')
    janela3.resizable(False, False)



    # recebendo os dados a partir da terceira janela3
    label_nome = Label(janela3, text="nome")
    label_nome.place(x=10, y=10)
    nome = Entry(janela3, width=20)
    nome.place(x=145, y=10)

    label_sexo = Label(janela3, text="sexo [F/M]")
    label_sexo.place(x=10, y=35)
    sexo = Entry(janela3, width=20)
    sexo.place(x=145, y=35)

    label_dia = Label(janela3, text="nascimento")
    label_dia.place(x=10, y=60)
    dia = Entry(janela3, width=4)
    dia.place(x=145, y=60)

    label_mes = Label(janela3, text="/")
    label_mes.place(x=173, y=59)
    mes = Entry(janela3, width=4)
    mes.place(x=184, y=60)

    label_ano = Label(janela3, text="/")
    label_ano.place(x=211, y=59)
    ano = Entry(janela3, width=7)
    ano.place(x=222, y=60)

    label_peso = Label(janela3, text="peso")
    label_peso.place(x=10, y=85)
    peso = Entry(janela3, width=20)
    peso.place(x=145, y=85)

    label_contato = Label(janela3, text="contato")
    label_contato.place(x=10, y=110)
    contato = Entry(janela3, width=20)
    contato.place(x=145, y=110)

    dia = mes = ano = 00


    # função para salvar os arquivos

    def leiaCont(ct):
        try:
            n = int(input(ct))
            contato = str(n)
        except:
            label_ct = Label(janela3, text="!", bg='red')
            label_ct.place(x=272, y=110)
            
        else:
            if len(contato) <=9:
                label_ct = Label(janela3, text="!", bg='red')
                label_ct.place(x=272, y=110)
            else:
                return n


    def calculo_idade(a, m, d):
        try:
            dat_nasc = date(a, m, d)
            nasc = date.today() - dat_nasc
            calculo_idade = nasc.days / 365.25
            idade = int(calculo_idade)
            nascimento = str(f"{d}/{m}/{a}")
        except:
            label_msg = Label(janela3, text="Algumas informações de nascimento estão incorretas")
            label_msg.place(x=10, y=180)

            label_ano = Label(janela3, text="?", bg='red')
            label_ano.place(x=272, y=60)


        else:
            return nascimento



    def salvar():
        nm = nome.get()
        if nm == "" or nm.isspace():
            label_nm = Label(janela3, text="?", bg='red')
            label_nm.place(x=272, y=10)
        else:
            n = str(nm)

        sx = str(sexo.get()).upper().strip()
        if sx == 'F' or sx == 'M':
             s = str(sx)

        else:
            label_sx = Label(janela3, text="?", bg='red')
            label_sx.place(x=272, y=35)
           

        d = int(dia.get())
        m = int(mes.get())
        a = int(ano.get())
        ps = peso.get()
        p = float(ps)
        ct = str(contato.get())
        c = leiaCont(ct)
        if len(ct) <= 8:
            label_sx = Label(janela3, text="?", bg='red')
            label_sx.place(x=272, y=80)
        nascimento = calculo_idade(a, m, d)







        try:
            a = open(arq, 'at')
        except:
            label_msg = Label(janela3, text="Houve um erro ao abrir o arquivo!")
            label_msg.place(x=10, y=180)
        else:
            try:
                if nascimento:
                    a.write(f"{n};{s};{nascimento};{p:.1f};{c}\n")
                    label_msg = Label(janela3, text=f'Novo registro de \'{n}\' adicionado com sucesso.')
                    label_msg.place(x=10, y=200)
                    
            except:
                label_msg = Label(janela3, text="Houve um erro ao salvar o arquivo")
                label_msg.place(x=10, y=165)
            else:

                a.close()



    # definindo botoes da terceira janela3
    btn = Button(janela3, text= 'salvar', command= salvar, bg= 'green')
    btn.place(x=35, y=220)

    btn = Button(janela3, text= "limpar", command= janela3.destroy, bg= 'orange')
    btn.place(x=100, y=220)


    btn = Button(janela3, text= "fechar janela", command= janela3.destroy, bg= 'red')
    btn.place(x=165, y=220)




# programa principal

# layout da janela3 principal
janela = Tk()
janela.title("gerenciador de dados pessoais")
janela['bg'] = 'gray'
img = PhotoImage(file= 'C:\\Users\\RAFAEL\Desktop\\adição e manipulacão de dados\\dependências\\imagem\\icone.png')
janela.iconphoto(True, img)




#dimensões da janela3 principal
largura = 600
altura = 300

# resolução do sistema
largura_screen = janela.winfo_screenwidth()
altura_screen = janela.winfo_screenheight()

# faz com que a janela principal sempre apareça no centro
posx = (largura_screen / 2) - (largura / 2)
posy = (altura_screen / 2) - (altura / 2)

#define a geometria da janela principal
janela.geometry('%dx%d+%d+%d' % (largura, altura, posx, posy))

#adicionando botoes na janela3 principal
btn = Button(janela, text= '1 - ver pessoas cadastrados',command=segunda_janela, bg= 'green')
btn.place(x=15, y=40)

btn = Button(janela, text= '2 - cadastrar novas pessoas', command=terceira_janela, bg= 'blue')
btn.place(x=15, y=80)

btn = Button(janela, text= '3 - sair do sistema', command= janela.destroy, bg= 'red')
btn.place(x=15, y=120)



# Verifica se o arquivo existe, se não, o arquivo é criado
arq = 'Dados cadastrais'
if not ArquivoExist(arq):
    Criar_Arq(arq)


janela.mainloop()