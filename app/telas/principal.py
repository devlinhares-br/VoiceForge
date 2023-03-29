from tkinter import *
from tkinter import ttk
from app.telas.menu_principal import MenuPrincipal
from app.telas.typography import Typography as font
from app.telas.status_bar import Status_Bar
from app.controllers.lists import Lists
from app.controllers.read import Speech
from app.controllers.convert import Convert
from threading import Thread as th
from pygame import mixer as mx


class Principal:
    def __init__(self):
        self.root = Tk()
        self.root.title("VoiceForge")
        self.tp = font()
        self.lt = Lists()
        self.read = Speech()
        self.convert = Convert()
        mx.init()
        
        menu_principal = MenuPrincipal(self.root)
        self.root.config(menu=menu_principal)
        
        self.main_frame = Frame(self.root)
        self.main_frame.pack(fill=BOTH, expand=True, padx=0, pady=0)
        
        self.texto_lb = Label(self.main_frame, font=self.tp.font_title, text="Texto:")
        self.texto_lb.place(x=10,y=10)

        self.tx_text = Text(self.main_frame, height=15, width=(60))
        self.tx_text.place(x=10, y=40)
        
        self.voz_lb = Label(self.main_frame, font=self.tp.font_title, text="Voz:")
        self.voz_lb.place(x=550,y=10)
        
        self.voz_ltb = Listbox(self.main_frame, height=15, width=50)
        self.vozes = self.lt.list_vozes()
        for voz in self.vozes:
            self.voz_ltb.insert(END, voz)
        self.voz_ltb.place(x=550, y=40)
        
        
        self.ler_bt = Button(self.main_frame, text='Ler', width=10, font=self.tp.font_btn,
                             command=lambda: th(target=self.ler_texto,
                                                args=(self.tx_text.get('1.0', END),
                                                      str(self.voz_ltb.get(ACTIVE)))).start())
        self.ler_bt.place(x=410 , y=300 )
        
        self.music_frame = Frame(borderwidth=2, relief='solid')
        self.music_frame.pack(fill=BOTH, expand=True, padx=10, pady=10)
        
        self.frame_lb = Label(self.music_frame, text='Configuração do Audio de fundo', width=28, font=self.tp.font_title)
        self.frame_lb.place(x=300,y=-7)
        
        self.musics_lb = Label(self.music_frame, text='Fundos', font=self.tp.font_title)
        self.musics_lb.place(x=10, y=15)
        
        self.musics_ltb = Listbox(self.music_frame, height=10, width=50)
        self.backs = self.lt.list_backs()
        for back in self.backs:
            self.musics_ltb.insert(END,back)
        self.musics_ltb.place(x=10, y=40)
        
        self.fade_in = BooleanVar()
        self.fade_in.set(False)
        self.fade_in.trace('w', self.update_fade_in)
        

        self.fade_in_ck = Checkbutton(self.music_frame, text="Fade-in", variable=self.fade_in)
        self.fade_in_ck.place(x=340, y=50)
       
        self.fade_in_sc = Scale(self.music_frame, from_=0, to=10, length=150, orient=HORIZONTAL, resolution=1, state='disabled')
        self.fade_in_sc.set(1)
        self.fade_in_sc.place(x=420, y=40)
        
        self.fade_out = BooleanVar()
        self.fade_out.set(False)
        self.fade_out.trace('w', self.update_fade_out)
        
        self.fade_out_ck = Checkbutton(self.music_frame, text='Fade-out', variable=self.fade_out)
        self.fade_out_ck.place(x=340, y=100)

        self.fade_out_sc = Scale(self.music_frame, from_=0, to=10, resolution=1, length=150, orient=HORIZONTAL, state='disabled')
        self.fade_out_sc.set(1)
        self.fade_out_sc.place(x=420 ,y=90)
        
        self.music_volume_lb = Label(self.music_frame, text='Volume')
        self.music_volume_lb.place(x=650, y=15)

        self.music_volume_sc = Scale(self.music_frame, resolution=1, length=150, orient=HORIZONTAL, from_=-100, to=100)
        self.music_volume_sc.set(0)
        self.music_volume_sc.place(x=650, y=40)
        
        self.music_ini_lb = Label(self.music_frame, text='Inicio')
        self.music_ini_lb.place(x=650, y=80)
        
        self.music_ini_sc = Scale(self.music_frame, resolution=1, length=150, orient=HORIZONTAL, from_=0, to=10)
        self.music_ini_sc.set(0)
        self.music_ini_sc.place(x=650, y=100)
        
        self.music_end_lb = Label(self.music_frame, text='Termino')
        self.music_end_lb.place(x=650, y=150)
       
        self.music_end_sc = Scale(self.music_frame, resolution=1, length=150, orient=HORIZONTAL, from_=0, to=10)
        self.music_end_sc.set(0)
        self.music_end_sc.place(x=650, y=170)
        
        self.music_play_bt = Button(self.music_frame, text='Play', font=self.tp.font_btn, width=10)
        self.music_play_bt.place(x=10, y= 230)
        
        self.music_pause_bt = Button(self.music_frame, text='Pause', font=self.tp.font_btn, width=10)
        self.music_pause_bt.place(x=100, y=230)
        
        self.music_stop_bt = Button(self.music_frame, text='Stop', font=self.tp.font_btn, width=10)
        self.music_stop_bt.place(x=190, y=230)
       
        self.status_bar = Status_Bar(self.root)
        
        self.save_frame = Frame(self.root)
        self.save_frame.pack(side=BOTTOM, padx=5, pady=5, fill=X)

        self.save_bt = Button(self.save_frame, text='Salvar', font=self.tp.font_btn, width=10)
        self.save_bt.pack(side=RIGHT, padx=5)

        self.root.geometry("870x750")
        self.root.minsize(870, 750)
        self.root.maxsize(870, 750)
        self.root.mainloop()
        
    def update_fade_in(self, *args):
        if(self.fade_in.get()):
            self.fade_in_sc.config(state='normal')
        else:
            self.fade_in_sc.config(state='disabled')
            
    def update_fade_out(self, *args):
        if(self.fade_out.get()):
            self.fade_out_sc.config(state='normal')
        else:
            self.fade_out_sc.config(state='disabled')

    def ler_texto(self, texto, voice):
        self.read.set_voz(voice)
        self.read.read_text(texto)
        # raw_file = 'app/audio_files/temp/output.raw'
        # wav_file = 'app/audio_files/temp/output.wav'
        # self.convert.raw_to_wav(raw_file, wav_file)
        # mx.music.load(wav_file)
        # mx.music.play()
        return True
