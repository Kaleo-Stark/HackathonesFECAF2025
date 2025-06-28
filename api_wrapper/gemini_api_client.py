import requests
import json

class GeminiApiClient:
    """Cliente para interagir com a API Gemini através do servidor Flask"""
    
    def __init__(self, base_url="http://127.0.0.1:5000"):
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update({
            'Content-Type': 'application/json'
        })
    
    def health_check(self):
        """Verifica se a API está funcionando"""
        try:
            response = self.session.get(f"{self.base_url}/health")
            return response.json()
        except Exception as e:
            raise Exception(f"Erro ao verificar saúde da API: {e}")
    
    def generate_text(self, prompt):
        """Gera texto usando o Gemini"""
        try:
            payload = {"prompt": prompt}
            response = self.session.post(
                f"{self.base_url}/generate-text",
                json=payload
            )
            
            if response.status_code == 200:
                return response.json()['generated_text']
            else:
                raise Exception(f"Erro na API: {response.json().get('error', 'Erro desconhecido')}")
                
        except Exception as e:
            raise Exception(f"Erro ao gerar texto: {e}")
    
    def chat_interaction(self, message, history=None):
        """Interage com o chat do Gemini"""
        try:
            if history is None:
                history = []
            
            payload = {
                "message": message,
                "history": history
            }
            
            response = self.session.post(
                f"{self.base_url}/chat",
                json=payload
            )
            
            if response.status_code == 200:
                data = response.json()
                return {
                    'response': data['response'],
                    'updated_history': data['updated_history']
                }
            else:
                raise Exception(f"Erro na API: {response.json().get('error', 'Erro desconhecido')}")
                
        except Exception as e:
            raise Exception(f"Erro na interação do chat: {e}")
