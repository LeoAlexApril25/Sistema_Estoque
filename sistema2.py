import customtkinter

items = ["Opcão1", "Opção2", "Opção3", "Opcão4", "Opção5", "Opção6"]
items1 = ["1", "2", "3", "4", "5", "6"]


customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("blue")

def Tela_Cadastrar():
    Frame_03.grid_forget()
    Frame_04.grid_forget()
    Frame_05.grid_forget()
    Frame_06.grid_forget()
    Frame02.grid_propagate(False)
    Frame02.grid(row=0, column=1, padx=5, pady=5)

def Tela_Editar():
    Frame02.grid_forget()
    Frame_04.grid_forget()
    Frame_05.grid_forget()
    Frame_06.grid_forget()
    Frame_03.grid_propagate(False)
    Frame_03.grid(row=0, column=1, padx=5, pady=5)

def Tela_Saída():
    Frame02.grid_forget()
    Frame_03.grid_forget()
    Frame_05.grid_forget()
    Frame_06.grid_forget()
    Frame_04.grid_propagate(False)
    Frame_04.grid(row=0, column=1, padx=5, pady=5)

def Tela_Entrada():
    Frame02.grid_forget()
    Frame_03.grid_forget()
    Frame_04.grid_forget()
    Frame_06.grid_forget()
    Frame_05.grid_propagate(False)
    Frame_05.grid(row=0, column=1, padx=5, pady=5)

def Tela_Relatorio():
    Frame02.grid_forget()
    Frame_03.grid_forget()
    Frame_04.grid_forget()
    Frame_05.grid_forget()
    Frame_06.grid_propagate(False)
    Frame_06.grid(row=0, column=1, padx=5, pady=5)


def on_trash_icon_click(item_num):
    print(f"Ícone de lixeira da linha {item_num} clicado!")

def create_line(Frame_04, text, item_num):
    label = customtkinter.CTkLabel(line_frame, text=text, anchor="w")
    label.grid(row=item_num, column=0, padx=5, pady=0, stick="ew")
    #label.pack(side="left", fill="x")

    line_frame.grid_columnconfigure(0, weight=1)
    line_frame.grid_columnconfigure(1, weight=1)

    trash_icon = customtkinter.CTkButton(line_frame, text="🗑️", command=lambda: on_trash_icon_click(item_num), width=40, height=20)
    trash_icon.grid(row=item_num, column=1, padx=5, pady=0, stick="e")
    #trash_icon.pack(side="right", fill="x")


janela = customtkinter.CTk()
janela.title("Projeto")
janela.geometry("800x400")

Frame01 = customtkinter.CTkFrame(janela, fg_color="Light green", width=190, height=380, corner_radius=0)
Frame01.grid_propagate(False)
Frame01.grid(row=0, column=0, padx=5, pady=10)

Frame02 = customtkinter.CTkFrame(janela, fg_color="Dark red", width=590, height=380, corner_radius=0)
Frame02.grid_propagate(False)
Frame02.grid(row=0, column=1, padx=5, pady=5)

Frame_03 = customtkinter.CTkFrame(janela, fg_color="Dark red", width=590, height=380, corner_radius=0)
Frame_03.grid_propagate(False)

Frame_04 = customtkinter.CTkFrame(janela, fg_color="Dark red", width=590, height=380, corner_radius=0)
Frame_04.grid_propagate(False)

Frame_05 = customtkinter.CTkFrame(janela, fg_color="Dark red", width=590, height=380, corner_radius=0)
Frame_05.grid_propagate(False)

Frame_06 = customtkinter.CTkFrame(janela, fg_color="Dark red", width=590, height=380, corner_radius=0)
Frame_06.grid_propagate(False)


Label_titulo = customtkinter.CTkLabel(Frame01, width=190,  text="Novo Sistema", text_color="blue", font=("Couvier", 18))
Label_titulo.grid(padx=10, pady=20, row=0, column=0)

Botao1 = customtkinter.CTkButton(Frame01, text="Cadastrar", font=("Couvier", 16), corner_radius=0, command=Tela_Cadastrar)
Botao1.grid(pady=5, row=1, column=0)

Botao2 = customtkinter.CTkButton(Frame01, text="Editar", font=("Couvier", 16), corner_radius=0, command=Tela_Editar)
Botao2.grid(pady=5, row=2, column=0)

Botao3 = customtkinter.CTkButton(Frame01, text="Saída", font=("Couvier", 16), corner_radius=0, command=Tela_Saída)
Botao3.grid(pady=5, row=3, column=0)

Botao4 = customtkinter.CTkButton(Frame01,  text="Entrada", font=("Couvier", 16), corner_radius=0, command=Tela_Entrada)
Botao4.grid(pady=5, row=4, column=0)

Botao5 = customtkinter.CTkButton(Frame01, text="Relátorio", font=("Couvier", 16), corner_radius=0, command=Tela_Relatorio)
Botao5.grid(pady=5, row=5, column=0)

Texto1 = customtkinter.CTkLabel(Frame02, text="Cadastro do Produto", text_color="Black", font=("Couvier", 18))
Texto1.grid(padx=10, pady=20, row=0, column=1)

mensagem = customtkinter.CTkLabel(Frame02, text="Nome do Produto:", text_color="black")
mensagem.grid(padx=5, pady=5, row=1, column=0, stick="ne")

mensagem1 = customtkinter.CTkLabel(Frame02, text="Preço(R$):", text_color="black" )
mensagem1.grid(padx=5, pady=5, row=2, column=0, stick="ne")

mensagem2 = customtkinter.CTkLabel(Frame02, text="Descrição:", text_color="black")
mensagem2.grid(padx=5, pady=5, row=3, column=0, stick="ne")

