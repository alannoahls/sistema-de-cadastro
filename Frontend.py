from tkinter import *
from Backend import save_fan, get_fans  # Importando as funções do backend

class Gui:
    def __init__(self):
        self.window = Tk()
        self.window.title("Cadastro de Fãs - PYSQL")
        self.window.geometry("450x350")
        self.window.configure(bg="#2C2F33")  # Fundo da janela em cinza escuro

        # Variáveis para armazenar os dados de entrada
        self.txtNome = StringVar()
        self.txtSobrenome = StringVar()
        self.txtEmail = StringVar()
        self.txtCPF = StringVar()

        # Labels e campos de entrada com estilos personalizados
        self.custom_label("Nome:", 0, 0)
        self.custom_entry(self.txtNome, 0, 1)

        self.custom_label("Sobrenome:", 1, 0)
        self.custom_entry(self.txtSobrenome, 1, 1)

        self.custom_label("E-mail:", 2, 0)
        self.custom_entry(self.txtEmail, 2, 1)

        self.custom_label("Instagram:", 3, 0)
        self.custom_entry(self.txtCPF, 3, 1)

        # Configuração da Listbox e Scrollbar com estilo
        self.listbox = Listbox(self.window, height=8, width=50, font=("Arial", 10), bg="#F3F3F3", selectbackground="#DDA0DD", relief="flat", bd=1)
        self.listbox.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

        self.scrollbar = Scrollbar(self.window, command=self.listbox.yview)
        self.scrollbar.grid(row=4, column=2, sticky='ns')
        self.listbox.config(yscrollcommand=self.scrollbar.set)

        # Adicionar o botão "Salvar Fã" com estilo roxo
        self.botao_salvar = Button(self.window, text="Salvar Fã", font=("Arial", 10, "bold"), bg="#9932CC", fg="white", relief="groove", bd=2, command=self.save_fan_data)
        self.botao_salvar.grid(row=5, column=0, columnspan=2, pady=10)

        # Atualiza a Listbox com os dados do banco
        self.refresh_listbox()

    # Função para adicionar cor personalizada ao Label e Entry
    def custom_label(self, text, row, column):
        label = Label(self.window, text=text, font=("Arial", 10, "bold"), fg="#FFFFFF", bg="#2C2F33")
        label.grid(row=row, column=column, sticky='w', padx=5, pady=5)

    def custom_entry(self, text_var, row, column):
        entry = Entry(self.window, textvariable=text_var, width=30, font=("Arial", 10), relief="solid", bd=1)
        entry.grid(row=row, column=column, padx=5, pady=5)

    # Função para atualizar a Listbox com os dados dos fãs no banco de dados
    def refresh_listbox(self):
        self.listbox.delete(0, END)  # Limpa a Listbox
        fãs = get_fans()  # Obtém os fãs do banco de dados
        for fã in fãs:
            self.listbox.insert(END, f"{fã[1]} {fã[2]} - {fã[3]}")  # Exibe nome, sobrenome e Instagram

    # Função para salvar os dados do fã no banco de dados
    def save_fan_data(self):
        nome = self.txtNome.get()
        sobrenome = self.txtSobrenome.get()
        email = self.txtEmail.get()
        instagram = self.txtCPF.get()

        # Chama a função do backend para salvar os dados no banco
        save_fan(nome, sobrenome, email, instagram)

        # Atualiza a Listbox com os novos dados
        self.refresh_listbox()

        # Limpa os campos de entrada
        self.txtNome.set("")
        self.txtSobrenome.set("")
        self.txtEmail.set("")
        self.txtCPF.set("")

    # Função para iniciar o loop da janela
    def run(self):
        self.window.mainloop()
