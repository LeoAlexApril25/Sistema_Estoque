import customtkinter as ctk

root = ctk.CTk()

opcoes = ["Opção 1", "Opção 2", "Opção 3"]

combo = ctk.CTkComboBox(root, values=opcoes)
combo.grid(padx=5, pady=5)

root.mainloop()