Produto = customtkinter.CTkEntry(Frame02, placeholder_text="Digite o nome do produto :", width=300)
Produto.grid(padx=5, pady=5, row=1, column=1)

Preco = customtkinter.CTkEntry(Frame02, placeholder_text=("0.00"), width=80)
Preco.grid(padx=5, pady=5, row=2, column=1, stick="w")

Descricao = customtkinter.CTkTextbox(Frame02, width=300, height=80)
Descricao.grid(padx=5, pady=5, row=3, column=1, stick="ne")

Salvar = customtkinter.CTkButton(Frame02, text="Salvar", width=80, fg_color="black", hover_color="#E65829")
Salvar.grid(padx=5, pady=5, row=4, column=1, stick="e")

#columnspan ele centraliza o título no espaçamento onde fica tabuada/linhas e outras informações do outro lado
Label_titulo2 = customtkinter.CTkLabel(Frame_03, text="Editar produtos cadastrados:", text_color="Black", font=("Couvier", 16))
Label_titulo2.grid(padx=0, pady=20, row=0, column=0, columnspan=4)



Label_titulo4 = customtkinter.CTkLabel(Frame_05, text="Entrada", text_color="Black", font=("Couvier", 16))
Label_titulo4.grid(padx=280, pady=30, row=0, column=1)

Label_titulo5 = customtkinter.CTkLabel(Frame_06, text="Relatório", text_color="Black", font=("Couvier", 16))
Label_titulo5.grid(padx=280, pady=30, row=1, column=1)

Buscar_produto = customtkinter.CTkEntry(Frame_03, placeholder_text="Informar produto", font=("Couvier", 16), width=230)
Buscar_produto.grid(padx=20, pady=20, row=1, column=0, columnspan=4, stick="w")

Editar_dados = customtkinter.CTkEntry(Frame_03, placeholder_text="Editar dados:", font=("Couvier", 16))
Editar_dados.grid(padx=5, pady=0, row=2, column=1, stick="w", columnspan=3)

Editar_preco = customtkinter.CTkEntry(Frame_03, placeholder_text="0.00:", width=80)
Editar_preco.grid(padx=5, pady=0, row=3, column=1, stick="w", columnspan=3)

Editar_descricao = customtkinter.CTkTextbox(Frame_03, width=300, height=80, fg_color="black")
Editar_descricao.grid(padx=5, pady=0, row=4, column=1, stick="w", columnspan=3)

# rowspan é resposavel as linhas da coluna
Produto_T = customtkinter.CTkScrollableFrame(Frame_03)
Produto_T.grid(pady=0, padx=20, row=2, column=0, rowspan=4)

Excluir = customtkinter.CTkButton(Frame_03, text="Excluir", width=80, fg_color="Red", hover_color="Blue")
Excluir.grid(padx=5, pady=5, stick="w", row=5, column=1)

Cancelar = customtkinter.CTkButton(Frame_03, text="Cancelar", width=80, fg_color="Purple", hover_color="Blue")
Cancelar.grid(padx=0, pady=5, row=5, column=2)

Salvar = customtkinter.CTkButton(Frame_03, text="Salvar", width=80, fg_color="Purple", hover_color="Blue")
Salvar.grid(padx=5, pady=5, stick="e", row=5, column=3)

#Frame04
Label_titulo3 = customtkinter.CTkLabel(Frame_04, text="Saída de Produto", text_color="Black", font=("Couvier", 16))
Label_titulo3.grid(padx=0, pady=0, row=0, column=0, columnspan=3)

Campo_busca = customtkinter.CTkEntry(Frame_04, placeholder_text="Buscar", width=230)
Campo_busca.grid(padx=20, pady=20, row=1, column=0, stick="w")

Nome_quantidade = customtkinter.CTkEntry(Frame_04, placeholder_text="Quantidade e Nome do produto", width=230)
Nome_quantidade.grid(padx=5, pady=0, row=1, column=1, columnspan=2)

Produto_S = customtkinter.CTkScrollableFrame(Frame_04, width=140)
Produto_S.grid(pady=0, padx=20, row=2, column=0, rowspan=4)

Quantidade_R = customtkinter.CTkEntry(Frame_04, placeholder_text="Quatidade retirada", width=90)
Quantidade_R.grid(padx=5, pady=0, row=2, column=1, stick="w")

item_B = customtkinter.CTkButton(Frame_04, text="Adic item", fg_color="Blue", font=("Couvier", 16), width=130)
item_B.grid(padx=5, pady=0, row=2, column=2, stick="e")

line_frame = customtkinter.CTkFrame(Frame_04, width=230)
line_frame.grid(padx=5, pady=5, row=3, column=1, columnspan=2, stick="we")

Cancelar_saida = customtkinter.CTkButton(Frame_04, text="Cancelar", fg_color="Blue", font=("Couvier", 16), width=80)
Cancelar_saida.grid(padx=0, pady=5, stick="w", row=5, column=1)

S_saida = customtkinter.CTkButton(Frame_04, text="Saida", fg_color="Blue", font=("Couvier", 16), width=80)
S_saida.grid(padx=0, pady=5, stick="e", row=5, column=2)


item = [f"Item {i + 1}" for i in range(3)]

for i, item in enumerate(items):
    create_line(Frame_04, item, i + 1)



for item in items:
    box = customtkinter.CTkCheckBox(Produto_T, text=item)
    box.grid(pady=5)

for item1 in items1:
    box1 = customtkinter.CTkCheckBox(Produto_S, text=item1)
    box1.grid(pady=5)



janela.mainloop()