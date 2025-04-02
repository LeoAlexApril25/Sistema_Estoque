import tkinter
import tkinter as tk
import tkinter.ttk
import customtkinter
import sqlite3

produto_selecionado_entrada = None
produto_selecionado_saida = None


'''items = ["Opcão1", "Opção2", "Opção3", "Opcão4", "Opção5", "Opção6"]'''
items1 = ["1", "2", "3", "4", "5", "6"]
items2 = ["1", "2", "3", "4", "5", "6"]
coluna = ["NOME","QUANTIDADE","PREÇO","DESCRIÇÃO"]
coluna_saida = ["Nome", "Quantidade", "Data/hora"]
coluna_entrada = ["Nome", "Quantidade", "Data/hora"]

customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("blue")

def criar_cadastro():
    conexao_cadastro = sqlite3.connect("Banco estoque.db")
    terminal_cadastro_sql = conexao_cadastro.cursor()
    terminal_cadastro_sql.execute(f"CREATE TABLE IF NOT EXISTS cadastro(nome text,quantidade decimal, preco decimal, descricao text)")
    conexao_cadastro.commit()
    conexao_cadastro.close()

def limpar_campos_cadastro():
    Produto.delete(0, tk.END) #Limpa campo do Produto
    Preco.delete(0, tk.END) #Limpa o campo de preço
    Descricao.delete('1.0', tk.END) #Limpa o campo de descrição

def salvar_cadastro():
    conexao_cadastro = sqlite3.connect("Banco estoque.db")
    terminal_cadastro_sql = conexao_cadastro.cursor()
    terminal_cadastro_sql.execute(f"INSERT INTO cadastro(nome,quantidade, descricao, preco) VALUES ('{Produto.get()}','{0}',' {str(Descricao.get('1.0','end'))}','{float(Preco.get())}')")
    conexao_cadastro.commit()
    conexao_cadastro.close()

    limpar_campos_cadastro() #Limpa os campos após salvar


def ler_cadastro():
    conexao_cadastro = sqlite3.connect("Banco estoque.db")
    terminal_cadastro_sql = conexao_cadastro.cursor()
    terminal_cadastro_sql.execute("SELECT * FROM cadastro")
    receber_cadastro = terminal_cadastro_sql.fetchall()

    for row in tabela.get_children(): # Usando para impedir o botão relatorio que fica repetindo dados já inseridos no botão cadastro
        tabela.delete(row)

    for i in receber_cadastro:
        nome = str(i[0])
        quantidade = str(i[1])
        preco = "R$" + str(i[2])
        descricao = str(i[3])

        tabela.insert("", tk.END, values=(nome, quantidade, preco, descricao))
        conexao_cadastro.close()

criar_cadastro()

def obter_nomes_produtos():
    conexao_cadastro = sqlite3.connect("Banco estoque.db")
    terminal_cadastro_sql = conexao_cadastro.cursor()
    terminal_cadastro_sql.execute("SELECT nome, preco, descricao FROM cadastro")
    nomes = terminal_cadastro_sql.fetchall()
    conexao_cadastro.close()
    return [nome[0] for nome in nomes]

#
def atualizar_scrollframe(frame):

    # Limpa o frame antes de adicionar novos itens
    for widget in frame.winfo_children():
        widget.destroy()

    # Obtém os nomes dos produtos do banco
    produtos = obter_nomes_produtos()

    # Adiciona cada produto ao frame com a função de callback
    for produto in produtos:
        # Cria uma variável de controle
        var = tk.IntVar(value=0)  # Inicia desmarcado

        # Cria o checkbox com a função de callback
        box = customtkinter.CTkCheckBox(
            frame,
            text=produto,
            variable=var,
            command=lambda p=produto, v=var: insere_dados(p, frame) if v.get() == 1 else None
        )
        box.grid(pady=5, sticky="w")

def limpar_campo_edicao():
    Editar_dados.delete(0,tk.END)
    Editar_preco.delete(0,tk.END)
    Editar_descricao.delete('1.0',tk.END)

global  Editar_dados, Editar_preco, Editar_descricao

def seleciona_item(arg_item,arg_list):
    global valor_checkbox
    valor_checkbox = arg_item.get().strip("(),'\"")
    conexao_cadastro = sqlite3.connect("Banco estoque.db")
    terminal_sql_cadastro = conexao_cadastro.cursor()
    terminal_sql_cadastro.execute(f"SELECT*FROM produto WHERE nome ='{valor_checkbox}")
    receber_dados_produto = terminal_sql_cadastro.fetchall()
    inserir_dados(receber_dados_produto, arg_list)

def insere_dados(nome_produto, frame):
    global nome_original
    conexao_cadastro = sqlite3.connect("Banco estoque.db")
    terminal_cadastro_sql = conexao_cadastro.cursor()
    terminal_cadastro_sql.execute(f"SELECT * FROM cadastro WHERE nome = '{nome_produto}'")
    dados_produto = terminal_cadastro_sql.fetchall()
    print(frame)
    if frame == Produto_T:
        nome_original = dados_produto[0][0]
        Editar_dados.insert(0, dados_produto[0][0])
        Editar_preco.insert(0, dados_produto[0][2])
        Editar_descricao.insert(0.0, dados_produto[0][3])

