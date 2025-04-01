import tkinter as tk
from tkinter import ttk
import sqlite3

# Função para limpar os campos
def limpar_campos(frame):
    for widget in frame.winfo_children():
        if isinstance(widget, tk.Entry):
            widget.delete(0, tk.END)
        elif isinstance(widget, tk.Text):
            widget.delete("1.0", tk.END)

# Função para salvar os dados e limpar os campos
def salvar_cadastro():
    conexao_cadastro = sqlite3.connect("Banco estoque.db")
    terminal_cadastro_sql = conexao_cadastro.cursor()

    terminal_cadastro_sql.execute(
        "INSERT INTO cadastro(nome, quantidade, descricao, preco) VALUES (?, ?, ?, ?)",
        (Produto.get(), 0, Descricao.get("1.0", tk.END), float(Preco.get()))
    )
    conexao_cadastro.commit()
    conexao_cadastro.close()

    # Limpa os campos após salvar
    limpar_campos(Frame_Cadastro)

    print("Dados salvos e campos limpos com sucesso!")

# Cria a janela principal
janela = tk.Tk()
janela.title("Cadastro de Produtos")

# Cria um frame para os campos de entrada
Frame_Cadastro = tk.Frame(janela)
Frame_Cadastro.pack(padx=10, pady=10)

# Adiciona um Entry (campo de texto de uma linha)
label_nome = tk.Label(Frame_Cadastro, text="Nome:")
label_nome.grid(row=0, column=0, padx=5, pady=5)
Produto = tk.Entry(Frame_Cadastro, width=30)
Produto.grid(row=0, column=1, padx=5, pady=5)

# Adiciona um Entry para o preço
label_preco = tk.Label(Frame_Cadastro, text="Preço:")
label_preco.grid(row=1, column=0, padx=5, pady=5)
Preco = tk.Entry(Frame_Cadastro, width=30)
Preco.grid(row=1, column=1, padx=5, pady=5)

# Adiciona um Text (campo de texto de múltiplas linhas)
label_descricao = tk.Label(Frame_Cadastro, text="Descrição:")
label_descricao.grid(row=2, column=0, padx=5, pady=5)
Descricao = tk.Text(Frame_Cadastro, width=30, height=5)
Descricao.grid(row=2, column=1, padx=5, pady=5)

# Botão para salvar os dados
botao_salvar = tk.Button(janela, text="Salvar", command=salvar_cadastro)
botao_salvar.pack(pady=10)

# Inicia o loop principal da interface
janela.mainloop()
for item in items:
    box = customtkinter.CTkCheckBox(Produto_T, text=item)
    box.grid(pady=5)