# Guia de Deploy da API Businesses of the Industry no Render

Este guia contém instruções detalhadas para fazer o deploy da API Businesses of the Industry no Render.

## Arquivos Incluídos

- `app.py` - Arquivo principal da API com todos os endpoints e dados simulados
- `requirements.txt` - Dependências necessárias com versões específicas
- `Procfile` - Instruções para o servidor web no Render

## Passos para Deploy no Render

### 1. Criar uma conta no Render (caso ainda não tenha)

1. Acesse [render.com](https://render.com)
2. Clique em "Sign Up" e crie uma conta (pode usar GitHub, GitLab ou e-mail)

### 2. Criar um novo Web Service

1. No Dashboard do Render, clique no botão "New +" no canto superior direito
2. Selecione "Web Service"
3. Escolha "Deploy from Git repository" ou "Deploy manually" (conforme sua preferência)

### 3. Configurar o Serviço

Se estiver usando Git:
1. Conecte seu repositório GitHub/GitLab
2. Selecione o repositório com os arquivos da API

Se estiver fazendo upload manual:
1. Faça upload dos arquivos extraídos do zip fornecido

Em ambos os casos, configure:
- **Name**: businesses-industry-api (ou nome de sua preferência)
- **Runtime**: Python 3
- **Build Command**: `pip install -r requirements.txt`
- **Start Command**: `gunicorn app:app` (MUITO IMPORTANTE - este é o comando correto)
- **Plan**: Free

### 4. Iniciar o Deploy

1. Clique em "Create Web Service"
2. Aguarde o processo de build e deploy ser concluído (pode levar alguns minutos)

### 5. Testar a API

Após o deploy ser concluído, você receberá uma URL (algo como https://businesses-industry-api.onrender.com)

Para testar se a API está funcionando corretamente, acesse:
- `[sua-url]/api/health` - Deve retornar status "ok"
- `[sua-url]/api/industries` - Deve listar todas as indústrias
- `[sua-url]/` - Deve mostrar informações gerais da API

## Solução de Problemas

Se encontrar o erro 502 (Bad Gateway):
1. Verifique se o comando de inicialização está correto: `gunicorn app:app`
2. Confira os logs de build e deploy no painel do Render
3. Certifique-se de que todos os arquivos foram enviados corretamente

## Próximos Passos

Após o deploy bem-sucedido, você pode:
1. Integrar a API com o frontend React
2. Adicionar um banco de dados real (MongoDB, PostgreSQL)
3. Implementar autenticação e autorização
4. Expandir os endpoints conforme necessário
