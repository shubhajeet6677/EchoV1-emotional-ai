# Connects APIs, services, etc.

from Core_Brain import stt, tts, nlp, memory

def pipeline(audio_file_path : str ) -> dict:

    text = stt.transcribe_file(audio_file_path)
    
    result = nlp.analyze(text, memory_manager=memory)
    
    
    audio_response = tts.speak(result["response"])
    
    
    
    return {
        "transcribed_text": text,
        "intent": result['intent'],
        "emotion": result['emotion'],
        "sentiment": result['sentiment'],
        "response_text": result['response'],
        # "response_audio_path": audio_response_path
    }