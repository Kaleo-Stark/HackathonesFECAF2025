from api_wrapper.gemini_api_client import GeminiApiClient

class GeradorDeIdeias:
    """Classe para gerar ideias criativas usando Gemini"""
    
    def __init__(self, gemini_client: GeminiApiClient):
        self.gemini_client = gemini_client
    
    def gerar_ideias(self, tema, quantidade=5):
        """Gera ideias sobre um tema específico"""
        prompt = f"""
        Gere {quantidade} ideias criativas e inovadoras sobre: {tema}
        
        Para cada ideia, forneça:
        - Nome/título da ideia
        - Descrição breve
        - Potencial de impacto
        
        Formato: Lista numerada, seja criativo e prático.
        """
        
        try:
            resposta = self.gemini_client.generate_text(prompt)
            return resposta
        except Exception as e:
            return f"Erro ao gerar ideias: {e}"
    
    def brainstorm_startup(self, setor):
        """Brainstorm específico para ideias de startup"""
        prompt = f"""
        Faça um brainstorm de 3 ideias de startup inovadoras para o setor: {setor}
        
        Para cada startup, inclua:
        - Nome da startup
        - Problema que resolve
        - Solução proposta
        - Modelo de negócio básico
        - Diferenciais competitivos
        
        Seja específico e realista.
        """
        
        try:
            resposta = self.gemini_client.generate_text(prompt)
            return resposta
        except Exception as e:
            return f"Erro no brainstorm: {e}"
