import tkinter as tk
from app.controllers.imports import Imports

class MenuPrincipal(tk.Menu):
    def __init__(self, master):
        super().__init__(master)
        self.im = Imports()
        
        # Criar o menu Arquivo
        arquivo_menu = tk.Menu(self, tearoff=0)
        arquivo_menu.add_command(label="Importar", command=lambda: self.im.import_music())
        arquivo_menu.add_separator()
        arquivo_menu.add_command(label="Sair", command=master.quit)
        
        # Criar o menu Ajuda
        ajuda_menu = tk.Menu(self, tearoff=0)
        ajuda_menu.add_command(label="Sobre")
        
        # Adicionar os menus ao menu principal
        self.add_cascade(label="Arquivo", menu=arquivo_menu)
        self.add_cascade(label="Ajuda", menu=ajuda_menu)