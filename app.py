from flask import Flask, jsonify, request
from flask_cors import CORS
import os
import json
import logging
from datetime import datetime

# Configuração de logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Inicializa a aplicação Flask
app = Flask(__name__)
CORS(app)  # Habilita CORS para todas as rotas

# Dados simulados para a API
MOCK_INDUSTRIES = [
    {
        "id": "ind001",
        "name": "TechGlobal Solutions",
        "description": "Empresa líder em soluções tecnológicas para indústria 4.0",
        "sector": "Tecnologia",
        "country": "Brasil",
        "region": "América do Sul",
        "founded": 2010,
        "employees": 1200,
        "revenue": "$250M",
        "status": "Ativo",
        "website": "https://techglobal.example.com",
        "contact_email": "contact@techglobal.example.com",
        "address": "Av. Paulista, 1000, São Paulo, SP, Brasil",
        "certifications": ["ISO 9001", "ISO 27001"],
        "products": ["Software Industrial", "IoT Solutions", "Cloud Services"]
    },
    {
        "id": "ind002",
        "name": "EcoFarm Industries",
        "description": "Produtora de alimentos orgânicos com práticas sustentáveis",
        "sector": "Agricultura",
        "country": "Argentina",
        "region": "América do Sul",
        "founded": 2005,
        "employees": 850,
        "revenue": "$120M",
        "status": "Ativo",
        "website": "https://ecofarm.example.com",
        "contact_email": "info@ecofarm.example.com",
        "address": "Ruta 9, Km 50, Buenos Aires, Argentina",
        "certifications": ["Organic Certified", "Fair Trade"],
        "products": ["Grãos Orgânicos", "Frutas Frescas", "Vegetais Orgânicos"]
    },
    {
        "id": "ind003",
        "name": "AutoMex Manufacturing",
        "description": "Fabricante de componentes automotivos de alta precisão",
        "sector": "Automotivo",
        "country": "México",
        "region": "América do Norte",
        "founded": 1998,
        "employees": 3200,
        "revenue": "$500M",
        "status": "Ativo",
        "website": "https://automex.example.com",
        "contact_email": "sales@automex.example.com",
        "address": "Carretera Industrial 200, Monterrey, México",
        "certifications": ["ISO/TS 16949", "ISO 14001"],
        "products": ["Sistemas de Freio", "Componentes de Motor", "Sistemas Elétricos"]
    },
    {
        "id": "ind004",
        "name": "Nordic Furniture Design",
        "description": "Fabricante de móveis de design escandinavo",
        "sector": "Mobiliário",
        "country": "Suécia",
        "region": "Europa",
        "founded": 1986,
        "employees": 720,
        "revenue": "$180M",
        "status": "Ativo",
        "website": "https://nordicfurniture.example.com",
        "contact_email": "info@nordicfurniture.example.com",
        "address": "Industrivägen 45, Estocolmo, Suécia",
        "certifications": ["FSC Certified", "ISO 9001"],
        "products": ["Móveis Residenciais", "Móveis de Escritório", "Decoração"]
    },
    {
        "id": "ind005",
        "name": "AfriTex Textiles",
        "description": "Produtora de têxteis tradicionais e modernos",
        "sector": "Têxtil",
        "country": "Gana",
        "region": "África",
        "founded": 2008,
        "employees": 450,
        "revenue": "$75M",
        "status": "Ativo",
        "website": "https://afritex.example.com",
        "contact_email": "contact@afritex.example.com",
        "address": "Industrial Zone, Accra, Gana",
        "certifications": ["Fair Trade", "OEKO-TEX"],
        "products": ["Tecidos Tradicionais", "Roupas", "Acessórios Têxteis"]
    },
    {
        "id": "ind006",
        "name": "AsiaPharma Solutions",
        "description": "Desenvolvedora e fabricante de produtos farmacêuticos",
        "sector": "Farmacêutico",
        "country": "Singapura",
        "region": "Ásia",
        "founded": 2001,
        "employees": 1800,
        "revenue": "$320M",
        "status": "Ativo",
        "website": "https://asiapharma.example.com",
        "contact_email": "info@asiapharma.example.com",
        "address": "Biopolis Drive 30, Singapura",
        "certifications": ["GMP", "ISO 13485"],
        "products": ["Medicamentos Genéricos", "Suplementos Nutricionais", "Equipamentos Médicos"]
    }
]

