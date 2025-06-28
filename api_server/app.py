import os
from flask import Flask, request, jsonify
import google.generativeai as genai
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()

app = Flask(__name__)

# Configurar Gemini
genai.configure(api_key=os.getenv('GEMINI_API_KEY'))
model = genai.GenerativeModel('gemini-1.5-flash')

@app.route('/health', methods=['GET'])
def health_check():
    """Endpoint para verificar se a API está funcionando"""
    return jsonify({
        'status': 'healthy',
        'message': 'API Gemini está funcionando!'
    })

@app.route('/generate-text', methods=['POST'])
def generate_text():
    """Endpoint para geração de texto"""
    try:
        data = request.json
        prompt = data.get('prompt')
        
        if not prompt:
            return jsonify({'error': 'Prompt é obrigatório'}), 400
        
        # Gerar texto com Gemini
        response = model.generate_content(prompt)
        
        return jsonify({
            'generated_text': response.text,
            'prompt': prompt
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/chat', methods=['POST'])
def chat():
    """Endpoint para interação de chat"""
    try:
        data = request.json
        message = data.get('message')
        history = data.get('history', [])
        
        if not message:
            return jsonify({'error': 'Message é obrigatória'}), 400
        
        # Iniciar chat com histórico
        chat_session = model.start_chat(history=history)
        
        # Enviar mensagem
        response = chat_session.send_message(message)
        
        # Atualizar histórico
        updated_history = chat_session.history
        
        return jsonify({
            'response': response.text,
            'message': message,
            'updated_history': [
                {
                    'role': msg.role,
                    'parts': [part.text for part in msg.parts]
                } for msg in updated_history
            ]
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    host = os.getenv('FLASK_HOST', '127.0.0.1')
    port = int(os.getenv('FLASK_PORT', 5000))
    
    print(f"🚀 Iniciando servidor Flask em {host}:{port}")
    app.run(host=host, port=port, debug=False)
