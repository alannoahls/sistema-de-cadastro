# Importando o backend (Backend.py) e o GUI (Frontend.py)
import Backend as core
import Frontend as gui
import tkinter as tk

# Inicializando a variável app com None
app = None

# Função para exibir todos os registros de fãs
def view_command():
    app.listbox.delete(0, tk.END)  # Limpa a listbox antes de exibir
    rows = core.view_all()  # Busca todos os registros
    for row in rows:
        app.listbox.insert(tk.END, row)  # Insere registros válidos na listbox

# Função para inserir um novo fã no banco de dados
def insert_command():
    name = app.txtNome.get()
    surname = app.txtSobrenome.get()
    email = app.txtEmail.get()
    instagram = app.txtCPF.get()
    core.save_fan(name, surname, email, instagram)
    view_command()  # Atualiza a listbox
    # Limpa os campos de entrada para o próximo cadastro
    app.txtNome.set("")
    app.txtSobrenome.set("")
    app.txtEmail.set("")
    app.txtCPF.set("")

# Função para selecionar um fã da listbox e preencher os campos de entrada
def get_selected_row(event):
    try:
        index = app.listbox.curselection()[0]
        selected_row = app.listbox.get(index)
        app.txtNome.set(selected_row[1])
        app.txtSobrenome.set(selected_row[2])
        app.txtEmail.set(selected_row[3])
        app.txtCPF.set(selected_row[4])
    except IndexError:
        pass

# Função principal que inicia a aplicação
def run():
    global app
    app = gui.Gui()
    app.listbox.bind('<<ListboxSelect>>', get_selected_row)
    app.botao_salvar.configure(command=insert_command)  # Configura o botão "Salvar Fã" para inserir
    app.run()  # Inicia o loop da interface gráfica

# Executa a aplicação
if __name__ == "__main__":
    run()
