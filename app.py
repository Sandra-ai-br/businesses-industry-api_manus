from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Habilita CORS para permitir requisições do frontend

# Dados simulados para demonstração - serão substituídos por banco de dados posteriormente
mock_industries = [
    {
        "id": "1",
        "name": "Metalúrgica Global S.A.",
        "sector": "Manufatura",
        "country": "Brasil",
        "state": "São Paulo",
        "city": "São Paulo",
        "description": "Fabricante de componentes metálicos para indústria automotiva",
        "products": [
            "Componentes de transmissão automotiva",
            "Peças de suspensão de alta resistência",
            "Sistemas de freio para veículos pesados",
            "Componentes estruturais de chassis"
        ],
        "certifications": ["ISO 9001", "ISO 14001", "IATF 16949"],
        "export_markets": ["Argentina", "Chile", "México", "Estados Unidos", "Alemanha"],
        "contact_person": "Carlos Silva",
        "position": "Diretor de Exportação",
        "email": "carlos.silva@metalurgicaglobal.com.br",
        "phone": "+55 11 3456-7890",
        "website": "https://www.metalurgicaglobal.com.br",
        "status": "available",
        "location": {"lat": -23.5505, "lng": -46.6333}
    },
    {
        "id": "2",
        "name": "TechSolutions Inc.",
        "sector": "Tecnologia",
        "country": "Estados Unidos",
        "state": "Califórnia",
        "city": "San Francisco",
        "description": "Desenvolvimento de soluções de automação industrial",
        "products": [
            "Sistemas de automação industrial",
            "Software de gestão de produção",
            "Sensores inteligentes",
            "Soluções IoT para indústria"
        ],
        "certifications": ["ISO 9001", "ISO 27001"],
        "export_markets": ["Brasil", "México", "Canadá", "Alemanha", "Japão"],
        "contact_person": "John Smith",
        "position": "International Business Manager",
        "email": "john.smith@techsolutions.com",
        "phone": "+1 415-555-7890",
        "website": "https://www.techsolutions.com",
        "status": "seeking",
        "location": {"lat": 37.7749, "lng": -122.4194}
    },
    {
        "id": "3",
        "name": "AgroVerde Ltda.",
        "sector": "Agronegócio",
        "country": "Brasil",
        "state": "Mato Grosso",
        "city": "Cuiabá",
        "description": "Produção de insumos agrícolas sustentáveis",
        "products": [
            "Fertilizantes orgânicos",
            "Defensivos biológicos",
            "Sementes certificadas",
            "Sistemas de irrigação eficiente"
        ],
        "certifications": ["ISO 14001", "Certificação Orgânica", "Rainforest Alliance"],
        "export_markets": ["Argentina", "Paraguai", "Uruguai", "Chile"],
        "contact_person": "Ana Oliveira",
        "position": "Gerente Comercial",
        "email": "ana.oliveira@agroverde.com.br",
        "phone": "+55 65 3333-4444",
        "website": "https://www.agroverde.com.br",
        "status": "available",
        "location": {"lat": -15.6014, "lng": -56.0979}
    },
    {
        "id": "4",
        "name": "Química Industrial GmbH",
        "sector": "Químico",
        "country": "Alemanha",
        "state": "Baviera",
        "city": "Munique",
        "description": "Produção de compostos químicos para diversos setores",
        "products": [
            "Solventes industriais",
            "Aditivos para plásticos",
            "Catalisadores",
            "Produtos para tratamento de água"
        ],
        "certifications": ["ISO 9001", "ISO 14001", "REACH"],
        "export_markets": ["França", "Itália", "Espanha", "Brasil", "China"],
        "contact_person": "Klaus Weber",
        "position": "Export Director",
        "email": "klaus.weber@qiGmbH.de",
        "phone": "+49 89 1234-5678",
        "website": "https://www.qi-gmbh.de",
        "status": "seeking",
        "location": {"lat": 48.1351, "lng": 11.5820}
    },
    {
        "id": "5",
        "name": "Têxtil Moderna S.A.",
        "sector": "Têxtil",
        "country": "Portugal",
        "state": "Porto",
        "city": "Vila Nova de Gaia",
        "description": "Fabricação de tecidos técnicos de alta performance",
        "products": [
            "Tecidos impermeáveis",
            "Materiais têxteis para automóveis",
            "Tecidos anti-chama",
            "Tecidos técnicos para esportes"
        ],
        "certifications": ["ISO 9001", "OEKO-TEX Standard 100"],
        "export_markets": ["Espanha", "França", "Brasil", "Marrocos", "Angola"],
        "contact_person": "Manuel Ferreira",
        "position": "Diretor de Exportação",
        "email": "manuel.ferreira@textilmoderna.pt",
        "phone": "+351 22 123-4567",
        "website": "https://www.textilmoderna.pt",
        "status": "available",
        "location": {"lat": 41.1333, "lng": -8.6167}
    },
    {
        "id": "6",
        "name": "Mineração Sustentável Ltda.",
        "sector": "Mineração",
        "country": "Brasil",
        "state": "Minas Gerais",
        "city": "Belo Horizonte",
        "description": "Extração de minérios com práticas sustentáveis",
        "products": [
            "Minério de ferro",
            "Bauxita",
            "Manganês",
            "Serviços de recuperação ambiental"
        ],
        "certifications": ["ISO 14001", "ISO 45001", "Certificação Verde"],
        "export_markets": ["China", "Japão", "Coreia do Sul", "Alemanha"],
        "contact_person": "Roberto Campos",
        "position": "Diretor Comercial",
        "email": "roberto.campos@mineracaosustentavel.com.br",
        "phone": "+55 31 9876-5432",
        "website": "https://www.mineracaosustentavel.com.br",
        "status": "seeking",
        "location": {"lat": -19.9167, "lng": -43.9345}
    }
]

