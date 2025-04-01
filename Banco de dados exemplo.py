import customtkinter
import sqlite3

# conecta com o banco de  dados
#create

def criar_dados():
    conexao = sqlite3.connect("dados.db")
    terminal_sql = conexao.cursor()
    terminal_sql.execute("CREATE TABLE IF NOT EXISTS pessoas(nome text)")
    conexao.commit()
    conexao.close()

#create
def salvar_dados():
    conexao = sqlite3.connect("dados.db")
    terminal_sql = conexao.cursor()
    terminal_sql.execute(f"INSERT INTO pessoas (nome) VALUES(' {Entrada.get()}')")
    conexao.commit()
    conexao.close()

#read
def ler_dados():
    conexao = sqlite3.connect("dados.db")
    terminal_sql = conexao.cursor()
    terminal_sql.execute("SELECT * FROM pessoas")
    receber_dados = terminal_sql.fetchall()

    nome = ""

    for i in receber_dados:
        nome += "\n" + str(i[0])
    Dados_nome.configure(text=nome)
    conexao.close()

# Chamar a função de criar o bamco de dados

criar_dados()


customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("blue")

janela = customtkinter.CTk()
janela.title("Sistema Salva nome")
janela.geometry("300x300")

Titulo = customtkinter.CTkLabel(janela, text="Sistema \n Salva Nome", font=("Courier", 18))
Titulo.grid(pady=5, padx=60, row=0, column=1)

Entrada = customtkinter.CTkEntry(janela, placeholder_text="Insera o nome", font=("Courier", 18), width=180)
Entrada.grid(pady=5, padx=60, row=1, column=1)

Salvar = customtkinter.CTkButton(janela, text="Salvar", width=180, command=salvar_dados)
Salvar.grid(pady=5, padx=60, row=2, column=1)

Listar = customtkinter.CTkButton(janela, text="Listar", width=180, command=ler_dados)
Listar.grid(pady=5, padx=60, row=3, column=1)

Dados_nome = customtkinter.CTkLabel(janela, text=" ", font=("Courier", 18))
Dados_nome.grid(pady=5, padx=60, row=3, column=1)

janela.mainloop()
