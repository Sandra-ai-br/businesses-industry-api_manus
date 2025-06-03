from datetime import datetime
from bson import ObjectId
from database import db, COLLECTIONS

class IndustryModel:
    """Modelo para operações com indústrias no banco de dados"""
    
    @staticmethod
    def get_all(filters=None, limit=100, skip=0):
        """
        Recupera todas as indústrias com filtros opcionais
        
        Args:
            filters (dict): Filtros a serem aplicados
            limit (int): Número máximo de resultados
            skip (int): Número de resultados para pular (paginação)
            
        Returns:
            list: Lista de indústrias
        """
        collection = db.get_collection(COLLECTIONS['industries'])
        query = filters if filters else {}
        
        if collection:
            cursor = collection.find(query).limit(limit).skip(skip)
            return list(cursor)
        else:
            # Fallback para dados simulados quando não há conexão com o banco
            from mock_data import mock_industries
            return mock_industries
    
    @staticmethod
    def get_by_id(industry_id):
        """
        Recupera uma indústria pelo ID
        
        Args:
            industry_id (str): ID da indústria
            
        Returns:
            dict: Dados da indústria ou None se não encontrada
        """
        collection = db.get_collection(COLLECTIONS['industries'])
        
        if collection:
            try:
                return collection.find_one({"_id": ObjectId(industry_id)})
            except:
                return None
        else:
            # Fallback para dados simulados
            from mock_data import mock_industries
            return next((i for i in mock_industries if i["id"] == industry_id), None)
    
    @staticmethod
    def search(query=None, sector=None, region=None, limit=100, skip=0):
        """
        Busca indústrias com base em texto, setor e/ou região
        
        Args:
            query (str): Texto para busca
            sector (str): Setor para filtrar
            region (str): Região para filtrar
            limit (int): Número máximo de resultados
            skip (int): Número de resultados para pular (paginação)
            
        Returns:
            list: Lista de indústrias que correspondem aos critérios
        """
        collection = db.get_collection(COLLECTIONS['industries'])
        search_query = {}
        
        # Adiciona filtro de texto se fornecido
        if query:
            search_query["$or"] = [
                {"name": {"$regex": query, "$options": "i"}},
                {"description": {"$regex": query, "$options": "i"}},
                {"products": {"$elemMatch": {"$regex": query, "$options": "i"}}}
            ]
        
        # Adiciona filtro de setor se fornecido
        if sector and sector != "Todos os setores":
            search_query["sector"] = sector
        
        # Adiciona filtro de região se fornecido
        if region and region != "Global":
            # Mapeamento simplificado de regiões para países
            region_countries = {
                "América do Sul": ["Brasil", "Argentina", "Chile", "Paraguai", "Uruguai", "Colômbia", "Peru"],
                "Europa": ["Alemanha", "Portugal", "França", "Espanha", "Itália"],
                "América do Norte": ["Estados Unidos", "Canadá", "México"],
                "Ásia": ["Japão", "China", "Índia", "Coreia do Sul"],
                "África": ["África do Sul", "Egito", "Nigéria"],
                "Oceania": ["Austrália", "Nova Zelândia"]
            }
            
            if region in region_countries:
                search_query["location.country"] = {"$in": region_countries[region]}
        
        if collection:
            cursor = collection.find(search_query).limit(limit).skip(skip)
            return list(cursor)
        else:
            # Fallback para dados simulados
            from mock_data import mock_industries
            
            # Filtragem manual para dados simulados
            results = mock_industries
            
            if query:
                query = query.lower()
                results = [i for i in results if 
                          query in i['name'].lower() or 
                          query in i['description'].lower() or
                          any(query in product.lower() for product in i['products'])]
            
            if sector and sector != "Todos os setores":
                results = [i for i in results if i['sector'] == sector]
            
            if region and region != "Global":
                if region == "América do Sul":
                    countries = ["Brasil", "Argentina", "Chile", "Paraguai", "Uruguai", "Colômbia", "Peru"]
                    results = [i for i in results if i['country'] in countries]
                elif region == "Europa":
                    countries = ["Alemanha", "Portugal", "França", "Espanha", "Itália"]
                    results = [i for i in results if i['country'] in countries]
                elif region == "América do Norte":
                    countries = ["Estados Unidos", "Canadá", "México"]
                    results = [i for i in results if i['country'] in countries]
            
            return results
    
    @staticmethod
    def create(industry_data):
        """
        Cria uma nova indústria no banco de dados
        
        Args:
            industry_data (dict): Dados da indústria
            
        Returns:
            dict: Indústria criada com ID
        """
        collection = db.get_collection(COLLECTIONS['industries'])
        
        # Adiciona timestamps
        industry_data["metadata"] = {
            "created_at": datetime.utcnow(),
            "updated_at": datetime.utcnow(),
            "verified": False
        }
        
        if collection:
            result = collection.insert_one(industry_data)
            industry_data["_id"] = result.inserted_id
            return industry_data
        else:
            return None
    
    @staticmethod
    def update(industry_id, industry_data):
        """
        Atualiza uma indústria existente
        
        Args:
            industry_id (str): ID da indústria
            industry_data (dict): Novos dados da indústria
            
        Returns:
            bool: True se atualizado com sucesso, False caso contrário
        """
        collection = db.get_collection(COLLECTIONS['industries'])
        
        # Atualiza timestamp
        industry_data["metadata.updated_at"] = datetime.utcnow()
        
        if collection:
            try:
                result = collection.update_one(
                    {"_id": ObjectId(industry_id)},
                    {"$set": industry_data}
                )
                return result.modified_count > 0
            except:
                return False
        else:
            return False
    
    @staticmethod
    def delete(industry_id):
        """
        Remove uma indústria do banco de dados
        
        Args:
            industry_id (str): ID da indústria
            
        Returns:
            bool: True se removido com sucesso, False caso contrário
        """
        collection = db.get_collection(COLLECTIONS['industries'])
        
        if collection:
            try:
                result = collection.delete_one({"_id": ObjectId(industry_id)})
                return result.deleted_count > 0
            except:
                return False
        else:
            return False


