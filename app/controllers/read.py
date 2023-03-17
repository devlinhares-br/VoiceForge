import os
import azure.cognitiveservices.speech as speechsdk
from datetime import datetime
from config import *


class Speech():
    
    def __init__(self) -> None:
        self.__a_key = os.getenv['A_key'] or None
        self.__a_region = os.getenv['A_region'] or None
        self.__speech_config = speechsdk.SpeechConfig(subscription=self.__a_key, region=self.__a_region)
        self.__speech_config.set_speech_synthesis_output_format(speechsdk.SpeechSynthesisOutputFormat(17))
        self.__speech_config.speech_synthesis_voice_name = "pt-BR-FranciscaNeural"
        self.__synthesizer = speechsdk.SpeechSynthesizer(speech_config = self.__speech_config)

    
    def read_text(self, text):
        response = self.__synthesizer.speak_text(text)
        
        try:
            with open('app/audio_files/temp/output.raw', 'wb') as audio:
                audio.write(response.audio_data)
                audio.close()
        except IOError as err:
            with open('log/error_logs.log', 'wb') as audio:
                audio.write(f'{datetime.now()} - {err}')
                audio.close()
        