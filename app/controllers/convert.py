import wave

class Convert():
    
    def __init__():
        pass

    
    def ram_to_wave(ram_file, wav_path):
        ram_file = wave.open(ram_file, 'rb')
        num_channels = 1
        sample_rate = 8000
        sample_width = 2
        
        wav_file = wave.open(f'{wav_path}', 'wb')
        wav_file.setnchannels(num_channels)
        wav_file.setframerate(sample_rate)
        wav_file.setsampwidth(sample_width)
        
        data = ram_file.readframes(ram_file.getnframes())
        wav_file.writeframes(data)
        
        ram_file.close()
        wav_file.close()

# TODO testar classe