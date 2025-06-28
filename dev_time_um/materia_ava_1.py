# Arquivo: dev_time_um/materia_ava_1.py

from api_wrapper.gemini_api_client import GeminiApiClient

# O conteúdo da matéria continua o mesmo, servindo como base.
CONTEUDO_DA_MATERIA = """
### MÓDULO 1: INTRODUÇÃO A BANCOS DE DADOS E SQL ###

**1.1. O que é SQL?**
SQL (Structured Query Language) é a linguagem padrão para gerenciar bancos de dados relacionais.
Comandos principais: SELECT, INSERT, UPDATE, DELETE, CREATE, DROP.

**1.2. Comandos DML - Manipulando Dados**
- `INSERT INTO tabela VALUES (...);`
- `UPDATE tabela SET coluna = novo_valor WHERE condicao;`
- `DELETE FROM tabela WHERE condicao;`

**1.3. Comandos DQL - Consultando Dados com SELECT**
- `SELECT * FROM tabela WHERE condicao;`
- Cláusulas importantes: WHERE, ORDER BY, GROUP BY.

### MÓDULO 2: JOINs - Combinando Tabelas ###

**2.1. INNER JOIN**
Retorna apenas os registros que têm correspondência em ambas as tabelas.
Exemplo: `SELECT A.nome, B.pedido FROM Clientes A INNER JOIN Pedidos B ON A.ID = B.ClienteID;`

**2.2. LEFT JOIN**
Retorna TODOS os registros da tabela da esquerda e os correspondentes da tabela da direita.
Exemplo: `SELECT A.nome, B.pedido FROM Clientes A LEFT JOIN Pedidos B ON A.ID = B.ClienteID;`

### MÓDULO 3: MODELAGEM DE DADOS E NORMALIZAÇÃO ###

**3.1. Chaves (Keys)**
- Chave Primária (Primary Key): Identificador único de uma linha.
- Chave Estrangeira (Foreign Key): Campo que aponta para a Chave Primária de outra tabela.

**3.2. Normalização**
Processo para organizar tabelas e minimizar a redundância de dados (1FN, 2FN, 3FN).
"""

class ChatMateria1:
    """
    Tutor de IA que mantém o histórico da conversa no servidor.
    """
    
    def __init__(self, gemini_client: GeminiApiClient):
        self.gemini_client = gemini_client
    
    def conversar(self, duvida_aluno: str, historico: list = None):
        """
        Recebe a dúvida e o histórico, retorna a resposta e o histórico atualizado.
        O histórico é usado pela IA para manter o contexto.
        """
        if historico is None:
            historico = []

        prompt_para_ia = f"""
        Você é um "Tutor de IA Multifuncional" especialista em Banco de Dados. Siga estas regras de conversa RIGOROSAMENTE.

        **REGRA 1: É A PRIMEIRA MENSAGEM?**
        - VERIFIQUE se o "Histórico da Conversa" abaixo está VAZIO.
        - SE ESTIVER VAZIO, esta é a primeira interação. Sua resposta DEVE OBRIGATORIAMENTE ter duas partes:
          1. Uma saudação e o menu de "Ações Disponíveis".
          2. A resposta direta para a "Pergunta do Aluno".

        **REGRA 2: É UMA MENSAGEM DE CONTINUAÇÃO?**
        - SE o "Histórico da Conversa" NÃO ESTIVER VAZIO, esta é uma continuação.
        - Responda DIRETAMENTE à "Pergunta do Aluno" sem nenhuma saudação ou menu.
        - Ao final da sua resposta, adicione a seguinte frase em uma nova linha: "Para voltar ao menu, digite 1."

        **REGRA 3: O ALUNO PEDIU O MENU?**
        - SE a "Pergunta do Aluno" for exatamente o número "1", ignore as outras regras e apenas mostre a lista de "Ações Disponíveis".

        **Ações Disponíveis (Apresentar no menu):**
        - **Explorar Conceitos:** Peça para explicar qualquer tópico (Ex: "explique o que é Normalização").
        - **Resolver Exercícios:** Envie um problema e peça a resolução passo a passo.
        - **Criar Quiz:** Peça um quiz sobre um assunto para testar seu conhecimento.
        - **Planejar Estudos:** Peça ajuda para criar um plano de estudos.

        **Instruções Gerais:**
        - Use o "Conteúdo de Referência" como sua principal fonte de verdade para garantir a precisão.
        - Elabore a resposta de forma didática e completa.

        ---
        Conteúdo de Referência:
        {CONTEUDO_DA_MATERIA}
        ---

        Histórico da Conversa:
        {historico}
        ---

        Pergunta do Aluno:
        "{duvida_aluno}"

        Sua resposta (seguindo as regras acima):
        """
        
        try:
            resposta = self.gemini_client.generate_text(prompt_para_ia)
            
            # Adiciona a nova interação ao histórico para a próxima rodada
            historico_atualizado = historico + [
                {'role': 'user', 'parts': [duvida_aluno]},
                {'role': 'model', 'parts': [resposta]}
            ]
            
            # Retorna a resposta E o histórico atualizado
            return resposta, historico_atualizado

        except Exception as e:
            print(f"ERRO ao contatar a API Gemini: {e}")
            return "Desculpe, ocorreu um problema técnico.", historico
