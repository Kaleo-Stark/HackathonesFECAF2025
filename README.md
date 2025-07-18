# 🚀 Hackathon FECAF 2025 - API Tutoria Educacional POO

## 📋 Descrição
API desenvolvida para ajudar alunos a entender melhor Programação Orientada a Objetos (POO), utilizando inteligência artificial (Google Gemini) para fornecer tutoria personalizada focada em conceitos de programação.

## 🛠️ Tecnologias
- **Python 3.x**
- **Flask** - Framework web
- **Google Gemini AI** - IA para geração de conteúdo educacional
- **Postman** - Para testar a API

## 🚀 Como Executar

### 1. Instalar Dependências
```bash
pip install -r requirements.txt
```

### 2. Configurar API Key
Crie um arquivo `.env` na raiz do projeto:
```
GEMINI_API_KEY=sua_chave_api_aqui
```

### 3. Executar o Projeto
```bash
python main.py
```

O servidor será iniciado em: `http://127.0.0.1:5000`

## 📚 Endpoints da API

### Base URL: `http://127.0.0.1:5000`

---

## 🚀 Endpoint Unificado `/chat`

**POST** `/chat`

Endpoint único e simplificado para tutoria educacional de POO.

### Como Usar:

**Body:**
```json
{
    "prompt": "Não entendi a parte do polimorfismo"
}
```

**Resposta:**
```json
{
    "prompt": "Não entendi a parte do polimorfismo",
    "resultado": "Polimorfismo é um dos pilares da POO que permite..."
}
```

**📖 Documentação completa:** [ENDPOINT_CHAT_UNIFICADO.md](ENDPOINT_CHAT_UNIFICADO.md)

---

## 🧪 Como Testar no Postman

### Configuração:
1. **Método:** POST
2. **URL:** `http://127.0.0.1:5000/chat`
3. **Headers:** 
   - Key: `Content-Type`
   - Value: `application/json`
4. **Body:** 
   - Selecione "raw"
   - Escolha "JSON"
   - Cole o body com apenas o campo "prompt"

### Exemplos de Teste:

#### 1. Dúvida sobre conceito:
```json
{
    "prompt": "Não entendi a parte do polimorfismo"
}
```

#### 2. Pergunta sobre exercício:
```json
{
    "prompt": "Como crio uma classe Animal em Java?"
}
```

#### 3. Explicação de conceito:
```json
{
    "prompt": "Explique herança em POO"
}
```

---

## 🎯 Exemplos de Prompts para Testar

### Básico
- "Não entendi a parte do polimorfismo"
- "Como instancio uma classe em Java?"
- "O que é encapsulamento?"
- "Explique classe e objeto"

### Intermediário
- "Diferença entre classe abstrata e interface"
- "Como funciona herança múltipla?"
- "O que é polimorfismo de sobrecarga?"
- "Explique o conceito de interfaces"

### Avançado
- "Como implementar o padrão Singleton?"
- "Explique os princípios SOLID"
- "Diferença entre composição e agregação"
- "Como usar generics em POO?"

---

## 🔧 Estrutura do Projeto

```
HackathonesFECAF2025/
├── main.py                 # Arquivo principal
├── requirements.txt        # Dependências
├── README.md              # Este arquivo
├── ENDPOINT_CHAT_UNIFICADO.md # Documentação do endpoint
├── api_server/
│   └── app.py             # Servidor Flask
├── dev_time_um/
│   ├── materia_ava_2.py   # Classe de tutoria educacional POO
│   └── ...
├── dev_time_dois/
│   └── ...
└── api_wrapper/
    └── gemini_api_client.py
```

---

## 🚨 Solução de Problemas

### Erro 404
- Verifique se o servidor está rodando
- Confirme a URL está correta
- Verifique se o JSON está formatado

### Erro de Credenciais
- Certifique-se que a `GEMINI_API_KEY` está configurada no `.env`
- Verifique se a chave é válida

### Erro de Importação
- Execute `pip install -r requirements.txt`
- Verifique se todas as dependências estão instaladas

---

## 🎉 Funcionalidades

- ✅ Explicação didática de conceitos de POO
- ✅ Resolução passo a passo de exercícios
- ✅ Criação de quizzes educativos
- ✅ Resposta de dúvidas específicas
- ✅ Planejamento de estudos personalizado
- ✅ Suporte a diferentes níveis (básico, intermediário, avançado)
- ✅ Foco específico em Programação Orientada a Objetos
- ✅ Endpoint unificado com apenas um parâmetro `prompt`

---

## 📞 Suporte

Para dúvidas ou problemas, verifique:
1. Se o servidor está rodando
2. Se a API key está configurada
3. Se o JSON está formatado corretamente
4. Se a URL está correta
5. Se o parâmetro "prompt" está presente

---

## �� Pronto para usar!

Agora você pode usar um único endpoint `/chat` com apenas o campo `prompt` para qualquer dúvida sobre POO! 🎯
