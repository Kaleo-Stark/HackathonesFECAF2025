from api_wrapper.gemini_api_client import GeminiApiClient

class ChatMateria2:
    """Classe para gerar ideias criativas usando Gemini"""
    
    def __init__(self, gemini_client: GeminiApiClient):
        self.gemini_client = gemini_client
    
    def conversar(self, prompt):
        # Trocar ostextos para o que a função deve fazer#
        """Gera ideias sobre um tema específico"""
        prompt = f"""
        Gere ideias criativas e inovadoras sobre: {prompt}
        
        Para cada ideia, forneça:
        - Nome/título da ideia
        - Descrição breve
        - Potencial de impacto
        
        Formato: Lista numerada, seja criativo e prático.
        """
        ###################### Aqui não mexer ##########################
        try:
            resposta = self.gemini_client.generate_text(prompt)
            return resposta
        except Exception as e:
            return f"Erro ao gerar ideias: {e}"
        ################################################################