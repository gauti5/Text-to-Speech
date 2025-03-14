from dataclasses import dataclass
import os, sys

from text_to_speech.constants import APPLICATION_NAME, ARTIFACT_DIR_KEY, AUDIO_DIR, TEXT_DIR

CURRENT_DIR=os.getcwd()
@dataclass
class TTSconfig:
    app_name: str=APPLICATION_NAME
    artifact_dir: str=os.path.join(CURRENT_DIR, app_name, ARTIFACT_DIR_KEY)
    audio_dir: str=os.path.join(artifact_dir, AUDIO_DIR)
    text_dir: str=os.path.join(artifact_dir, TEXT_DIR)