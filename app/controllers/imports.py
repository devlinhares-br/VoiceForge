import os
from app.controllers.convert import Convert
from tkinter import filedialog

class Imports():
    
    def __init__(self):
        self.convert = Convert()
    
    def import_music(self):
        path = filedialog.askopenfilename(title="Selecionar Arquivo de Áudio", filetypes=(("mp3 files", "*.mp3"), ("all files", "*.*")))
        arquivo = os.path.basename(path)
        wav_path=f'app/audio_files/backs/{arquivo[:-3]}.wav'

        self.convert.mp3_to_wav(mp3_file = path, wav_path=wav_path)