def deletar_produtos(nome_produto):
    conexao_cadastro = sqlite3.connect("Banco estoque.db")
    terminal_cadastro_sql = conexao_cadastro.cursor()
    terminal_cadastro_sql.execute(f"DELETE FROM cadastro WHERE nome ='{nome_produto}'")
    conexao_cadastro.commit()
    conexao_cadastro.close()
    Editar_dados.delete(0, "end")
    Editar_preco.delete(0, "end")
    Editar_descricao.delete(0.0, "end")
    atualizar_scrollframe(Produto_T)

def editar_dados(nome_produto,preco_produto,descricao_produto):
    conexao_cadastro = sqlite3.connect("Banco estoque.db")
    terminal_sql_cadastro = conexao_cadastro.cursor()
    terminal_sql_cadastro.execute(f"UPDATE cadastro SET nome = '{nome_produto}',preco = '{preco_produto}', descricao = '{descricao_produto}' WHERE nome ='{nome_original}'")
    conexao_cadastro.commit()
    conexao_cadastro.close()
    Editar_dados.delete(0, "end")
    Editar_preco.delete(0, "end")
    Editar_descricao.delete(0.0, "end")
    atualizar_scrollframe(Produto_T)

def obter_nomes_produto_saida():
    conexao_cadastro = sqlite3.connect("Banco estoque.db")
    terminal_cadastro_sql = conexao_cadastro.cursor()
    terminal_cadastro_sql.execute("SELECT nome, quantidade FROM cadastro")
    nomes = terminal_cadastro_sql.fetchall()
    conexao_cadastro.close()
    return [nome[0] for nome in nomes]

def atualizar_scrollframe_saida(frame):


    for widget in frame.winfo_children():
        widget.destroy()

    produtos = obter_nomes_produto_saida()


    for produto in produtos:

        var = tk.IntVar(value=0)


        box1 = customtkinter.CTkCheckBox(
            frame,
            text=produto,
            variable=var,
            command=lambda p=produto, v=var: inserir_dados(p, frame) if v.get() == 1 else None
        )
        box1.grid(pady=5, sticky="w")

def inserir_dados(nome_produto, frame):
    global produto_selecionado_saida
    conexao_cadastro = sqlite3.connect("Banco estoque.db")
    terminal_cadastro_sql = conexao_cadastro.cursor()
    terminal_cadastro_sql.execute(f"SELECT * FROM cadastro WHERE nome = '{nome_produto}'")
    dados_produto = terminal_cadastro_sql.fetchall()
    print(frame)

    if frame == Produto_S:
        produto_selecionado_saida = dados_produto[0]
        Nome_quantidade.delete(0,tk.END)
        Nome_quantidade.insert(0, dados_produto[0][0])
        Quantidade_R.delete(0, tk.END)
        Quantidade_R.insert(0, dados_produto[0][1])


