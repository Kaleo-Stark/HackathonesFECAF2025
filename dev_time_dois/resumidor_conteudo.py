from api_wrapper.gemini_api_client import GeminiApiClient

class ResumidorConteudo:
    """Classe para resumir conteúdos usando Gemini"""
    
    def __init__(self, gemini_client: GeminiApiClient):
        self.gemini_client = gemini_client
    
    def resumir_texto(self, texto, tamanho="medio"):
        """Resume um texto em diferentes tamanhos"""
        tamanhos = {
            "curto": "em 2-3 frases",
            "medio": "em 1 parágrafo",
            "longo": "em 2-3 parágrafos"
        }
        
        instrucao_tamanho = tamanhos.get(tamanho, tamanhos["medio"])
        
        prompt = f"""
        Resuma o seguinte texto {instrucao_tamanho}:
        
        "{texto}"
        
        Mantenha as informações mais importantes e o contexto principal.
        O resumo deve ser claro e bem estruturado.
        """
        
        try:
            resposta = self.gemini_client.generate_text(prompt)
            return resposta
        except Exception as e:
            return f"Erro ao resumir texto: {e}"
    
    def extrair_pontos_principais(self, texto):
        """Extrai os pontos principais de um texto"""
        prompt = f"""
        Extraia os pontos principais do seguinte texto:
        
        "{texto}"
        
        Retorne em formato de lista com bullet points (•).
        Máximo 7 pontos, priorizando os mais importantes.
        """
        
        try:
            resposta = self.gemini_client.generate_text(prompt)
            return resposta
        except Exception as e:
            return f"Erro ao extrair pontos principais: {e}"
