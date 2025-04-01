import tkinter as tk
import tkinter.ttk
import customtkinter
import sqlite3

# Configuração inicial do CustomTkinter
customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("blue")


# Função para criar a tabela no banco de dados
def criar_cadastro():
    conexao_cadastro = sqlite3.connect("Banco estoque.db")
    terminal_cadastro = conexao_cadastro.cursor()
    terminal_cadastro.execute("CREATE TABLE IF NOT EXISTS cadastro(nome TEXT, preco REAL, descricao TEXT)")
    conexao_cadastro.commit()
    conexao_cadastro.close()


# Função para salvar o cadastro no banco de dados
def salvar_cadastro():
    conexao_cadastro = sqlite3.connect("Banco estoque.db")
    terminal_cadastro = conexao_cadastro.cursor()

    # Inserir os dados no banco de dados
    terminal_cadastro.execute("INSERT INTO cadastro (nome, preco, descricao) VALUES (?, ?, ?)",
                              (Produto.get(), float(Preco.get()), Descricao.get("1.0", "end-1c")))

    conexao_cadastro.commit()
    conexao_cadastro.close()

    # Limpar os campos após salvar
    Produto.delete(0, tk.END)
    Preco.delete(0, tk.END)
    Descricao.delete("1.0", tk.END)

    # Atualizar a tabela no frame de relatório
    ler_cadastro()


# Função para ler os dados do banco de dados e exibi-los na tabela
def ler_cadastro():
    conexao_cadastro = sqlite3.connect("Banco estoque.db")
    terminal_cadastro = conexao_cadastro.cursor()
    terminal_cadastro.execute("SELECT * FROM cadastro")
    receber_cadastro = terminal_cadastro.fetchall()

    # Limpar a tabela antes de inserir novos dados
    for row in tabela.get_children():
        tabela.delete(row)

    # Inserir os dados na tabela
    for i in receber_cadastro:
        nome = str(i[0])
        preco = "R$" + str(i[1])
        descricao = str(i[2])
        tabela.insert("", tk.END, values=(nome, preco, descricao))

    conexao_cadastro.close()


# Funções para alternar entre os frames
def Tela_Cadastrar():
    Frame_Editar.grid_forget()
    Frame_Saida.grid_forget()
    Frame_Entrada.grid_forget()
    Frame_Relatorio.grid_forget()
    Frame_B_Relatorio_Saida.grid_forget()
    Frame_B_Relatorio_Entrada.grid_forget()
    Frame_Cadastro.grid_propagate(False)
    Frame_Cadastro.grid(row=0, column=1, padx=5, pady=5)


def Tela_Editar():
    Frame_Cadastro.grid_forget()
    Frame_Saida.grid_forget()
    Frame_Entrada.grid_forget()
    Frame_Relatorio.grid_forget()
    Frame_B_Relatorio_Saida.grid_forget()
    Frame_B_Relatorio_Entrada.grid_forget()
    Frame_Editar.grid_propagate(False)
    Frame_Editar.grid(row=0, column=1, padx=5, pady=5)


def Tela_Saída():
    Frame_Cadastro.grid_forget()
    Frame_Editar.grid_forget()
    Frame_Entrada.grid_forget()
    Frame_Relatorio.grid_forget()
    Frame_B_Relatorio_Saida.grid_forget()
    Frame_B_Relatorio_Entrada.grid_forget()
    Frame_Saida.grid_propagate(False)
    Frame_Saida.grid(row=0, column=1, padx=5, pady=5)


def Tela_Entrada():
    Frame_Cadastro.grid_forget()
    Frame_Editar.grid_forget()
    Frame_Saida.grid_forget()
    Frame_Relatorio.grid_forget()
    Frame_B_Relatorio_Saida.grid_forget()
    Frame_B_Relatorio_Entrada.grid_forget()
    Frame_Entrada.grid_propagate(False)
    Frame_Entrada.grid(row=0, column=1, padx=5, pady=5)


def Tela_Relatorio():
    Frame_Cadastro.grid_forget()
    Frame_Editar.grid_forget()
    Frame_Saida.grid_forget()
    Frame_Entrada.grid_forget()
    Frame_B_Relatorio_Saida.grid_forget()
    Frame_B_Relatorio_Entrada.grid_forget()
    Frame_Relatorio.grid_propagate(False)
    Frame_Relatorio.grid(row=0, column=1, padx=5, pady=5)

    # Atualizar a tabela ao abrir o frame de relatório
    ler_cadastro()


# Janela principal
janela = customtkinter.CTk()
janela.title("Projeto")
janela.geometry("800x400")

# Frame do lado esquerdo (menu)
Frame_LadoEsquerdo = customtkinter.CTkFrame(janela, fg_color="Light green", width=190, height=380, corner_radius=0)
Frame_LadoEsquerdo.grid_propagate(False)
Frame_LadoEsquerdo.grid(row=0, column=0, padx=5, pady=10)