def adicionar_item_saida():
    global produto_selecionado_saida

    if produto_selecionado_saida is None:
        print("❌ Nenhum produto selecionado!")
        return

    quantidade_retirada = Quantidade_R.get().strip()

    if not quantidade_retirada.isdigit():
        print("❌ Quantidade inválida! Digite um número.")
        return

    quantidade_recebida = int(quantidade_retirada)

    texto_item = f"{produto_selecionado_saida[0]} | Qtd: {quantidade_retirada}"

    create_line(Entrada_frame, texto_item, len(Entrada_frame.winfo_children()) // 2 + 1)

    Quantidade_R.delete(0, tk.END)
    produto_selecionado_saida = None
    Nome_quantidade.delete(0, tk.END)


def obter_nomes_produto_entrada():
    conexao_cadastro = sqlite3.connect("Banco estoque.db")
    terminal_cadastro_sql = conexao_cadastro.cursor()
    terminal_cadastro_sql.execute("SELECT nome, quantidade FROM cadastro")
    nomes = terminal_cadastro_sql.fetchall()
    conexao_cadastro.close()
    return [nome[0] for nome in nomes]

def atualizar_scrollframe_entrada(frame):


    for widget in frame.winfo_children():
        widget.destroy()

    produtos = obter_nomes_produto_entrada()


    for produto in produtos:

        var = tk.IntVar(value=0)


        box2 = customtkinter.CTkCheckBox(
            frame,
            text=produto,
            variable=var,
            command=lambda p=produto, v=var: inserir_dados_entrada(p, frame) if v.get() == 1 else None
        )
        box2.grid(pady=5, sticky="w")


def inserir_dados_entrada(nome_produto, frame):
    global produto_selecionado_entrada

    conexao_cadastro = sqlite3.connect("Banco estoque.db")
    terminal_cadastro_sql = conexao_cadastro.cursor()
    terminal_cadastro_sql.execute(f"SELECT * FROM cadastro WHERE nome = '{nome_produto}'")
    dados_produto = terminal_cadastro_sql.fetchall()
    conexao_cadastro.close()

    if frame == Produto_E:
        produto_selecionado_entrada = dados_produto[0]  # Armazena o produto
        Nome_quantidadeE.delete(0, tk.END)
        Nome_quantidadeE.insert(0, dados_produto[0][0])
        Quantidade_E.delete(0, tk.END)
        Quantidade_E.insert(0, str(dados_produto[0][1]))


def adicionar_item_entrada():
    global produto_selecionado_entrada

    if produto_selecionado_entrada is None:
        print("❌ Nenhum produto selecionado!")
        return

    quantidade_recebida = Quantidade_E.get().strip()

    if not quantidade_recebida.isdigit():
        print("❌ Quantidade inválida! Digite um número.")
        return

    quantidade_recebida = int(quantidade_recebida)


    texto_item = f"{produto_selecionado_entrada[0]} | Qtd: {quantidade_recebida}"


    create_line(Entrada_frame, texto_item, len(Entrada_frame.winfo_children()) // 2 + 1)


    Quantidade_E.delete(0, tk.END)
    produto_selecionado_entrada = None
    Nome_quantidadeE.delete(0, tk.END)

def cancelar_edicao():
    limpar_campo_edicao()


def Tela_Cadastrar():
    Frame_Editar.grid_forget()
    Frame_Saida.grid_forget()
    Frame_Entrada.grid_forget()
    Frame_Relatorio.grid_forget()
    Frame_B_Relatorio_Saida.grid_forget()
    Frame_B_Relatorio_Entrada.grid_forget()
    Frame_Cadastro.grid_propagate(False)
    Frame_Cadastro.grid(row=0, column=1, padx=5, pady=5)
    if hasattr(Frame_Cadastro, 'produtos_frame'):
        atualizar_scrollframe(Frame_Cadastro.produtos_frame)


def Tela_Editar():
    Frame_Cadastro.grid_forget()
    Frame_Saida.grid_forget()
    Frame_Entrada.grid_forget()
    Frame_Relatorio.grid_forget()
    Frame_B_Relatorio_Saida.grid_forget()
    Frame_B_Relatorio_Entrada.grid_forget()
    Frame_Editar.grid_propagate(False)
    Frame_Editar.grid(row=0, column=1, padx=5, pady=5)
    atualizar_scrollframe(Produto_T)

def Tela_Saída():
    Frame_Cadastro.grid_forget()
    Frame_Editar.grid_forget()
    Frame_Entrada.grid_forget()
    Frame_Relatorio.grid_forget()
    Frame_B_Relatorio_Saida.grid_forget()
    Frame_B_Relatorio_Entrada.grid_forget()
    Frame_Saida.grid_propagate(False)
    Frame_Saida.grid(row=0, column=1, padx=5, pady=5)
    #atualizar_scrollframe(Produto_S)
    atualizar_scrollframe_saida(Produto_S)

def Tela_Entrada():
    Frame_Cadastro.grid_forget()
    Frame_Editar.grid_forget()
    Frame_Saida.grid_forget()
    Frame_Relatorio.grid_forget()
    Frame_B_Relatorio_Saida.grid_forget()
    Frame_B_Relatorio_Entrada.grid_forget()
    Frame_Entrada.grid_propagate(False)
    Frame_Entrada.grid(row=0, column=1, padx=5, pady=5)
    #atualizar_scrollframe(Produto_E)
    atualizar_scrollframe_entrada(Produto_E)

def Tela_Relatorio():
    Frame_Cadastro.grid_forget()
    Frame_Editar.grid_forget()
    Frame_Saida.grid_forget()
    Frame_Entrada.grid_forget()
    Frame_B_Relatorio_Saida.grid_forget()
    Frame_B_Relatorio_Entrada.grid_forget()
    Frame_Relatorio.grid_propagate(False)
    Frame_Relatorio.grid(row=0, column=1, padx=5, pady=5)
    ler_cadastro()

def on_trash_icon_click(item_num):
    print(f"Ícone de lixeira da linha {item_num} clicado!")


def create_line(frame, text, item_num):
    linha_frame = customtkinter.CTkFrame(frame)
    linha_frame.grid(row=item_num, column=0, columnspan=2, sticky="ew", pady=2)

    # Label com o texto do item
    label = customtkinter.CTkLabel(linha_frame, text=text, anchor="w")
    label.pack(side="left", padx=5, fill="x", expand=True)

    # Botão de lixeira para remover
    trash_icon = customtkinter.CTkButton(
        linha_frame,
        text="🗑️",
        width=40, height=20,
        command=lambda: linha_frame.destroy()  # Remove a linha
    )
    trash_icon.pack(side="right", padx=5)

    line_frame.grid_columnconfigure(0, weight=1)
    line_frame.grid_columnconfigure(1, weight=1)

def on_trash_icon_click2(item1_num):
    print(f"Ícone de lixeira da linha {item1_num} clicado!")

def create_line_entrada(frame, text, item_num):
    linha_frame_saida = customtkinter.CTkFrame(frame)
    linha_frame_saida.grid(row=item_num, column=0, columnspan=2, sticky="ew", pady=2)

    # Label com o texto do item
    label = customtkinter.CTkLabel(Entrada_frame, text=text, anchor="w")
    label.pack(side="left", padx=5, fill="x", expand=True)

    # Botão de lixeira para remover
    trash_icon = customtkinter.CTkButton(
        Entrada_frame,
        text="🗑️",
        width=40, height=20,
        command=lambda: Entrada_frame.destroy()  # Remove a linha
    )
    trash_icon.pack(side="right", padx=5)

    Entrada_frame.grid_columnconfigure(0, weight=1)
    Entrada_frame.grid_columnconfigure(1, weight=1)

def Tela_B_estoque():
    Frame_B_Relatorio_Saida.grid_forget()
    Frame_B_Relatorio_Entrada.grid_forget()
    Frame_Relatorio.grid_propagate(False)
    Frame_Relatorio.grid(row=0, column=1, padx=5, pady=5)

def Tela_B_saida():
    Frame_Relatorio.grid_forget()
    Frame_B_Relatorio_Entrada.grid_forget()
    Frame_B_Relatorio_Saida.grid_propagate(False)
    Frame_B_Relatorio_Saida.grid(row=0, column=1, padx=5, pady=5)

def Tela_B_entrada():
    Frame_Relatorio.grid_forget()
    Frame_B_Relatorio_Saida.grid_forget()
    Frame_B_Relatorio_Entrada.grid_propagate(False)
    Frame_B_Relatorio_Entrada.grid(row=0, column=1, padx=5, pady=5)

janela2 = None

def abrir_janela2():
    global janela2
    if janela2 is None or not janela2.winfo_exists():
        janela2 = customtkinter.CTkToplevel()
        janela2.geometry("590x380")
        janela2.title("Projeto")

        label_relatorio = customtkinter.CTkLabel(janela2, text="Escolher relatório(s):",text_color="#A8B30F")
        label_relatorio.grid(row=1, column=0, pady=20, padx=20, sticky="w")

        exportar_estoque = customtkinter.CTkCheckBox(janela2, text="Exportar Estoque")
        exportar_estoque.grid(row=2, column=0, pady=20, padx=20, sticky="w")

        exportar_saida = customtkinter.CTkCheckBox(janela2, text="Exportar Saída")
        exportar_saida.grid(row=3, column=0, pady=20, padx=20, sticky="w")

        exportar_entrada = customtkinter.CTkCheckBox(janela2, text="Exportar Entrada")
        exportar_entrada.grid(row=4, column=0, pady=20, padx=20, sticky="w")

        #titulo escolher extenção

        label_extencao = customtkinter.CTkLabel(janela2,text="Escolher extensão:", text_color="#A8B30F")
        label_extencao.grid(row=1, column=2, pady=20, padx=100, sticky="w")

        # Caixas para formatos de arquivo
        formato_word = customtkinter.CTkCheckBox(janela2, text="Word")
        formato_word.grid(row=2, column=2, pady=20, padx=100, sticky="w")

        formato_pdf = customtkinter.CTkCheckBox(janela2, text="PDF")
        formato_pdf.grid(row=3, column=2, pady=20, padx=100, sticky="w")

        formato_excel = customtkinter.CTkCheckBox(janela2, text="Excel")
        formato_excel.grid(row=4, column=2, pady=20, padx=100, sticky="w")

        # botoes

        salvar_popup = customtkinter.CTkButton(janela2, text="salvar", width=100)
        salvar_popup.grid(row=5, column=2, pady=5, padx=0, sticky="w")

        cancelar_popup = customtkinter.CTkButton(janela2, text="cancelar", width=100)
        cancelar_popup.grid(row=5, column=1, pady=5, padx=20, sticky="w")

        janela2.protocol("NM_DELETE_WINDOW", fechar_janela2)
        janela2.attributes("-topmost", 1) # Faz o janela dois ficar na frente

    else:
        janela2.lift()

def fechar_janela2():
    global janela2
    if janela2 is not None:
        janela2.destroy()
        janela2 = None



janela = customtkinter.CTk()
janela.title("Projeto")
janela.geometry("800x400")


# Dados da Janela e botões, exatamente Frame 1
# Frame 1

Frame_LadoEsquerdo = customtkinter.CTkFrame(janela, fg_color="Light green", width=190, height=380, corner_radius=0)
Frame_LadoEsquerdo.grid_propagate(False)
Frame_LadoEsquerdo.grid(row=0, column=0, padx=5, pady=10)

Frame_LadoEsquerdo.grid(row=0, column=0, padx=5, pady=10)
Label_NewSistem = customtkinter.CTkLabel(Frame_LadoEsquerdo, width=190,  text="Novo Sistema", text_color="blue", font=("Couvier", 18))
Label_NewSistem.grid(padx=10, pady=20, row=0, column=0)

Botao_Cadastrar = customtkinter.CTkButton(Frame_LadoEsquerdo, text="Cadastrar", font=("Couvier", 16), corner_radius=0, command=Tela_Cadastrar)
Botao_Cadastrar.grid(pady=5, row=1, column=0)

Botao_Editar = customtkinter.CTkButton(Frame_LadoEsquerdo, text="Editar", font=("Couvier", 16), corner_radius=0, command=Tela_Editar)
Botao_Editar.grid(pady=5, row=2, column=0)

Botao_Saida = customtkinter.CTkButton(Frame_LadoEsquerdo, text="Saída", font=("Couvier", 16), corner_radius=0, command=Tela_Saída)
Botao_Saida.grid(pady=5, row=3, column=0)

Botao_Entrada = customtkinter.CTkButton(Frame_LadoEsquerdo,  text="Entrada", font=("Couvier", 16), corner_radius=0, command=Tela_Entrada)
Botao_Entrada.grid(pady=5, row=4, column=0)

Botao_Relatorio = customtkinter.CTkButton(Frame_LadoEsquerdo, text="Relátorio", font=("Couvier", 16), corner_radius=0, command=Tela_Relatorio)
Botao_Relatorio.grid(pady=5, row=5, column=0)

# dados do botão Tela de cadastro
# Frame 2

Frame_Cadastro = customtkinter.CTkFrame(janela, fg_color="Dark red", width=590, height=380, corner_radius=0)
Frame_Cadastro.grid_propagate(False)
Frame_Cadastro.grid(row=0, column=1, padx=5, pady=5)

Texto1 = customtkinter.CTkLabel(Frame_Cadastro, text="Cadastro do Produto", text_color="Black", font=("Couvier", 18))
Texto1.grid(padx=10, pady=20, row=0, column=1)

mensagem_NameProduct = customtkinter.CTkLabel(Frame_Cadastro, text="Nome do Produto:", text_color="black")
mensagem_NameProduct.grid(padx=5, pady=5, row=1, column=0, stick="ne")

mensagem_Preco = customtkinter.CTkLabel(Frame_Cadastro, text="Preço(R$):", text_color="black" )
mensagem_Preco.grid(padx=5, pady=5, row=2, column=0, stick="ne")


mensagem_Descrition = customtkinter.CTkLabel(Frame_Cadastro, text="Descrição:", text_color="black")
mensagem_Descrition.grid(padx=5, pady=5, row=3, column=0, stick="ne")

Produto = customtkinter.CTkEntry(Frame_Cadastro, placeholder_text="Digite o nome do produto :", width=300)
Produto.grid(padx=5, pady=5, row=1, column=1)

Preco = customtkinter.CTkEntry(Frame_Cadastro, placeholder_text=("0.00"), width=80)
Preco.grid(padx=5, pady=5, row=2, column=1, stick="w")


Descricao = customtkinter.CTkTextbox(Frame_Cadastro, width=300, height=80)
Descricao.grid(padx=5, pady=5, row=3, column=1, stick="ne")

Salvar = customtkinter.CTkButton(Frame_Cadastro, text="Salvar", width=80, fg_color="black", hover_color="#E65829", command=salvar_cadastro)
Salvar.grid(padx=5, pady=5, row=4, column=1, stick="e")

# columnspan ele centraliza o título no espaçamento onde fica tabuada/linhas e outras informações do outro lado
# Frame 3

Frame_Editar = customtkinter.CTkFrame(janela, fg_color="Dark red", width=590, height=380, corner_radius=0)
Frame_Editar.grid_propagate(False)

Label_EditionProduction = customtkinter.CTkLabel(Frame_Editar, text="Editar produtos cadastrados:", text_color="Black", font=("Couvier", 16))
Label_EditionProduction.grid(padx=0, pady=20, row=0, column=0, columnspan=4)

Buscar_produto = customtkinter.CTkEntry(Frame_Editar, placeholder_text="Informar produto", font=("Couvier", 16), width=230)
Buscar_produto.grid(padx=20, pady=20, row=1, column=0, columnspan=4, stick="w")

Editar_dados = customtkinter.CTkEntry(Frame_Editar, placeholder_text="Editar dados:", font=("Couvier", 16))
Editar_dados.grid(padx=5, pady=0, row=1, column=1, stick="w", columnspan=3)

Editar_preco = customtkinter.CTkEntry(Frame_Editar, placeholder_text="0.00:", width=80)
Editar_preco.grid(padx=5, pady=0, row=2, column=1, stick="w", columnspan=3)

Editar_descricao = customtkinter.CTkTextbox(Frame_Editar, width=300, height=120, fg_color="black")
Editar_descricao.grid(padx=5, pady=0, row=3, column=1, stick="w", columnspan=3)

# rowspan é resposavel as linhas da coluna
Produto_T = customtkinter.CTkScrollableFrame(Frame_Editar)
Produto_T.grid(pady=0, padx=20, row=2, column=0, rowspan=4)

Excluir = customtkinter.CTkButton(Frame_Editar, text="Excluir", width=80, fg_color="Red", hover_color="Blue",command = lambda : deletar_produtos(Editar_dados.get()))
Excluir.grid(padx=5, pady=5, stick="w", row=5, column=1)

Cancelar = customtkinter.CTkButton(Frame_Editar, text="Cancelar", width=80, fg_color="Purple", hover_color="Blue", command=cancelar_edicao)
Cancelar.grid(padx=0, pady=5, row=5, column=2)

Salvar = customtkinter.CTkButton(Frame_Editar, text="Salvar", width=80, fg_color="Purple", hover_color="Blue", command = lambda : editar_dados(Editar_dados.get(), Editar_preco.get(), Editar_descricao.get(1.0, "end")))
Salvar.grid(padx=5, pady=5, stick="e", row=5, column=3)

#Frame04

Frame_Saida = customtkinter.CTkFrame(janela, fg_color="Dark red", width=590, height=380, corner_radius=0)
Frame_Saida.grid_propagate(False)

Label_ExitProduction = customtkinter.CTkLabel(Frame_Saida, text="Saída de Produto", text_color="Black", font=("Couvier", 16))
Label_ExitProduction.grid(padx=0, pady=20, row=0, column=0, columnspan=3)

Campo_busca = customtkinter.CTkEntry(Frame_Saida, placeholder_text="Buscar", width=230)
Campo_busca.grid(padx=20, pady=20, row=1, column=0, stick="w")

Nome_quantidade = customtkinter.CTkEntry(Frame_Saida, placeholder_text="Nome do produto", width=230)
Nome_quantidade.grid(padx=5, pady=0, row=1, column=1, columnspan=2)

Produto_S = customtkinter.CTkScrollableFrame(Frame_Saida)
Produto_S.grid(pady=0, padx=20, row=2, column=0, rowspan=3)

Quantidade_R = customtkinter.CTkEntry(Frame_Saida, placeholder_text="Quatidade retirada", width=90)
Quantidade_R.grid(padx=5, pady=0, row=2, column=1, stick="w")

item_B = customtkinter.CTkButton(Frame_Saida, text="Adic item", fg_color="Blue", font=("Couvier", 16), width=130, command=adicionar_item_saida)
item_B.grid(padx=5, pady=5, row=2, column=2, stick="e")

line_frame = customtkinter.CTkFrame(Frame_Saida, width=230)
line_frame.grid(padx=5, pady=0, row=3, column=1, columnspan=3, stick="we")

Cancelar_saida = customtkinter.CTkButton(Frame_Saida, text="Cancelar", fg_color="Blue", font=("Couvier", 16), width=80)
Cancelar_saida.grid(padx=5, pady=0, stick="w", row=4, column=1)

S_saida = customtkinter.CTkButton(Frame_Saida, text="Saida", fg_color="Blue", font=("Couvier", 16), width=80)
S_saida.grid(padx=5, pady=0, stick="e", row=4, column=2)

# frame05
Frame_Entrada = customtkinter.CTkFrame(janela, fg_color="Dark red", width=590, height=380, corner_radius=0)
Frame_Entrada.grid_propagate(False)

Label_Entrada = customtkinter.CTkLabel(Frame_Entrada, text="Entrada", text_color="Black", font=("Couvier", 16))
Label_Entrada.grid(padx=0, pady=20, row=0, column=0, columnspan=3)

Campo_busca_E = customtkinter.CTkEntry(Frame_Entrada, placeholder_text="Buscar", width=230)
Campo_busca_E.grid(padx=20, pady=20, row=1, column=0, stick="w")

Nome_quantidadeE = customtkinter.CTkEntry(Frame_Entrada, placeholder_text="Quantidade e Nome do produto", width=230)
Nome_quantidadeE.grid(padx=5, pady=0, row=1, column=1, columnspan=2)

Produto_E = customtkinter.CTkScrollableFrame(Frame_Entrada)
Produto_E.grid(pady=0, padx=20, row=2, column=0, rowspan=3)

Quantidade_E = customtkinter.CTkEntry(Frame_Entrada, placeholder_text="Quatidade recebida", width=90)
Quantidade_E.grid(padx=5, pady=0, row=2, column=1, stick="w")

item_Adic = customtkinter.CTkButton(Frame_Entrada, text="Adic item", fg_color="Blue", font=("Couvier", 16), width=130, command=adicionar_item_entrada)
item_Adic.grid(padx=5, pady=5, row=2, column=2, stick="e")

Entrada_frame = customtkinter.CTkFrame(Frame_Entrada, width=230)
Entrada_frame.grid(padx=5, pady=0, row=3, column=1, columnspan=3, stick="we")

Cancelar_entrada = customtkinter.CTkButton(Frame_Entrada, text="Cancelar", fg_color="Blue", font=("Couvier", 16), width=80)
Cancelar_entrada.grid(padx=5, pady=0, stick="w", row=4, column=1)

S_saida_E = customtkinter.CTkButton(Frame_Entrada, text="Saida", fg_color="Blue", font=("Couvier", 16), width=80)
S_saida_E.grid(padx=5, pady=0, stick="e", row=4, column=2)

# frame6

Frame_Relatorio = customtkinter.CTkFrame(janela, fg_color="Dark red", width=590, height=380, corner_radius=0)
Frame_Relatorio.grid_propagate(False)

Label_Relatorion = customtkinter.CTkLabel(Frame_Relatorio, text=" Estoque Relatório", text_color="Black", font=("Couvier", 16))
Label_Relatorion.grid(padx=0, pady=20, row=0, column=0, columnspan=4)

Buscar_Relatorio = customtkinter.CTkEntry(Frame_Relatorio, placeholder_text="buscar produto", width=230)
Buscar_Relatorio.grid(padx=5, pady=5, row=1, column=0, stick="w")

# janela exportar
Exportar = customtkinter.CTkButton(Frame_Relatorio, text="Exportar", fg_color="Blue",font=("Couvier", 16), width=80, command=abrir_janela2)
Exportar.grid(padx=5, pady=5, row=1, column=3)


tabela = tkinter.ttk.Treeview(Frame_Relatorio, columns=coluna, show="headings", height=5)
tabela.column("NOME", width=110)
tabela.column("QUANTIDADE", width=110)
tabela.column("PREÇO", width=110)
tabela.column("DESCRIÇÃO", width=110)

scroll = tkinter.ttk.Scrollbar(Frame_Relatorio, command=tabela.yview)
tabela.grid(pady=5, padx=10, column=0, columnspan=4, row=2, stick="nsew")

for col in coluna:
    tabela.heading(col, text=col)
    dados = []


for dado in dados:
    tabela.insert("", "end", values=dado)
    tabela.grid(pady=5, padx=5, row=2, column=0, columnspan=4, stick="nsew")

# Ajuste das colunas para garantir distribuição de espaço
Frame_Relatorio.grid_columnconfigure(0, weight=1)  # Coluna 0 (com a Textbox) vai se expandir
Frame_Relatorio.grid_columnconfigure(1, weight=0)  # Coluna 1 (do meio) não vai se expandir
Frame_Relatorio.grid_columnconfigure(2, weight=1)  # Coluna 2 (com o botão Exportar) também vai se expandir

# Ajuste das linhas
Frame_Relatorio.grid_rowconfigure(0, weight=0)  # Linha do título não precisa se expandir
Frame_Relatorio.grid_rowconfigure(1, weight=0)  # Linha de busca e botão Exportar não precisa se expandir
Frame_Relatorio.grid_rowconfigure(2, weight=1)  # Linha com a Textbox vai se expandir para ocupar mais espaço
Frame_Relatorio.grid_rowconfigure(3, weight=0)  # Linha dos botões não vai se expandir


B_Estoque = customtkinter.CTkButton(Frame_Relatorio, text="Estoque", fg_color="Red", font=("Couvier", 16), width=80, command =Tela_B_estoque)
B_Estoque.grid(padx=5, pady=0,  row=3, column=1)

B_Saida = customtkinter.CTkButton(Frame_Relatorio, text="Saida", fg_color="Red", font=("Couvier", 16), width=80, command = Tela_B_saida)
B_Saida.grid(padx=5, pady=0, row=3, column=2)

B_Entrada = customtkinter.CTkButton(Frame_Relatorio, text="Entrada", fg_color="Red", font=("Couvier", 16), width=80, command =Tela_B_entrada)
B_Entrada.grid(padx=5, pady=0, row=3, column=3)

# Aqui é o botão de saída do frame do relatorio
# Frame 7

Frame_B_Relatorio_Saida = customtkinter.CTkFrame(janela, fg_color="Dark red", width=590, height=380, corner_radius=0)
Frame_B_Relatorio_Saida.grid_propagate(False)

Label_RelatorionExit = customtkinter.CTkLabel(Frame_B_Relatorio_Saida, text=" Relatorio saída", text_color="Black", font=("Couvier", 16))
Label_RelatorionExit.grid(padx=0, pady=20, row=0, column=0, columnspan=4)

Buscar_RelatorioS = customtkinter.CTkEntry(Frame_B_Relatorio_Saida, placeholder_text="Buscar", font=("Couvier", 16), width=230)
Buscar_RelatorioS.grid(padx=5, pady=5, row=1, column=0, stick="w")

ExportarS = customtkinter.CTkButton(Frame_B_Relatorio_Saida, text="Exportar", font=("Couvier", 16), width=80,command=abrir_janela2)
ExportarS.grid(padx=5, pady=5, row=1, column=3)

Estoque_RS = customtkinter.CTkTextbox(Frame_B_Relatorio_Saida)
Estoque_RS.grid(pady=5, padx=5, row=2, column=0, columnspan=4, stick="nsew")

tabela_Saida = tkinter.ttk.Treeview(Frame_B_Relatorio_Saida, columns=coluna_saida, show="headings", height=5)
tabela_Saida.heading("Nome", text="Nome")
tabela_Saida.column("Nome", width=110)
tabela_Saida.heading("Quantidade", text="Quantidade")
tabela_Saida.column("Quantidade", width=110)
tabela_Saida.heading("Data/hora", text="Data/hora")
tabela_Saida.column("Data/hora", width=110)


scroll_Saida = tkinter.ttk.Scrollbar(Frame_B_Relatorio_Saida, orient="vertical", command=tabela_Saida.yview)
tabela_Saida.grid(row=2, column=4, sticky='ns')

for col_saida in coluna_saida:
    tabela_Saida.heading(col_saida, text=col_saida)
    dados_saida = [
        ("Fone X",  25, 17.02),
        ("Iphone 17", 30, 19.04),
        ("Notebook",  28, 47.000, 25.04)]


for dado_saida in dados_saida:
    tabela_Saida.insert("", "end", values=dado_saida)
    tabela_Saida.grid(pady=5, padx=5, row=2, column=0, columnspan=4, stick="nsew")


Frame_B_Relatorio_Saida.grid_columnconfigure(0, weight=1)  # Coluna 0 (com a Textbox) vai se expandir
Frame_B_Relatorio_Saida.grid_columnconfigure(1, weight=0)  # Coluna 1 (do meio) não vai se expandir
Frame_B_Relatorio_Saida.grid_columnconfigure(2, weight=1)  # Coluna 2 (com o botão Exportar) também vai se exFrame_B_Relatorio_Saida
Frame_B_Relatorio_Saida.grid_rowconfigure(0, weight=0)  # Linha do título não precisa se expandir
Frame_B_Relatorio_Saida.grid_rowconfigure(1, weight=0)  # Linha de busca e botão Exportar não precisa se expandir
Frame_B_Relatorio_Saida.grid_rowconfigure(2, weight=1)  # Linha com a Textbox vai se expandir para ocupar mais espaço
Frame_B_Relatorio_Saida.grid_rowconfigure(3, weight=0)  # Linha dos botões não vai se expandir

B_Estoque_Saida = customtkinter.CTkButton(Frame_B_Relatorio_Saida, text="Estoque", fg_color="Red", font=("Couvier", 16), width=80, command=Tela_B_estoque)
B_Estoque_Saida.grid(padx=5, pady=0,  row=3, column=1)

B_Saida_Exit = customtkinter.CTkButton(Frame_B_Relatorio_Saida, text="Saida", fg_color="Red", font=("Couvier", 16), width=80, command=Tela_B_saida)
B_Saida_Exit.grid(padx=5, pady=0, row=3, column=2)

B_Entrada_Saida = customtkinter.CTkButton(Frame_B_Relatorio_Saida, text="Entrada", fg_color="Red", font=("Couvier", 16), width=80, command=Tela_B_entrada)
B_Entrada_Saida.grid(padx=5, pady=0, row=3, column=3)

#Relatorio estoque
# Frame 8
Frame_B_Relatorio_Entrada = customtkinter.CTkFrame(janela, fg_color="Dark red", width=590, height=380, corner_radius=0)
Frame_B_Relatorio_Entrada.grid_propagate(False)

B_Entrada_R = customtkinter.CTkButton(Frame_B_Relatorio_Entrada, text="Entrada", fg_color="Red", font=("Couvier", 16), width=80, command=Tela_B_entrada)
B_Entrada_R.grid(padx=5, pady=0, row=3, column=3)

Label_Relatorion_Entry = customtkinter.CTkLabel(Frame_B_Relatorio_Entrada, text=" Relatorio entrada", text_color="Black", font=("Couvier", 16))
Label_Relatorion_Entry.grid(padx=0, pady=20, row=0, column=0, columnspan=4)

Buscar_Relatorio_S = customtkinter.CTkEntry(Frame_B_Relatorio_Entrada, placeholder_text="Buscar", font=("Couvier", 16), width=230)
Buscar_Relatorio_S.grid(padx=5, pady=5, row=1, column=0, stick="w")

Exportar_S = customtkinter.CTkButton(Frame_B_Relatorio_Entrada, text="Exportar", font=("Couvier", 16), width=80,command=abrir_janela2)
Exportar_S.grid(padx=5, pady=5, row=1, column=3)

Estoque_R_S = customtkinter.CTkTextbox(Frame_B_Relatorio_Entrada)
Estoque_R_S.grid(pady=5, padx=5, row=2, column=0, columnspan=4, stick="nsew")


tabela_Entrada = tkinter.ttk.Treeview(Frame_B_Relatorio_Entrada, columns=coluna_saida, show="headings", height=5)
tabela_Entrada.heading("Nome", text="Nome")
tabela_Entrada.column("Nome", width=110)
tabela_Entrada.heading("Quantidade", text="Quantidade")
tabela_Entrada.column("Quantidade", width=110)
tabela_Entrada.heading("Data/hora", text="Data/hora")
tabela_Entrada.column("Data/hora", width=110)


scroll_Entrada = tkinter.ttk.Scrollbar(Frame_B_Relatorio_Entrada, orient="vertical", command=tabela_Entrada.yview)
tabela_Entrada.grid(row=2, column=4, stick='ns')

for col_entrada in coluna_entrada:
    tabela_Entrada.heading(col_entrada, text=col_entrada)
    dados_entrada = [
        ("Fone X",  25, 17.02),
        ("Iphone 17", 30, 19.04),
        ("Notebook",  28, 47.000, 25.04)]


for dado_entrada in dados_entrada:
    tabela_Entrada.insert("", "end", values=dado_entrada)
    tabela_Entrada.grid(pady=5, padx=5, row=2, column=0, columnspan=4, stick="nsew")


Frame_B_Relatorio_Entrada.grid_columnconfigure(0, weight=1)  # Coluna 0 (com a Textbox) vai se expandir
Frame_B_Relatorio_Entrada.grid_columnconfigure(1, weight=0)  # Coluna 1 (do meio) não vai se expandir
Frame_B_Relatorio_Entrada.grid_columnconfigure(2, weight=1)  # Coluna 2 (com o botão Exportar) também vai se expandir78
Frame_B_Relatorio_Entrada.grid_rowconfigure(0, weight=0)  # Linha do título não precisa se expandir
Frame_B_Relatorio_Entrada.grid_rowconfigure(1, weight=0)  # Linha de busca e botão Exportar não precisa se expandir
Frame_B_Relatorio_Entrada.grid_rowconfigure(2, weight=1)  # Linha com a Textbox vai se expandir para ocupar mais espaço
Frame_B_Relatorio_Entrada.grid_rowconfigure(3, weight=0)  # Linha dos botões não vai se expandir8

B_Estoque_E = customtkinter.CTkButton(Frame_B_Relatorio_Entrada, text="Estoque", fg_color="Red", font=("Couvier", 16), width=80, command=Tela_B_estoque)
B_Estoque_E.grid(padx=5, pady=0,  row=3, column=1)

B_Saida_E = customtkinter.CTkButton(Frame_B_Relatorio_Entrada, text="Saida", fg_color="Red", font=("Couvier", 16), width=80, command=Tela_B_saida)
B_Saida_E.grid(padx=5, pady=0, row=3, column=2)

B_Entrada_Relatorio_E = customtkinter.CTkButton(Frame_B_Relatorio_Entrada, text="Entrada", fg_color="Red", font=("Couvier", 16), width=80, command=Tela_B_entrada)
B_Entrada_Relatorio_E.grid(padx=5, pady=0, row=3, column=3)

# Usando no frame da Saída
item = [f"Item {i + 1}" for i in range(3)]

'''for i, item in enumerate(items):
    create_line(Frame_Saida, item, i + 1)'''

# Usando no Frame entrada
'''item2 = [f"Item {i + 1}" for i in range(3)]
for i, item2 in enumerate(items2):
    create_line2(Frame_Entrada, item2, i + 1)'''

# Usando no Frame editar
'''for item in items:
    box = customtkinter.CTkCheckBox(Produto_T, text=item)
    box.grid(pady=5)'''

'''for item1 in items1:
    box1 = customtkinter.CTkCheckBox(Produto_S, text=item1)
    box1.grid(pady=5)'''

'''for item2 in items2:
    box2 = customtkinter.CTkCheckBox(Produto_E, text=item2)
    box2.grid(pady=5)'''


janela.mainloop()