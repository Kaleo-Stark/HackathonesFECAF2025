from api_wrapper.gemini_api_client import GeminiApiClient

class ConteudoAva:
    """Classe para analisar conteúdo de slides e gerar sugestões de melhoria usando Gemini"""
    
    def __init__(self, gemini_client: GeminiApiClient):
        self.gemini_client = gemini_client
    
    def analisar(self, prompt_professor: str, conteudo_slides: str):
        """
        Analisa o conteúdo dos slides com base em um prompt do professor, 
        gerando sugestões de afinamento e melhorias.

        Args:
            prompt_professor (str): O prompt fornecido pelo professor, 
                                    com as diretrizes para a análise.
            conteudo_slides (str): O texto extraído do conteúdo dos slides.

        Returns:
            str: As sugestões de afinamento e melhorias geradas pela IA, 
                 ou uma mensagem de erro.
        """
        # Adaptação do prompt para a nova funcionalidade
        prompt_para_ia = f"""
        Você é um assistente de IA especializado em otimização de conteúdo educacional.
        Seu objetivo é analisar o material de aula fornecido e, com base no prompt do professor,
        oferecer sugestões detalhadas para afinamento e melhoria do conteúdo.

        **Prompt do Professor:**
        {prompt_professor}

        **Conteúdo dos Slides para Análise:**
        ---
        {conteudo_slides}
        ---

        Com base no "Prompt do Professor" e analisando o "Conteúdo dos Slides",
        forneça sugestões práticas e acionáveis para:
        1.  **Afinamento do Conteúdo:** Como tornar o material mais conciso, claro ou focado.
        2.  **Melhorias Didáticas:** Sugestões para tornar o material mais engajante, interativo,
            fácil de entender ou memorizar (ex: exemplos, analogias, exercícios, estrutura).
        3.  **Expansão/Aprofundamento (se aplicável):** Pontos onde o conteúdo pode ser
            expandido para maior riqueza, ou onde uma conexão com outros tópicos seria benéfica.
        4.  **Correção/Clareza (se aplicável):** Identificação de possíveis ambiguidades, erros
            conceituais ou áreas que necessitam de maior clareza.

        Formate suas sugestões de forma clara e organizada, utilizando tópicos ou listas numeradas.
        Seja direto e objetivo.
        """

        ###################### Aqui não mexer ##########################
        try:
            resposta = self.gemini_client.generate_text(prompt_para_ia)
            return resposta
        except Exception as e:
            return f"Erro ao gerar sugestões: {e}"
        ################################################################