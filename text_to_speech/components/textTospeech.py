from text_to_speech.logger import logger
from text_to_speech.exception import CustomException
from text_to_speech.entity.config_entity import TTSconfig
from text_to_speech.constants import TEXT_FILE_NAME, CURRENT_TIME_STAMP

import os, sys
import base64
import socket


from gtts import gTTS  # google text to speech API

class TTSapplication:
    def __init__(self, app_config=TTSconfig()):
        try:
            self.app_config=app_config
            self.artifact_dir=app_config.artifact_dir
            self.audio_dir=app_config.audio_dir
            self.text_dir=app_config.text_dir
        except Exception as e:
            return CustomException(e,sys)
        
    def check_internet(self):
    
        try:
            socket.create_connection(("8.8.8.8", 53), timeout=3)
            return True
        except OSError:
            return False
        
    def textTospeech(self, text, accent):
        try:
        
        
            text_filename=TEXT_FILE_NAME
            text_file_path=os.path.join(self.text_dir, TEXT_FILE_NAME)
            os.makedirs(self.text_dir, exist_ok=True)
            
            with open(text_file_path, 'a+') as file:
                file.write(f"\n{text}")
                
            tts=gTTS(text=text, lang='en', slow=False, tld=accent)
            
            file_name=f"converted_file{CURRENT_TIME_STAMP}.mp3"
            os.makedirs(self.audio_dir, exist_ok=True)
            audio_path=os.path.join(self.audio_dir, file_name)
            
            # Save the Audio File
            
            tts.save(audio_path)
            
            with open(audio_path, 'rb') as file:
                my_string=base64.b64encode(file.read())
                
            return my_string
            
        except Exception as e:
            raise CustomException(e,sys)
            
                
    