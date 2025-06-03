from flask import Flask, jsonify, request
from flask_cors import CORS
from models import IndustryModel, SectorModel, CountryModel
from database import db

app = Flask(__name__)
CORS(app)  # Habilita CORS para permitir requisições do frontend

@app.route('/api/health', methods=['GET'])
def health_check():
    """Endpoint para verificar se a API está funcionando"""
    db_status = "connected" if db.is_connected() else "disconnected"
    return jsonify({
        "status": "online",
        "database": db_status,
        "message": "API do Businesses of the Industry está funcionando corretamente"
    })

@app.route('/api/industries', methods=['GET'])
def get_industries():
    """Endpoint para listar todas as indústrias com filtros opcionais"""
    # Parâmetros de filtro
    sector = request.args.get('sector')
    country = request.args.get('country')
    status = request.args.get('status')
    limit = int(request.args.get('limit', 100))
    skip = int(request.args.get('skip', 0))
    
    # Construir filtros
    filters = {}
    if sector:
        filters["sector"] = sector
    
    if country:
        filters["location.country"] = country
    
    if status:
        filters["status"] = status
    
    # Buscar indústrias usando o modelo
    industries = IndustryModel.get_all(filters, limit, skip)
    
    # Retornar resultados
    return jsonify({
        "count": len(industries),
        "results": industries
    })

@app.route('/api/industries/<industry_id>', methods=['GET'])
def get_industry_details(industry_id):
    """Endpoint para obter detalhes de uma indústria específica"""
    industry = IndustryModel.get_by_id(industry_id)
    
    if industry:
        return jsonify(industry)
    else:
        return jsonify({"error": "Indústria não encontrada"}), 404

@app.route('/api/industries/search', methods=['GET'])
def search_industries():
    """Endpoint para busca avançada de indústrias"""
    # Parâmetros de busca
    query = request.args.get('q', '')
    sector = request.args.get('sector')
    region = request.args.get('region')
    limit = int(request.args.get('limit', 100))
    skip = int(request.args.get('skip', 0))
    
    # Buscar indústrias usando o modelo
    results = IndustryModel.search(query, sector, region, limit, skip)
    
    return jsonify({
        "count": len(results),
        "results": results
    })

@app.route('/api/sectors', methods=['GET'])
def get_sectors():
    """Endpoint para listar todos os setores disponíveis"""
    sectors = SectorModel.get_all()
    # Extrair apenas os nomes dos setores para manter compatibilidade com a API anterior
    sector_names = [sector["name"] for sector in sectors]
    return jsonify(sector_names)

@app.route('/api/countries', methods=['GET'])
def get_countries():
    """Endpoint para listar todos os países disponíveis"""
    countries = CountryModel.get_all()
    # Extrair apenas os nomes dos países para manter compatibilidade com a API anterior
    country_names = [country["name"] for country in countries]
    return jsonify(country_names)

# Novos endpoints para CRUD completo

@app.route('/api/industries', methods=['POST'])
def create_industry():
    """Endpoint para criar uma nova indústria"""
    data = request.json
    
    # Validação básica
    required_fields = ["name", "sector", "description"]
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"Campo obrigatório ausente: {field}"}), 400
    
    # Criar indústria usando o modelo
    result = IndustryModel.create(data)
    
    if result:
        return jsonify(result), 201
    else:
        return jsonify({"error": "Erro ao criar indústria"}), 500

@app.route('/api/industries/<industry_id>', methods=['PUT'])
def update_industry(industry_id):
    """Endpoint para atualizar uma indústria existente"""
    data = request.json
    
    # Verificar se a indústria existe
    existing = IndustryModel.get_by_id(industry_id)
    if not existing:
        return jsonify({"error": "Indústria não encontrada"}), 404
    
    # Atualizar indústria usando o modelo
    success = IndustryModel.update(industry_id, data)
    
    if success:
        updated = IndustryModel.get_by_id(industry_id)
        return jsonify(updated)
    else:
        return jsonify({"error": "Erro ao atualizar indústria"}), 500

@app.route('/api/industries/<industry_id>', methods=['DELETE'])
def delete_industry(industry_id):
    """Endpoint para remover uma indústria"""
    # Verificar se a indústria existe
    existing = IndustryModel.get_by_id(industry_id)
    if not existing:
        return jsonify({"error": "Indústria não encontrada"}), 404
    
    # Remover indústria usando o modelo
    success = IndustryModel.delete(industry_id)
    
    if success:
        return jsonify({"message": "Indústria removida com sucesso"}), 200
    else:
        return jsonify({"error": "Erro ao remover indústria"}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