@app.route('/api/health', methods=['GET'])
def health_check():
    """Endpoint para verificar se a API está funcionando"""
    return jsonify({
        "status": "online",
        "message": "API do Businesses of the Industry está funcionando corretamente"
    })

@app.route('/api/industries', methods=['GET'])
def get_industries():
    """Endpoint para listar todas as indústrias com filtros opcionais"""
    # Parâmetros de filtro
    sector = request.args.get('sector')
    country = request.args.get('country')
    status = request.args.get('status')
    
    # Aplicar filtros se fornecidos
    filtered_industries = mock_industries
    
    if sector:
        filtered_industries = [i for i in filtered_industries if i['sector'].lower() == sector.lower()]
    
    if country:
        filtered_industries = [i for i in filtered_industries if i['country'].lower() == country.lower()]
    
    if status:
        filtered_industries = [i for i in filtered_industries if i['status'].lower() == status.lower()]
    
    # Retornar resultados filtrados
    return jsonify({
        "count": len(filtered_industries),
        "results": filtered_industries
    })

@app.route('/api/industries/<industry_id>', methods=['GET'])
def get_industry_details(industry_id):
    """Endpoint para obter detalhes de uma indústria específica"""
    industry = next((i for i in mock_industries if i['id'] == industry_id), None)
    
    if industry:
        return jsonify(industry)
    else:
        return jsonify({"error": "Indústria não encontrada"}), 404

@app.route('/api/industries/search', methods=['GET'])
def search_industries():
    """Endpoint para busca avançada de indústrias"""
    # Parâmetros de busca
    query = request.args.get('q', '').lower()
    sector = request.args.get('sector')
    region = request.args.get('region')
    
    # Aplicar busca e filtros
    results = mock_industries
    
    if query:
        results = [i for i in results if 
                  query in i['name'].lower() or 
                  query in i['description'].lower() or
                  any(query in product.lower() for product in i['products'])]
    
    if sector and sector != 'Todos os setores':
        results = [i for i in results if i['sector'].lower() == sector.lower()]
    
    if region and region != 'Global':
        # Simplificação para demonstração - em um cenário real, teríamos um mapeamento de regiões para países
        if region == 'América do Sul':
            countries = ['Brasil', 'Argentina', 'Chile', 'Paraguai', 'Uruguai', 'Colômbia', 'Peru']
            results = [i for i in results if i['country'] in countries]
        elif region == 'Europa':
            countries = ['Alemanha', 'Portugal', 'França', 'Espanha', 'Itália']
            results = [i for i in results if i['country'] in countries]
        elif region == 'América do Norte':
            countries = ['Estados Unidos', 'Canadá', 'México']
            results = [i for i in results if i['country'] in countries]
    
    return jsonify({
        "count": len(results),
        "results": results
    })

@app.route('/api/sectors', methods=['GET'])
def get_sectors():
    """Endpoint para listar todos os setores disponíveis"""
    sectors = sorted(list(set(i['sector'] for i in mock_industries)))
    return jsonify(sectors)

@app.route('/api/countries', methods=['GET'])
def get_countries():
    """Endpoint para listar todos os países disponíveis"""
    countries = sorted(list(set(i['country'] for i in mock_industries)))
    return jsonify(countries)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
