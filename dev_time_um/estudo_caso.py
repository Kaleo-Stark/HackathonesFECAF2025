from api_wrapper.gemini_api_client import GeminiApiClient

class EstudoCaso:
    """Classe para gerar ideias criativas usando Gemini"""
    
    def __init__(self, gemini_client: GeminiApiClient):
        """
        Inicializa a classe EstudoCaso com uma instância de GeminiApiClient.
        Esta instância é responsável por se comunicar diretamente com a API do Google Gemini.
        """
        self.gemini_client = gemini_client
    
    def analisar(self, prompt_professor: str, estudo_aluno: str):
        """
        Analisa um estudo de caso do aluno com base nas instruções do professor
        usando o modelo Gemini.

        Args:
            prompt_professor (str): O prompt ou tema fornecido pelo professor.
            estudo_aluno (str): O estudo de caso escrito pelo aluno.

        Returns:
            str: A análise do modelo Gemini ou uma mensagem de erro.
        """
        print("Preparando a análise do prompt do professor e o estudo do aluno...")

        # Construção do prompt final para o Gemini, exatamente como estava no seu serviço C#.
        # Este é o texto completo que será enviado ao modelo de IA.
        prompt = f"""
Você deve se comportar com uma API de avaliação de estudos de caso.

Você irá avaliar estudos de caso. Receberá um tema e instruções, seguido de um estudo de caso feito por um aluno.

Seu trabalho é:
- Analisar se o estudo de caso está de acordo com o tema e as instruções.
- Se não estiver dentro do tema, apontar os pontos a serem verificados e corrigidos de forma clara e direta, justificando o por quê de aquele trecho estar errado e adicionar essa resposta no JSON de retorno.
- Preencher as informações do JSON abaixo:

OBSERVAÇÃO: Você é uma API e em todas as repostas você deve retornar o seguinte JSON:
{{
    "status": <aprovado | reprovado | revisão>,
    "nota": <0-10>,
    "justificativa": <Texto explicativo sobre a nota e o status>
}}
===============(Prompt do professor)================
{prompt_professor}
====================================================

=============(Estudo de caso do aluno)==============
{estudo_aluno}
====================================================

Você deve retornar apenas o JSON acima, sem mais explicações ou textos adicionais.
"""
        
        print("Prompt formatado para o Gemini:\n", prompt)
        
        ###################### Aqui não mexer ##########################
        try:
            resposta = self.gemini_client.generate_text(prompt)
            return resposta
        except Exception as e:
            return f"Erro ao gerar ideias: {e}"
        ################################################################