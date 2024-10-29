import tkinter as tk
from tkinter import ttk
from controllers.filmes_controller import ControllerFilmes

#data
nomes = ['Palo Alto', 'Os sem floresta', 'Your Name']
assistido = ['25/09/2024', '03/10/2024', '25/07/2024']
class App(tk.Tk):

    def __init__(self):
        super().__init__()
        self.filmes = []
        self.create_table()
        self.controller = ControllerFilmes(self)
        self.controller.atualizar_lista_filmes()

    #Create table
    def create_table(self):
        def delete_item(_):
            for i in self.table.selection():
                self.table.delete(i)

        def item_select(_):
            for i in self.table.selection():
                print(self.table.item(i)['values'])
                
        self.table = ttk.Treeview(self, columns=('nome', 'assistido_em'), show='headings')

        self.table.heading('nome', text = 'Nome')
        self.table.heading('assistido_em', text='Assistido em')
        self.table.bind('<<TreeviewSelect>>', item_select)
        self.table.bind('<Delete>', delete_item)
        return self.table.pack(fill = 'both', expand=True)






    def set_filmes(self, filmes):
        self.filmes = filmes

    def atualizar_lista(self, filmes):
        # for record in self.table.get_children():
        #     self.table.delete(record)
        
        for filme in filmes:
            self.table.insert(parent='', index=0, values=(filme.nome, filme.assistido_em))
