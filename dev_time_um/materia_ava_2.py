from api_wrapper.gemini_api_client import GeminiApiClient

class ChatMateria2:
    """Classe para gerar ideias criativas usando Gemini"""
    
    def __init__(self, gemini_client: GeminiApiClient):
        self.gemini_client = gemini_client
    
    def conversar(self, prompt):
        # Trocar ostextos para o que a função deve fazer#
        """Estabelece e explica de forma concisa a matéria fornecida"""
        prompt = f"""
        Estabeleça e explique de forma concisa a matéria: {prompt}
        
        Forneça:
        - Definição clara e objetiva da matéria
        - Principais conceitos fundamentais
        - Aplicações práticas ou importância
        - Resumo em 2-3 pontos principais
        
        Seja direto, preciso e didático na explicação.
        """
        ###################### Aqui não mexer ##########################
        try:
            resposta = self.gemini_client.generate_text(prompt)
            return resposta
        except Exception as e:
            return f"Erro ao explicar matéria: {e}"
        ################################################################