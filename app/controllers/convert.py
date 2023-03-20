from pydub import AudioSegment

class Convert():
     
    def raw_to_wav(self, raw_file, wav_path):
        channels = 1
        sample_width = 2
        frame_rate = 8000
        
        audio = AudioSegment.from_raw(raw_file, sample_width=sample_width, channels=channels, frame_rate=frame_rate)
        audio.export(wav_path, format="wav")
    
    
    def mp3_to_wav(self, mp3_file, wav_path):

        
        audio = AudioSegment.from_mp3(mp3_file)

        audio.export(wav_path, format("wav"))


# TODO testar classe