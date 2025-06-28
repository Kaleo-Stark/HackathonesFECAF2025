    import os
    from flask import Flask, request, jsonify
    import google.generativeai as genai
    from dotenv import load_dotenv

    from api_wrapper.gemini_api_client import GeminiApiClient 
    from dev_time_um.estudo_caso import EstudoCaso
    from dev_time_um.conteudo_ava import ConteudoAva
    from dev_time_um.materia_ava_1 import ChatMateria1
    from dev_time_um.materia_ava_2 import ChatMateria2
    from dev_time_dois.bot_atendimento import BotAtendimento 
    from dev_time_dois.resumidor_conteudo import ResumidorConteudo 

    # Carregar variáveis de ambiente
    load_dotenv()

    app = Flask(__name__)

    # --- CONFIGURAÇÃO GLOBAL DO GEMINI E INSTANCIAÇÃO DO CLIENTE ---
    # Configure o genai UMA ÚNICA VEZ globalmente no ponto de entrada da API.
    # Esta linha é essencial para todas as interações com a API Gemini.
    genai.configure(api_key=os.getenv('GEMINI_API_KEY'))

    # Instância do modelo padrão (usado por /generate-text e, indiretamente, pelo GeminiApiClient)
    model = genai.GenerativeModel('gemini-1.5-flash')

    # Agora, instancie o seu GeminiApiClient (o cliente direto do Google Gemini)
    # Ele pega a API_KEY automaticamente do ambiente.
    gemini_client = GeminiApiClient() 
    # ----------------------------------------------------------------

    #=============================================(Daqui para baixo)===========================================)

    @app.route('/analisarEstudoCaso', methods=['POST'])
    def estudo_caso():
        estudo_caso = EstudoCaso(gemini_client)
        data = request.json

        prompt_professor = data.get('prompt')   
        estudo_aluno = data.get('estudo')    

        if not prompt_professor or not estudo_aluno:
            return jsonify({'erro': 'Prompt do professor e estudo de caso do aluno são obrigatórios.'}), 400

        try:
            analise = estudo_caso.analisar(prompt_professor, estudo_aluno)
            return jsonify(analise), 200 
        except Exception as e:
            return jsonify({'erro': f'Erro ao processar estudo de caso: {str(e)}'}), 500


    @app.route('/melhorarConteudoAva', methods=['POST'])
    def ava_conteudo():
        conteudo_ava = ConteudoAva(gemini_client)
        data = request.json
        prompt_professor = data.get('prompt')   
        conteudo_slides = data.get('conteudo')  

        if not prompt_professor or not conteudo_slides:
            return jsonify({'erro': 'Dados incompletos. Envie o prompt e o conteúdo dos slides.'}), 400
        
        try:
            analise = conteudo_ava.analisar(prompt_professor, conteudo_slides)
            return jsonify({'analise': analise}), 200
        except Exception as e:
            return jsonify({'erro': f'Erro ao melhorar conteúdo AVA: {str(e)}'}), 500


    @app.route('/chatMateria1', methods=['POST'])
    def materia1():
        data = request.json
        pergunta = data.get('prompt')
        historico_anterior = data.get('historico', [])

        if not pergunta:
            return jsonify({'error': 'O campo "prompt" com a pergunta é obrigatório.'}), 400

        chat_materia = ChatMateria1(gemini_client)
        
        try:
            resposta, historico_novo = chat_materia.conversar(pergunta, historico_anterior)
            return jsonify({
                'response': resposta,
                'historico': historico_novo 
            }), 200
        except Exception as e:
            return jsonify({'erro': f'Erro no chat da Matéria 1: {str(e)}'}), 500


    @app.route('/chatMateria2', methods=['POST'])
    def materia2():
        chat_materia = ChatMateria2(gemini_client)
        data = request.json
        promptJSON = data.get('prompt')

        if not promptJSON:
            return jsonify({'error': 'O campo "prompt" é obrigatório.'}), 400

        try:
            response = chat_materia.conversar(promptJSON)
            return jsonify({'response': response}), 200
        except Exception as e:
            return jsonify({'erro': f'Erro no chat da Matéria 2: {str(e)}'}), 500

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
            
            resultado = tutoria.conversar(prompt)
            
            return jsonify({
                'prompt': prompt,
                'resultado': resultado
            }), 200
            
        except Exception as e:
            return jsonify({'error': f'Erro na tutoria de chat: {str(e)}'}), 500

    ####################(Não mexer abaixo)############################
    @app.route('/generate-text', methods=['POST'])
    def generate_text():
        """
        Endpoint para geração de texto usando o modelo Gemini global.
        Este endpoint agora usa a instância 'model' que já está configurada
        com o genai.configure(api_key=...) no início do arquivo.
        """
        try:
            data = request.json
            prompt = data.get('prompt')
            
            if not prompt:
                return jsonify({'error': 'Prompt é obrigatório'}), 400
            
            response = model.generate_content(prompt)
            
            return jsonify({
                'generated_text': response.text,
                'prompt': prompt
            })
        
        except Exception as e:
            return jsonify({'error': f'Erro no endpoint /generate-text: {str(e)}'}), 500

    if __name__ == '__main__':
        host = os.getenv('FLASK_HOST', '0.0.0.0') 
        port = int(os.getenv('FLASK_PORT', 5000))
        
        print(f"🚀 Iniciando servidor Flask em {host}:{port}")
        app.run(host=host, port=port, debug=True)

    