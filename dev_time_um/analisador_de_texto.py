from api_wrapper.gemini_api_client import GeminiApiClient

class AnalisadorDeTexto:
    """Classe para análise de texto usando Gemini"""
    
    def __init__(self, gemini_client: GeminiApiClient):
        self.gemini_client = gemini_client
    
    def analisar_sentimento(self, texto):
        """Analisa o sentimento de um texto"""
        prompt = f"""
        Analise o sentimento do seguinte texto: "{texto}"
        
        Forneça:
        - Sentimento principal (Positivo/Negativo/Neutro)
        - Intensidade (Baixa/Média/Alta)
        - Emoções identificadas
        - Justificativa da análise
        
        Seja preciso e objetivo.
        """
        
        try:
            resposta = self.gemini_client.generate_text(prompt)
            return resposta
        except Exception as e:
            return f"Erro na análise de sentimento: {e}"
    
    def extrair_palavras_chave(self, texto, quantidade=10):
        """Extrai palavras-chave de um texto"""
        prompt = f"""
        Extraia as {quantidade} palavras-chave mais importantes do texto:
        
        "{texto}"
        
        Retorne apenas as palavras-chave separadas por vírgula, ordenadas por relevância.
        """
        
        try:
            resposta = self.gemini_client.generate_text(prompt)
            return resposta
        except Exception as e:
            return f"Erro na extração de palavras-chave: {e}"
