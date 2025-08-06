
import whisper
from pydub import AudioSegment
import tempfile 
import logging
import sounddevice as sd
import numpy as np


class SpeechToText:
    def __init__(self , model_name="small" , sample_rate=16000):
        self.model = whisper.load_model(model_name)
        self.sample_rate = sample_rate
        self.logger = logging.getLogger(__name__)
        logging.basicConfig(level=logging.INFO)


    def record_audio(self, duration=5) -> str:
        try:
            print("🎙️ Recording... Speak now.")
            sd.default.samplerate = self.sample_rate
            sd.default.channels = 1
            audio = sd.rec(int(duration * self.sample_rate), dtype='float32')
            sd.wait()
            print("✅ Done recording.")

            # Convert to AudioSegment
            pcm_audio = (audio * 32767).astype(np.int16).tobytes()
            audio_seg = AudioSegment(
                data=pcm_audio,
                sample_width=2,
                frame_rate=self.sample_rate,
                channels=1
            )

            tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".wav")
            audio_seg.export(tmp.name, format="wav")
            return tmp.name
        except Exception as e:
            self.logger.error(f"Error during recording: {e}")
            return ""

    def process_audio(self, audio_path: str) -> AudioSegment:
        audio = AudioSegment.from_file(audio_path)
        audio = audio.set_frame_rate(16000)
        audio = audio.set_channels(1)
        audio = audio.set_sample_width(2)  # 16-bit PCM
        audio = audio.normalize()

        return audio

    def transcribe(self, audio_segment: AudioSegment) -> str:
        try:
            with tempfile.NamedTemporaryFile(delete =False , suffix= ".wav") as temp:
                audio_segment.export(temp.name, format="wav")
                result = self.model.transcribe(temp.name, language="en" ,  task = "transcribe")
                return result['text'].strip()

        except Exception as e:
            self.logger.error(f"Error during transcription: {e}")
            return ""


    def transcribe_file(self , file_path: str) -> str:
        try:
            audio = self.process_audio(file_path)
            return self.transcribe(audio)

        except Exception as e:
            self.logger.error(f"Error during file transcription: {e}")
            return ""






# main() function use 
# from modules.speech_to_text import SpeechToText

# stt = SpeechToText(model_name="small")
# raw_audio = stt.record_audio(duration=5)
# audio_segment = stt.numpy_to_audiosegment(raw_audio)
# clean_audio = stt.preprocess(audio_segment)
# text = stt.transcribe(clean_audio)

# print("User said:", text)