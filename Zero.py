import customtkinter as ctk

# Lista fixa de itens do estoque
estoque = [
    {"Nome": "Produto A", "Quantidade": 0, "Preço": 0.00, "Descrição": "Descrição do Produto A"},
    {"Nome": "Produto B", "Quantidade": 0, "Preço": 0.00, "Descrição": "Descrição do Produto B"},
    {"Nome": "Produto C", "Quantidade": 0, "Preço": 0.00, "Descrição": "Descrição do Produto C"},
]

# Função para exibir o relatório com as informações do estoque
def atualizar_relatorio():
    # Limpar o conteúdo atual do relatório
    for widget in frame_relatorio.winfo_children():
        widget.destroy()

    # Exibir os títulos das colunas (cabeçalho)
    ctk.CTkLabel(frame_relatorio, text="Nome", font=("Arial", 12, "bold")).grid(row=0, column=0, padx=10, pady=5)
    ctk.CTkLabel(frame_relatorio, text="Quantidade", font=("Arial", 12, "bold")).grid(row=0, column=1, padx=10, pady=5)
    ctk.CTkLabel(frame_relatorio, text="Preço", font=("Arial", 12, "bold")).grid(row=0, column=2, padx=10, pady=5)
    ctk.CTkLabel(frame_relatorio, text="Descrição", font=("Arial", 12, "bold")).grid(row=0, column=3, padx=10, pady=5)

    # Exibir os dados do estoque
    for i, item in enumerate(estoque):
        ctk.CTkLabel(frame_relatorio, text=item["Nome"], font=("Arial", 12)).grid(row=i+1, column=0, padx=10, pady=5)
        ctk.CTkLabel(frame_relatorio, text=str(item["Quantidade"]), font=("Arial", 12)).grid(row=i+1, column=1, padx=10, pady=5)
        ctk.CTkLabel(frame_relatorio, text=f"R${item['Preço']:.2f}", font=("Arial", 12)).grid(row=i+1, column=2, padx=10, pady=5)
        ctk.CTkLabel(frame_relatorio, text=item["Descrição"], font=("Arial", 12)).grid(row=i+1, column=3, padx=10, pady=5)

# Criar a janela principal
root = ctk.CTk()

# Definir o tamanho da janela
root.geometry("700x400")

# Estilo personalizado para a tabela
frame_relatorio = ctk.CTkFrame(root, width=650, height=350, corner_radius=10)
frame_relatorio.pack(pady=20, padx=20)

# Label de título do relatório
label_titulo_relatorio = ctk.CTkLabel(frame_relatorio, text="Relatório de Estoque", font=("Arial", 16))
label_titulo_relatorio.grid(row=0, column=0, padx=10, pady=10, columnspan=4)

# Atualizar o relatório ao iniciar
atualizar_relatorio()

# Iniciar o loop da interface
root.mainloop()