Label_NewSistem = customtkinter.CTkLabel(Frame_LadoEsquerdo, width=190, text="Novo Sistema", text_color="blue",
                                         font=("Couvier", 18))
Label_NewSistem.grid(padx=10, pady=20, row=0, column=0)

Botao_Cadastrar = customtkinter.CTkButton(Frame_LadoEsquerdo, text="Cadastrar", font=("Couvier", 16), corner_radius=0,
                                          command=Tela_Cadastrar)
Botao_Cadastrar.grid(pady=5, row=1, column=0)

Botao_Editar = customtkinter.CTkButton(Frame_LadoEsquerdo, text="Editar", font=("Couvier", 16), corner_radius=0,
                                       command=Tela_Editar)
Botao_Editar.grid(pady=5, row=2, column=0)

Botao_Saida = customtkinter.CTkButton(Frame_LadoEsquerdo, text="Saída", font=("Couvier", 16), corner_radius=0,
                                      command=Tela_Saída)
Botao_Saida.grid(pady=5, row=3, column=0)

Botao_Entrada = customtkinter.CTkButton(Frame_LadoEsquerdo, text="Entrada", font=("Couvier", 16), corner_radius=0,
                                        command=Tela_Entrada)
Botao_Entrada.grid(pady=5, row=4, column=0)

Botao_Relatorio = customtkinter.CTkButton(Frame_LadoEsquerdo, text="Relátorio", font=("Couvier", 16), corner_radius=0,
                                          command=Tela_Relatorio)
Botao_Relatorio.grid(pady=5, row=5, column=0)

# Frame de Cadastro
Frame_Cadastro = customtkinter.CTkFrame(janela, fg_color="Dark red", width=590, height=380, corner_radius=0)
Frame_Cadastro.grid_propagate(False)

Texto1 = customtkinter.CTkLabel(Frame_Cadastro, text="Cadastro do Produto", text_color="Black", font=("Couvier", 18))
Texto1.grid(padx=10, pady=20, row=0, column=1)

mensagem_NameProduct = customtkinter.CTkLabel(Frame_Cadastro, text="Nome do Produto:", text_color="black")
mensagem_NameProduct.grid(padx=5, pady=5, row=1, column=0, stick="ne")

mensagem_Preco = customtkinter.CTkLabel(Frame_Cadastro, text="Preço(R$):", text_color="black")
mensagem_Preco.grid(padx=5, pady=5, row=2, column=0, stick="ne")

mensagem_Descrition = customtkinter.CTkLabel(Frame_Cadastro, text="Descrição:", text_color="black")
mensagem_Descrition.grid(padx=5, pady=5, row=3, column=0, stick="ne")

Produto = customtkinter.CTkEntry(Frame_Cadastro, placeholder_text="Digite o nome do produto :", width=300)
Produto.grid(padx=5, pady=5, row=1, column=1)

Preco = customtkinter.CTkEntry(Frame_Cadastro, placeholder_text="0.00", width=80)
Preco.grid(padx=5, pady=5, row=2, column=1, stick="w")

Descricao = customtkinter.CTkTextbox(Frame_Cadastro, width=300, height=80)
Descricao.grid(padx=5, pady=5, row=3, column=1, stick="ne")

Salvar = customtkinter.CTkButton(Frame_Cadastro, text="Salvar", width=80, fg_color="black", hover_color="#E65829",
                                 command=salvar_cadastro)
Salvar.grid(padx=5, pady=5, row=4, column=1, stick="e")

# Frame de Relatório
Frame_Relatorio = customtkinter.CTkFrame(janela, fg_color="Dark red", width=590, height=380, corner_radius=0)
Frame_Relatorio.grid_propagate(False)

Label_Relatorion = customtkinter.CTkLabel(Frame_Relatorio, text=" Estoque Relatório", text_color="Black",
                                          font=("Couvier", 16))
Label_Relatorion.grid(padx=0, pady=20, row=0, column=0, columnspan=4)

tabela = tkinter.ttk.Treeview(Frame_Relatorio, columns=("NOME", "PREÇO", "DESCRIÇÃO"), show="headings", height=5)
tabela.heading("NOME", text="NOME")
tabela.column("NOME", width=110)
tabela.heading("PREÇO", text="PREÇO")
tabela.column("PREÇO", width=110)
tabela.heading("DESCRIÇÃO", text="DESCRIÇÃO")
tabela.column("DESCRIÇÃO", width=110)

scroll = tkinter.ttk.Scrollbar(Frame_Relatorio, orient="vertical", command=tabela.yview)
tabela.grid(row=2, column=0, columnspan=4, sticky="nsew")

# Configuração do grid do frame de relatório
Frame_Relatorio.grid_columnconfigure(0, weight=1)
Frame_Relatorio.grid_rowconfigure(2, weight=1)

# Inicialização do banco de dados
criar_cadastro()

# Iniciar a aplicação
janela.mainloop()