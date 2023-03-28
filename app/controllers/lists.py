import os

class Lists():
    
    def list_backs(self):
        path = 'app/audio_files/backs/'
        return [file for file in os.listdir(path) if os.path.isfile(os.path.join(path, file))]
    
    def list_vozes(self):
        return ['pt-BR-AntonioNeural', 'pt-BR-BrendaNeural', 'pt-BR-DonatoNeural', 'pt-BR-ElzaNeural', 'pt-BR-FabioNeural',
                'pt-BR-FranciscaNeural', 'pt-BR-GiovannaNeural', 'pt-BR-HumbertoNeural', 'pt-BR-JulioNeura', 'pt-BR-LeilaNeural',
                'pt-BR-LeticiaNeural', 'pt-BR-ManuelaNeural', 'pt-BR-NicolauNeural', 'pt-BR-ValerioNeural', 'pt-BR-YaraNeural']
