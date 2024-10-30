import tkinter as tk
from tkinter import ttk
from controllers.filmes_controller import ControllerFilmes

#data
class App(tk.Tk):

    def __init__(self):
        super().__init__()
        self.filmes = []
        self.controller = ControllerFilmes()

        self.frame = ttk.Frame(self)
        self.frame.pack()

        self.table = ttk.Treeview(self.frame, columns=('nome', 'assistido_em'), show='headings')
        self.table.grid(row=0, column=0)

        self.table.heading('nome', text = 'Nome')
        self.table.heading('assistido_em', text='Assistido em')
        self.table.bind('<<TreeviewSelect>>', self.item_select)
        self.table.bind('<Delete>', self.delete_item)
        self.atualizar_lista()

    #Create table
    def delete_item(self, _):
        for i in self.table.selection():
            self.table.delete(i)

    def item_select(self, _):
        for i in self.table.selection():
            print(self.table.item(i)['values'])

    def _set_filmes(self, filmes):
        self.filmes = filmes

    def atualizar_lista(self):
        self._set_filmes(self.controller.get_filmes())
        
        for record in self.table.get_children():
            self.table.delete(record)
        
        for filme in self.filmes:
            self.table.insert(parent='', index=0, values=(filme.nome, filme.assistido_em))
