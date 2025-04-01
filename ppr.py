import tkinter as tk
import customtkinter
from tkinter import ttk

# Função fictícia de exportação
def abrir_janela2():
    print("Exportando...")

# Criando a janela principal
root = tk.Tk()
root.title("Estoque Relatório")

# Criando o Frame_06
Frame_06 = customtkinter.CTkFrame(root, width=590, height=380)
Frame_06.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

# Configurando a grid do Frame para expandir corretamente
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

# Título
Label_titulo5 = customtkinter.CTkLabel(Frame_06, text="Estoque Relatório", text_color="Black", font=("Couvier", 16))
Label_titulo5.grid(padx=0, pady=20, row=0, column=0, columnspan=4)

# Campo de busca
Buscar_Relatorio = customtkinter.CTkEntry(Frame_06, placeholder_text="Buscar produto", width=230)
Buscar_Relatorio.grid(padx=5, pady=5, row=1, column=0, sticky="w")

# Botão de exportação
Exportar = customtkinter.CTkButton(Frame_06, text="Exportar", fg_color="Blue", font=("Couvier", 16), width=80, command=abrir_janela2)
Exportar.grid(padx=5, pady=5, row=1, column=3)

# Textbox (não muito claro como usá-lo, mas incluído no layout)
Estoque_R = customtkinter.CTkTextbox(Frame_06)
Estoque_R.grid(pady=5, padx=5, row=2, column=0, columnspan=4, sticky="nsew")

# Definindo as colunas para a tabela
coluna = ("Nome", "Idade", "Preço", "Estado")

# Criando a tabela Treeview
tabela = ttk.Treeview(Frame_06, columns=coluna, show="headings")

# Configurando os cabeçalhos da tabela
for col in coluna:
    tabela.heading(col, text=col)

# Dados para a tabela
dados = [
    ("Fone X", 25, 90.99, "Novo"),
    ("Iphone 17", 30, 87.00, "Novo"),
    ("Notebook", 28, 47.000, "Novo"),
    ("Estiligue", 22, 15.00, "Novo")
]

# Inserindo as linhas de dados
for dado in dados:
    tabela.insert("", "end", values=dado)

# Exibindo a tabela
tabela.grid(pady=5, padx=5, row=3, column=0, columnspan=4, sticky="nsew")

# Iniciando a interface gráfica
root.mainloop()