class SectorModel:
    """Modelo para operações com setores no banco de dados"""
    
    @staticmethod
    def get_all():
        """
        Recupera todos os setores
        
        Returns:
            list: Lista de setores
        """
        collection = db.get_collection(COLLECTIONS['sectors'])
        
        if collection:
            return list(collection.find())
        else:
            # Fallback para dados simulados
            from mock_data import mock_industries
            sectors = sorted(list(set(i['sector'] for i in mock_industries)))
            return [{"name": sector} for sector in sectors]
    
    @staticmethod
    def get_by_name(name):
        """
        Recupera um setor pelo nome
        
        Args:
            name (str): Nome do setor
            
        Returns:
            dict: Dados do setor ou None se não encontrado
        """
        collection = db.get_collection(COLLECTIONS['sectors'])
        
        if collection:
            return collection.find_one({"name": name})
        else:
            # Fallback para dados simulados
            from mock_data import mock_industries
            if name in [i['sector'] for i in mock_industries]:
                return {"name": name}
            return None


class CountryModel:
    """Modelo para operações com países no banco de dados"""
    
    @staticmethod
    def get_all():
        """
        Recupera todos os países
        
        Returns:
            list: Lista de países
        """
        collection = db.get_collection(COLLECTIONS['countries'])
        
        if collection:
            return list(collection.find())
        else:
            # Fallback para dados simulados
            from mock_data import mock_industries
            countries = sorted(list(set(i['country'] for i in mock_industries)))
            return [{"name": country} for country in countries]
    
    @staticmethod
    def get_by_name(name):
        """
        Recupera um país pelo nome
        
        Args:
            name (str): Nome do país
            
        Returns:
            dict: Dados do país ou None se não encontrado
        """
        collection = db.get_collection(COLLECTIONS['countries'])
        
        if collection:
            return collection.find_one({"name": name})
        else:
            # Fallback para dados simulados
            from mock_data import mock_industries
            if name in [i['country'] for i in mock_industries]:
                return {"name": name}
            return None
