import tkinter as tk
from tkinter import ttk

# Criando a janela principal
root = tk.Tk()
root.title("Tabela com Tkinter")

# Definindo as colunas da tabela
colunas = ("ID", "Nome", "Idade", "Cidade")

# Criando o Treeview (tabela)
tabela = ttk.Treeview(root, columns=colunas, show="headings")

# Configurando o cabeçalho da tabela
for col in colunas:
    tabela.heading(col, text=col)

# Adicionando algumas linhas de dados
dados = [
    (1, "João", 25, "São Paulo"),
    (2, "Maria", 30, "Rio de Janeiro"),
    (3, "Carlos", 28, "Belo Horizonte"),
    (4, "Ana", 22, "Porto Alegre")
]

# Inserindo as linhas na tabela
for dado in dados:
    tabela.insert("", "end", values=dado)

# Exibindo a tabela
tabela.pack(padx=10, pady=10)

# Iniciando a interface gráfica
root.mainloop()
