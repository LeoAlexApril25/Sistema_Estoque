import customtkinter

def on_click(item):
   print(f"Você clicou em: {item}")

root = customtkinter.CTk()
root.geometry("300x300")
scrollable_frame = customtkinter.CTkScrollableFrame(root)
scrollable_frame.pack(pady=20, padx=20, fill="both", expand=True)
items = ["Item 1", "Item 2", "Item 3", "Item 4","Item 1", "Item 2", "Item 3", "Item 4"]
for item in items:
   box = customtkinter.CTkCheckBox(scrollable_frame, text=item, command=lambda i=item: on_click(i))
   box.pack(pady=5, padx=10, fill="x")
root.mainloop()