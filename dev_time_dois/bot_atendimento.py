from api_wrapper.gemini_api_client import GeminiApiClient

class BotAtendimento:
    """Bot de atendimento ao cliente usando Gemini"""
    
    def __init__(self, gemini_client: GeminiApiClient):
        self.gemini_client = gemini_client
        self.historico_conversas = {}
    
    def responder_cliente(self, mensagem, cliente_id="default"):
        """Responde uma mensagem do cliente"""
        prompt = f"""
        Você é um assistente de atendimento ao cliente profissional e amigável.
        
        Cliente disse: "{mensagem}"
        
        Responda de forma:
        - Educada e profissional
        - Útil e solucionadora
        - Empática quando necessário
        - Concisa mas completa
        
        Se não souber algo específico, oriente o cliente para onde pode obter ajuda.
        """
        
        try:
            resposta = self.gemini_client.generate_text(prompt)
            return resposta
        except Exception as e:
            return f"Desculpe, ocorreu um erro técnico. Tente novamente em alguns momentos."
    
    def chat_com_historico(self, mensagem, cliente_id):
        """Mantém conversa com histórico por cliente"""
        if cliente_id not in self.historico_conversas:
            self.historico_conversas[cliente_id] = []
        
        try:
            resultado = self.gemini_client.chat_interaction(
                mensagem, 
                self.historico_conversas[cliente_id]
            )
            
            # Atualizar histórico
            self.historico_conversas[cliente_id] = resultado['updated_history']
            
            return resultado['response']
        except Exception as e:
            return f"Desculpe, ocorreu um erro técnico. Tente novamente."
