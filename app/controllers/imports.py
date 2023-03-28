import shutil, os
from tkinter import filedialog

class Imports():
 
    def import_music(self):
        path = filedialog.askopenfilename(title="Selecionar Arquivo de Áudio", filetypes=(("Arquivos wav", "*.wav"), ("Todos os arquivos", "*.*")))
        arquivo = os.path.basename(path)
        path_to=f'app/audio_files/backs/{arquivo}'
        shutil.copy(path, path_to)
        
 