# Lista de setores disponíveis
SECTORS = [
    {"id": "tech", "name": "Tecnologia"},
    {"id": "agri", "name": "Agricultura"},
    {"id": "auto", "name": "Automotivo"},
    {"id": "furn", "name": "Mobiliário"},
    {"id": "text", "name": "Têxtil"},
    {"id": "pharm", "name": "Farmacêutico"}
]

# Lista de países disponíveis
COUNTRIES = [
    {"id": "br", "name": "Brasil", "region": "América do Sul"},
    {"id": "ar", "name": "Argentina", "region": "América do Sul"},
    {"id": "mx", "name": "México", "region": "América do Norte"},
    {"id": "se", "name": "Suécia", "region": "Europa"},
    {"id": "gh", "name": "Gana", "region": "África"},
    {"id": "sg", "name": "Singapura", "region": "Ásia"}
]

# Rota de verificação de saúde
@app.route('/api/health', methods=['GET'])
def health_check():
    """Endpoint para verificar se a API está funcionando"""
    return jsonify({
        "status": "ok",
        "message": "API Businesses of the Industry está funcionando!"
    })

# Rota para listar todas as indústrias
@app.route('/api/industries', methods=['GET'])
def get_industries():
    """Endpoint para listar todas as indústrias com filtros opcionais"""
    # Obtém parâmetros de consulta
    sector = request.args.get('sector')
    country = request.args.get('country')
    status = request.args.get('status')
    
    # Filtra as indústrias
    filtered_industries = MOCK_INDUSTRIES
    
    if sector:
        filtered_industries = [ind for ind in filtered_industries if ind['sector'] == sector]
    
    if country:
        filtered_industries = [ind for ind in filtered_industries if ind['country'] == country]
    
    if status:
        filtered_industries = [ind for ind in filtered_industries if ind['status'] == status]
    
    return jsonify({
        "status": "success",
        "count": len(filtered_industries),
        "data": filtered_industries
    })

# Rota para obter detalhes de uma indústria específica
@app.route('/api/industries/<id>', methods=['GET'])
def get_industry(id):
    """Endpoint para obter detalhes de uma indústria específica"""
    industry = next((ind for ind in MOCK_INDUSTRIES if ind['id'] == id), None)
    
    if not industry:
        return jsonify({
            "status": "error",
            "message": "Indústria não encontrada"
        }), 404
    
    return jsonify({
        "status": "success",
        "data": industry
    })

# Rota para busca avançada de indústrias
@app.route('/api/industries/search', methods=['GET'])
def search_industries():
    """Endpoint para busca avançada de indústrias"""
    # Obtém parâmetros de consulta
    query = request.args.get('q', '').lower()
    sector = request.args.get('sector')
    region = request.args.get('region')
    
    # Filtra as indústrias
    results = MOCK_INDUSTRIES
    
    if query:
        results = [ind for ind in results if 
                  query in ind['name'].lower() or 
                  query in ind['description'].lower() or
                  any(query in product.lower() for product in ind['products'])]
    
    if sector:
        results = [ind for ind in results if ind['sector'] == sector]
    
    if region:
        results = [ind for ind in results if ind['region'] == region]
    
    return jsonify({
        "status": "success",
        "count": len(results),
        "data": results
    })

# Rota para listar todos os setores
@app.route('/api/sectors', methods=['GET'])
def get_sectors():
    """Endpoint para listar todos os setores disponíveis"""
    return jsonify({
        "status": "success",
        "count": len(SECTORS),
        "data": SECTORS
    })

# Rota para listar todos os países
@app.route('/api/countries', methods=['GET'])
def get_countries():
    """Endpoint para listar todos os países disponíveis"""
    return jsonify({
        "status": "success",
        "count": len(COUNTRIES),
        "data": COUNTRIES
    })

# Rota raiz para informações da API
@app.route('/', methods=['GET'])
def api_info():
    """Endpoint raiz com informações sobre a API"""
    return jsonify({
        "name": "Businesses of the Industry API",
        "version": "1.0.0",
        "description": "API para o projeto Businesses of the Industry",
        "endpoints": [
            "/api/health",
            "/api/industries",
            "/api/industries/<id>",
            "/api/industries/search",
            "/api/sectors",
            "/api/countries"
        ]
    })

# Executa a aplicação se este arquivo for executado diretamente
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
