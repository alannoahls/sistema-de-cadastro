from tkinter import *
from Backend import save_fan, get_fans, view_all, search, insert  # Funções do backend

class Gui:
    def __init__(self):
        # Configuração da janela principal
        self.window = Tk()
        self.window.title("Cadastro de Fãs - PYSQL")
        self.window.geometry("450x400")
        self.window.configure(bg="#2C2F33")

        # Variáveis para armazenar os dados de entrada
        self.txtNome = StringVar()
        self.txtSobrenome = StringVar()
        self.txtEmail = StringVar()
        self.txtCPF = StringVar()

        # Labels e campos de entrada
        self.custom_label("Nome:", 0, 0)
        self.custom_entry(self.txtNome, 0, 1)
        self.custom_label("Sobrenome:", 1, 0)
        self.custom_entry(self.txtSobrenome, 1, 1)
        self.custom_label("E-mail:", 2, 0)
        self.custom_entry(self.txtEmail, 2, 1)
        self.custom_label("Instagram:", 3, 0)
        self.custom_entry(self.txtCPF, 3, 1)

        # Configuração da Listbox e Scrollbar
        self.listbox = Listbox(self.window, height=8, width=50, font=("Arial", 10), bg="#F3F3F3", selectbackground="#DDA0DD", relief="flat", bd=1)
        self.listbox.grid(row=4, column=0, columnspan=2, padx=5, pady=5)
        self.scrollbar = Scrollbar(self.window, command=self.listbox.yview)
        self.scrollbar.grid(row=4, column=2, sticky='ns')
        self.listbox.config(yscrollcommand=self.scrollbar.set)

        # Botões com comandos (placeholders, serão configurados no arquivo `aplicação.py`)
        self.btnViewAll = Button(self.window, text="Ver Todos", font=("Arial", 10, "bold"), bg="#4CAF50", fg="white", relief="groove", bd=2)
        self.btnViewAll.grid(row=5, column=0, pady=10, sticky="ew")

        self.btnSearch = Button(self.window, text="Buscar", font=("Arial", 10, "bold"), bg="#1E90FF", fg="white", relief="groove", bd=2)
        self.btnSearch.grid(row=5, column=1, pady=10, sticky="ew")

        self.btnInsert = Button(self.window, text="Inserir", font=("Arial", 10, "bold"), bg="#9932CC", fg="white", relief="groove", bd=2)
        self.btnInsert.grid(row=6, column=0, columnspan=2, pady=10, sticky="ew")

    def custom_label(self, text, row, column):
        label = Label(self.window, text=text, font=("Arial", 10, "bold"), fg="#FFFFFF", bg="#2C2F33")
        label.grid(row=row, column=column, sticky='w', padx=5, pady=5)

    def custom_entry(self, text_var, row, column):
        entry = Entry(self.window, textvariable=text_var, width=30, font=("Arial", 10), relief="solid", bd=1)
        entry.grid(row=row, column=column, padx=5, pady=5)

    def run(self):
        self.window.mainloop()
