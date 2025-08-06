 # Handles voice input & STT (Whisper) text_to_speech(text): text_to_speech(text):
from gtts import gTTS
import tempfile
import logging

class TextToSpeech:
    def __init__(self ,lang = "en"):
        self.lang = lang
        self.logger = logging.getLogger(__name__)
        logging.basicConfig(level=logging.INFO)

    def speak(self , text:str) -> str:
        if not text.strip():
            self.logger.warning("No text provided for speech synthesis.")
            return

        try:
            tts = gTTS(text= text , lang = self.lang)
            temp = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
            tts.save(temp.name)
            return f"Speech synthesized successfully. File saved at: {temp.name}"
        except Exception as e:
            self.logger.error(f"GTTS error: {e}")
            return f"[TTS Error]: {e}"



# from modules.text_to_speech import TextToSpeech

# tts = TextToSpeech()
# tts.speak("Hello, how can I help you today?")
