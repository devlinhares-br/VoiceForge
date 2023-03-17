import pygame


class AudioPlay():
    def __init__(self) -> None:
        super().__init__()
        pygame.init()
    
    def play_audio(self, audio_path):
        pygame.mixer.music.load(audio_path)
        
        pygame.mixer.music.play()
        
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
