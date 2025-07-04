# Dados simulados para uso quando o banco de dados não está disponível
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
