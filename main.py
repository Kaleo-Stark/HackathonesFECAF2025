import os
import time
import threading
import subprocess
from dotenv import load_dotenv
from api_wrapper.gemini_api_client import GeminiApiClient
from dev_time_um.gerador_de_ideias import GeradorDeIdeias
from dev_time_um.analisador_de_texto import AnalisadorDeTexto
from dev_time_um.materia_ava_2 import ChatMateria2
from dev_time_dois.bot_atendimento import BotAtendimento
from dev_time_dois.resumidor_conteudo import ResumidorConteudo

# Carregar variáveis de ambiente
load_dotenv()

def start_flask_server():
    """Inicia o servidor Flask em segundo plano"""
    os.system("python -m api_server.app")

def main():
    print("🚀 Iniciando Projeto Hackathon - API Gemini Modular")
    print("=" * 50)
    
    # Iniciar servidor Flask em thread separada
    print("📡 Iniciando servidor Flask...")
    flask_thread = threading.Thread(target=start_flask_server, daemon=True)
    flask_thread.start()
    
    # Aguardar servidor inicializar
    print("⏳ Aguardando servidor inicializar...")
    time.sleep(3)
    
    # Instanciar cliente da API
    host = os.getenv('FLASK_HOST', '127.0.0.1')
    port = os.getenv('FLASK_PORT', '5000')
    base_url = f"http://{host}:{port}"
    
    gemini_client = GeminiApiClient(base_url)
    
    print(f"✅ Servidor rodando em: {base_url}")
    print("=" * 50)
    
    # Demonstrar uso das classes dos times
    try:
        print("\n🔥 DEMONSTRAÇÃO - TIME UM")
        print("-" * 30)
        
        # Gerador de Ideias
        gerador = GeradorDeIdeias(gemini_client)
        ideias = gerador.gerar_ideias("aplicativo mobile inovador")
        print(f"💡 Ideias geradas: {ideias[:100]}...")
        
        # Analisador de Texto
        analisador = AnalisadorDeTexto(gemini_client)
        sentimento = analisador.analisar_sentimento("Estou muito feliz com este projeto!")
        print(f"😊 Análise de sentimento: {sentimento}")
        
        print("\n🔥 DEMONSTRAÇÃO - TIME DOIS")
        print("-" * 30)
        
        # Bot de Atendimento
        bot = BotAtendimento(gemini_client)
        resposta = bot.responder_cliente("Olá, preciso de ajuda com meu pedido")
        print(f"🤖 Bot responde: {resposta[:100]}...")
        
        # Resumidor de Conteúdo
        resumidor = ResumidorConteudo(gemini_client)
        resumo = resumidor.resumir_texto("""
        A inteligência artificial está transformando diversos setores da economia.
        Empresas estão adotando IA para automatizar processos, melhorar a experiência
        do cliente e otimizar operações. O machine learning permite que sistemas
        aprendam com dados e tomem decisões mais precisas.
        """)
        print(f"📝 Resumo: {resumo}")
        
        print("\n🔥 DEMONSTRAÇÃO - TUTORIA EDUCACIONAL (POO)")
        print("-" * 50)
        
        # Tutoria Educacional - ChatMateria2
        tutoria = ChatMateria2(gemini_client)
        
        # Testar com prompt direto
        explicacao = tutoria.conversar("Programação Orientada a Objetos")
        print(f"📚 Explicação POO: {explicacao[:150]}...")
        
        print("\n🔥 DEMONSTRAÇÃO - ENDPOINT UNIFICADO /chat")
        print("-" * 50)
        
        # Testar o endpoint unificado /chat
        import requests
        
        # 1. Pergunta sobre conceito
        response = requests.post(f"{base_url}/chat", json={
            "prompt": "Não entendi a parte do polimorfismo"
        })
        if response.status_code == 200:
            print(f"📚 /chat: {response.json()['resultado'][:100]}...")
        
        # 2. Pergunta sobre exercício
        response = requests.post(f"{base_url}/chat", json={
            "prompt": "Como crio uma classe Animal em Java?"
        })
        if response.status_code == 200:
            print(f"🧮 /chat: {response.json()['resultado'][:100]}...")
        
        # 3. Pergunta sobre conceito
        response = requests.post(f"{base_url}/chat", json={
            "prompt": "Explique herança em POO"
        })
        if response.status_code == 200:
            print(f"❓ /chat: {response.json()['resultado'][:100]}...")
        
        # 4. Pergunta sobre dúvida
        response = requests.post(f"{base_url}/chat", json={
            "prompt": "Qual a diferença entre classe e objeto?"
        })
        if response.status_code == 200:
            print(f"🤔 /chat: {response.json()['resultado'][:100]}...")
        
        # 5. Pergunta sobre planejamento
        response = requests.post(f"{base_url}/chat", json={
            "prompt": "Quero aprender POO, como devo estudar?"
        })
        if response.status_code == 200:
            print(f"📅 /chat: {response.json()['resultado'][:100]}...")
        
    except Exception as e:
        print(f"❌ Erro na demonstração: {e}")
        print("💡 Certifique-se de que sua GEMINI_API_KEY está configurada corretamente no .env")
    
    print("\n" + "=" * 50)
    print("✨ Demonstração concluída! O servidor continua rodando...")
    print("🌐 Acesse os endpoints em:")
    print(f"   • {base_url}/generate-text")
    print(f"   • {base_url}/chat (endpoint unificado para tutoria POO)")
    print("")
    print("📚 Como usar o /chat:")
    print("   • Envie um JSON com apenas o campo 'prompt'")
    print("   • Exemplo: {\"prompt\": \"Não entendi polimorfismo\"}")
    print("   • A IA responderá automaticamente baseada no contexto")
    print("🔄 Pressione Ctrl+C para parar")
    
    # Manter o programa rodando
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n👋 Encerrando aplicação...")

if __name__ == "__main__":
    main()
