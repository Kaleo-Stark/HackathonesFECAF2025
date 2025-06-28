import os
from flask import Flask, request, jsonify
import google.generativeai as genai
from dotenv import load_dotenv
from dev_time_um.estudo_caso import EstudoCaso
from dev_time_um.conteudo_ava import ConteudoAva
from dev_time_um.materia_ava_1 import ChatMateria1
from dev_time_um.materia_ava_2 import ChatMateria2
from api_wrapper.gemini_api_client import GeminiApiClient

# Carregar variáveis de ambiente
load_dotenv()

app = Flask(__name__)

# Configurar Gemini
genai.configure(api_key=os.getenv('GEMINI_API_KEY'))
model = genai.GenerativeModel('gemini-1.5-flash')

# Instanciar cliente da API
#host = os.getenv('FLASK_HOST', '127.0.0.1')
#port = os.getenv('FLASK_PORT', '5000')
#base_url = f"http://{host}:{port}"
#gemini_client = GeminiApiClient(base_url)
gemini_client = GeminiApiClient(os.getenv('GEMINI_API_KEY'))
#=============================================(Daqui para baixo)===========================================)

@app.route('/analisarEstudoCaso', methods=['POST'])
def estudo_caso():
    estudo_caso = EstudoCaso(gemini_client)
    data = request.json

    prompt_professor = data.get('prompt')  # Ex: "Analise se o estudo está dentro do tema de sustentabilidade urbana"
    estudo_aluno = data.get('estudo')  # Ex: "O aluno escreveu que sustentabilidade..."

    # Verificação básica
    if not prompt_professor or not estudo_aluno:
        return jsonify({'erro': 'Prompt do professor e estudo de caso do aluno são obrigatórios.'}), 400

    # Chama o analisador passando os dois parâmetros certos
    analise = estudo_caso.analisar(prompt_professor, estudo_aluno)
    return jsonify(analise), 200

@app.route('/melhorarConteudoAva', methods=['POST'])
def ava_conteudo():
    conteudo_ava = ConteudoAva(gemini_client)
    data = request.json
    prompt_professor = data.get('prompt')  # Instrução personalizada
    conteudo_slides = data.get('conteudo')  # Texto do slide

    if not prompt_professor or not conteudo_slides:
        return jsonify({'erro': 'Dados incompletos. Envie o prompt e o conteúdo dos slides.'}), 400
    
    analise = conteudo_ava.analisar(prompt_professor, conteudo_slides)
    return jsonify({'analise': analise}), 200

@app.route('/chatMateria1', methods=['POST'])
def materia1():
    data = request.json
    pergunta = data.get('prompt')
    
    # Recebe o histórico anterior. Se não vier, começa com uma lista vazia.
    historico_anterior = data.get('historico', [])

    if not pergunta:
        return jsonify({'error': 'O campo "prompt" com a pergunta é obrigatório.'}), 400

    chat_materia = ChatMateria1(gemini_client)
    
    # A função agora recebe a pergunta e o histórico
    resposta, historico_novo = chat_materia.conversar(pergunta, historico_anterior)
    
    # Retornamos a resposta e também o novo histórico para o cliente
    return jsonify({
        'response': resposta,
        'historico': historico_novo 
    }), 200

@app.route('/chatMateria2', methods=['POST'])
def materia2():
    chat_materia = ChatMateria2(gemini_client)
    data = request.json # Recebe o JSON do corpo da requisição
    promptJSON = data.get('prompt') # Pega um valor do JSON
    promptGemini = "Analisa o qe veio aqui: " + promptJSON
    response = chat_materia.conversar("carro")
    return jsonify({'response': response}), 200

#============================================= NOVOS ENDPOINTS - TUTORIA EDUCACIONAL =============================================

@app.route('/chat', methods=['POST'])
def chat_tutoria():
    """Endpoint unificado para tutoria educacional de POO"""
    try:
        data = request.json
        prompt = data.get('prompt')
        
        if not prompt:
            return jsonify({'error': 'Parâmetro "prompt" é obrigatório'}), 400
        
        tutoria = ChatMateria2(gemini_client)
        
        # Usar o método conversar que já existe na classe
        resultado = tutoria.conversar(prompt)
        
        return jsonify({
            'prompt': prompt,
            'resultado': resultado
        }), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

####################(Não mexer abaixo)############################
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

#@app.route('/chat', methods=['POST'])
#def chat():
#    """Endpoint para interação de chat"""
#    try:
#        data = request.json
#        message = data.get('message')
#        history = data.get('history', [])
#        
#        if not message:
#            return jsonify({'error': 'Message é obrigatória'}), 400
#        
#        # Iniciar chat com histórico
#        chat_session = model.start_chat(history=history)
#        
#        # Enviar mensagem
#        response = chat_session.send_message(message)
#        
#        # Atualizar histórico
#        updated_history = chat_session.history
#        
#        return jsonify({
#            'response': response.text,
#            'message': message,
#            'updated_history': [
#                {
#                    'role': msg.role,
#                    'parts': [part.text for part in msg.parts]
#                } for msg in updated_history
#            ]
#        })
#    
#    except Exception as e:
#        return jsonify({'error': str(e)}), 500
#"""

if __name__ == '__main__':
    host = os.getenv('FLASK_HOST', '0.0.0.0')
    port = int(os.getenv('FLASK_PORT', 5000))
    
    print(f"🚀 Iniciando servidor Flask em {host}:{port}")
    app.run(host=host, port=port, debug=True)
