import tkinter as tk

root = tk.Tk()

# Criando uma grid de 3x3
label1 = tk.Label(root, text="Label 1")
label1.grid(row=0, column=0)

label2 = tk.Label(root, text="Label 2")
label2.grid(row=0, column=1, columnspan=2)  # O label ocupa 2 colunas

label3 = tk.Label(root, text="Label 3")
label3.grid(row=1, column=0, rowspan=2)  # O label ocupa 2 linhas

root.mainloop()
