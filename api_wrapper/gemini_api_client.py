import google.generativeai as genai
import os 

class GeminiApiClient:
    """
    Cliente API para interagir DIRETAMENTE com o modelo Gemini do Google.
    Esta classe encapsula a lógica de chamada à API Gemini,
    utilizando a biblioteca oficial 'google-generativeai'.
    """
    def __init__(self, api_key: str = None, model_name: str = 'gemini-1.5-flash'):
        """
        Inicializa o cliente Gemini.
        Args:
            api_key (str): A chave de API para autenticação no Google Gemini.
                            Se não for fornecida, tentará buscar de GEMINI_API_KEY do ambiente.
            model_name (str): O nome do modelo Gemini a ser usado (padrão: 'gemini-1.5-flash').
        """
        if api_key is None:
            api_key = os.getenv('GEMINI_API_KEY')
            if not api_key:
                raise ValueError(
                    "GEMINI_API_KEY não fornecida. "
                    "Por favor, passe-a para o construtor ou defina a variável de ambiente."
                )

        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel(model_name)
    
    def generate_text(self, prompt: str) -> str:
        """
        Gera texto usando o modelo Gemini com base em um prompt fornecido.
        Args:
            prompt (str): O texto do prompt a ser enviado ao modelo Gemini.
        Returns:
            str: O texto gerado pelo modelo.
        Raises:
            Exception: Se ocorrer um erro durante a geração de conteúdo.
        """
        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            raise Exception(f"Erro ao gerar texto com Gemini: {e}") from e

    def start_chat_session(self, history: list = None, model_name: str = 'gemini-1.5-flash'):
        """
        Inicia ou continua uma sessão de chat com o modelo Gemini.
        Args:
            history (list, optional): Histórico de mensagens para iniciar o chat.
            model_name (str, optional): O nome do modelo de chat a ser usado.
        Returns:
            ChatSession: Um objeto de sessão de chat do Gemini.
        """
        return genai.GenerativeModel(model_name).start_chat(history=history)
