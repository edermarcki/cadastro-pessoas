from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

window = Tk()

class functions():
    def limpar_tela(self):
        # limpa os campos de entrada de dados
        self.nomeent.delete(0, END)
        self.idadeent.delete(0, END)
        self.identificador.delete(0, END)

    def enviar_dados(self):
        self.clientes = []
        self.nome = self.nomeent.get()
        self.idade = self.idadeent.get()
        self.id = self.identificador.get()
        self.sexo = self.vgen.get()
        if len(self.nome) == 0:
            messagebox.showerror(title='ERRO', message='Por favor, informe um NOME!')
            return 0
        if len(self.idade) == 0:
            messagebox.showerror(title='ERRO', message='Por favor, informe uma IDADE!')
            return 0
        if len(self.id) == 0:
            messagebox.showerror(title='ERRO', message='Por favor, informe um ID!')
            return 0
        if self.sexo == 'F':
            self.sexo = 'Feminino'
        else:
            self.sexo = 'Masculino'
        self.clientes.append([self.nome, self.idade, self.sexo, self.id])
        for v in self.clientes:
            a = f'Nome: {v[0]}, Idade: {v[1]}, Sexo: {v[2]}, ID: {v[3]}' # formatando a saída de dados
        self.output.insert(END, a)

    def salvarComo(self):
        # pega a saída de dados e salva em um arquivo txt
        file = filedialog.asksaveasfile(defaultextension='.txt', filetypes=[("Text File", ".txt")])
        outputfile = str((self.output.get(0, END)))
        file.write(outputfile)
        file.close()


class app(functions):
    def __init__(self):
        self.window = window
        self.tela()
        self.frame1()
        self.frame2()
        self.txt()
        self.entrada()
        self.botoes()
        self.saida()
        self.menus()

        window.mainloop()

    def tela(self):
        self.window.title("Cadastro Simples")
        self.window.configure(background='#DADADA')
        self.window.geometry("1050x550") # dimensão padrão
        self.window.resizable(True, True) # responsividade
        self.window.maxsize(width=1200, height=650) # dimensão máxima
        self.window.minsize(width=950, height=550) #dimensão mínima

    def frame1(self):
        self.frame1 = LabelFrame(self.window, bd=4, bg='#dadada', text='Cadastro',
                                 font=('verdana', 18), borderwidth=1, relief='solid')
        self.frame1.place(relx=0.13, rely=0.05, relwidth=0.7, relheight=0.45)

    def frame2(self):
        self.frame2 = Frame(self.window)
        self.frame2.place(relx=0.13, rely=0.57, relwidth=0.7, relheight=0.27 )

    def txt(self):
        # labels pertinentes aos inputs
        self.nome = Label(self.frame1, text='Nome: ', bg='#dadada', font=('verdana', 12))
        self.nome.place(relx=0, rely=0.05, relwidth=0.15, relheight=0.1)
        self.idade = Label(self.frame1, text='Idade: ', bg='#dadada', font=('verdana', 12))
        self.idade.place(relx=0.65, rely=0.05, relwidth=0.15, relheight=0.1)
        self.genero = Label(self.frame1, text='Sexo: ', bg='#dadada', font=('verdana', 12))
        self.genero.place(relx=0, rely=0.45, relwidth=0.15, relheight=0.1)
        self.id = Label(self.frame1, text='ID: ', bg='#dadada', font=('verdana', 12))
        self.id.place(relx=0.635, rely=0.45, relwidth=0.15, relheight=0.1)

    def entrada(self):
        self.nomeent = Entry(self.frame1, bg='#fff', font=('verdana', 10) ) # Entrada de dados: nome
        self.nomeent.place(relx=0.12, rely=0.06, relwidth=0.20, relheight=0.1)
        self.idadeent = Entry(self.frame1, bg='#fff', font=('verdana', 10) ) # Entrada de dados: idade
        self.idadeent.place(relx=0.77, rely=0.06, relwidth=0.05, relheight=0.1)
        #radio button genero
        self.vgen = StringVar()
        self.rb_masc = Radiobutton(self.frame1, text="Masculino", value='M', bg='#dadada',
                                   font=('verdana', 11), variable=self.vgen)
        self.rb_masc.place(relx=0.12, rely=0.46, relwidth=0.15, relheight=0.1)

        self.rb_fem = Radiobutton(self.frame1, text="Feminino", value='F', bg='#dadada',
                                   font=('verdana', 11), variable=self.vgen)
        self.rb_fem.place(relx=0.12, rely=0.58, relwidth=0.146, relheight=0.1)
        self.rb_fem.select() #starts with this option selected
        #identificador
        self.identificador = Entry(self.frame1, bg='#fff', font=('verdana', 10) )
        self.identificador.place(relx=0.74, rely=0.45, relwidth=0.15, relheight=0.1)

    def botoes(self):
        self.enviar = Button(self.frame1, text='Enviar', bg='#1F7698', fg='white',
                               font=('verdana', 11), command=self.enviar_dados)
        self.enviar.place(relx=0.3, rely=0.8, relwidth=0.2, relheight=0.15)
        self.limpar = Button(self.frame1, text='Limpar', bg='#FFF', fg='#1F7698', font=('verdana', 11),
                             command=self.limpar_tela)
        self.limpar.place(relx=0.55, rely=0.8, relwidth=0.2, relheight=0.15)
        self.btn_exp_cad = Button(window, text='Salvar Cadastro', bg='#1F7698', fg='white',
                               font=('verdana', 11), command=self.salvarComo)
        self.btn_exp_cad.place(relx=0.42, rely=0.881, relwidth=0.16, relheight=0.07)

    def saida(self):
        # saída de dados
        scrollbar = Scrollbar(self.frame2)
        scrollbar.place(relx=0.98, rely=0.0, relheight=1)
        self.output = Listbox(self.frame2, font=('verdana', 13), selectbackground='#1F7698')
        self.output.place(relx=0.0, rely=0.0, relwidth=0.98, relheight=1)
        self.output.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.output.yview)

    def sobre(self):
        # informação sobre o autor
        messagebox.showinfo(title='Sobre', message='Criador por: Eder A. Marcki Júnior\n'
                                                   'Estudante de Análise e Desenvolvimento de Sistemas')

    def menus(self):
        # Menu
        menubar = Menu(self.window)
        self.window.config(menu=menubar)
        filemenu = Menu(menubar, tearoff=0)
        # A função sair está dentro do menu, pois é o único lugar em que usarei esta função.
        def quit(): self.window.destroy()
        menubar.add_cascade(label="File", menu=filemenu)
        filemenu.add_command(label= "Salvar Como...", command=self.salvarComo)
        menubar.add_cascade(label="Sobre", command=self.sobre)

        filemenu.add_command(label="Sair", command=quit)



app()
