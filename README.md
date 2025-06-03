# API Businesses of the Industry - Solução Local

Esta é uma versão simplificada e robusta da API Businesses of the Industry, projetada para funcionar localmente sem problemas de compatibilidade.

## Estrutura do Projeto

- `app.py` - Arquivo principal da API com todos os endpoints e dados simulados
- `requirements.txt` - Dependências mínimas necessárias
- `README.md` - Documentação e instruções

## Como Executar Localmente

### Pré-requisitos

- Python 3.6 ou superior
- pip (gerenciador de pacotes do Python)

### Passos para Execução

1. **Crie um ambiente virtual (recomendado)**

```bash
# No Windows
python -m venv venv
venv\Scripts\activate

# No macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

2. **Instale as dependências**

```bash
pip install -r requirements.txt
```

3. **Execute a API**

```bash
python app.py
```

4. **Acesse a API**

A API estará disponível em: http://localhost:5000

## Endpoints Disponíveis

- `GET /` - Informações sobre a API
- `GET /api/health` - Verificação de saúde da API
- `GET /api/industries` - Lista todas as indústrias (aceita filtros)
- `GET /api/industries/<id>` - Detalhes de uma indústria específica
- `GET /api/industries/search` - Busca avançada de indústrias
- `GET /api/sectors` - Lista todos os setores disponíveis
- `GET /api/countries` - Lista todos os países disponíveis

## Exemplos de Uso

### Listar todas as indústrias
```
GET http://localhost:5000/api/industries
```

### Filtrar indústrias por setor
```
GET http://localhost:5000/api/industries?sector=Tecnologia
```

### Buscar indústrias por texto
```
GET http://localhost:5000/api/industries/search?q=tech
```

### Obter detalhes de uma indústria específica
```
GET http://localhost:5000/api/industries/ind001
```

## Opções de Deploy

Se desejar fazer o deploy desta API, recomendamos as seguintes plataformas que são mais compatíveis com esta estrutura:

### 1. PythonAnywhere

1. Crie uma conta em [PythonAnywhere](https://www.pythonanywhere.com/)
2. Faça upload dos arquivos
3. Configure um novo aplicativo web usando Flask
4. Defina o arquivo WSGI para apontar para `app.py`

### 2. Heroku

1. Crie um arquivo `Procfile` com o conteúdo: `web: gunicorn app:app`
2. Faça upload dos arquivos para um repositório Git
3. Conecte o Heroku ao repositório
4. Deploy a aplicação

### 3. Railway

1. Crie uma conta no [Railway](https://railway.app/)
2. Conecte ao repositório Git com os arquivos
3. Configure o comando de inicialização: `gunicorn app:app`

## Observações Importantes

- Esta versão usa dados simulados em memória, sem necessidade de banco de dados
- Para um ambiente de produção, considere adicionar autenticação e persistência de dados
- A API está configurada para permitir CORS, facilitando a integração com frontends
