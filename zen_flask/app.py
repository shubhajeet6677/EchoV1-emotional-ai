from flask import Flask, render_template, request, jsonify
from ai_integration.nlp_engine.nlp_engine import NLPEngine
from ai_integration.personalities.EchoPersonality import EchoPersonality
from ai_integration.personality_router import PersonalityRouter

app = Flask(__name__)

@app.route('/')
def landing():
    return render_template('landing.html')

@app.route('/features')
def features():
    return render_template('features.html')

@app.route('/chat')
def chat_page():
    return render_template('chat.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/get_ai_response', methods=['POST'])
def get_ai_response():
    user_input = request.json.get('message')
    if not user_input:
        return jsonify({'error': 'No message provided'}), 400

    # A dummy memory object, as MemoryManager is not integrated yet
    class DummyMemory:
        def __init__(self):
            pass
        def add_message(self, role, content):
            pass
        def get_history(self):
            return []

    dummy_memory = DummyMemory()
    router = PersonalityRouter()
    ai_response = router.get_response(user_input, dummy_memory)
    return jsonify({'response': ai_response})

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    if not user_message:
        return jsonify({'error': 'No message provided'}), 400

    # Process the message using NLPEngine and EchoPersonality
    nlp_engine = NLPEngine()
    personality = EchoPersonality()
    ai_response = nlp_engine.process_message(user_message, personality)

    return jsonify({'response': ai_response})

@app.route('/speech-to-text', methods=['POST'])
def speech_to_text():
    if 'audio' not in request.files:
        return jsonify({'error': 'No audio file provided'}), 400
    audio_file = request.files['audio']
    audio_bytes = audio_file.read()
    # Import and use SpeechToText
    from Core_Brain.speech_to_text import SpeechToText
    stt = SpeechToText()
    transcript = stt.process_audio_bytes(audio_bytes)
    return jsonify({'transcript': transcript})

if __name__ == '__main__':
    app.run(debug=True)