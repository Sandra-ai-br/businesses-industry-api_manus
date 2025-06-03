from pymongo import MongoClient
from dotenv import load_dotenv
import os
import logging

# Configuração de logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Carrega variáveis de ambiente
load_dotenv()

class Database:
    """Classe para gerenciar conexão com o MongoDB"""
    
    _instance = None
    
    def __new__(cls):
        """Implementação de Singleton para garantir uma única conexão"""
        if cls._instance is None:
            cls._instance = super(Database, cls).__new__(cls)
            cls._instance._initialize_connection()
        return cls._instance
    
    def _initialize_connection(self):
        """Inicializa a conexão com o MongoDB"""
        try:
            # Obtém a string de conexão das variáveis de ambiente ou usa um valor padrão para desenvolvimento
            mongo_uri = os.getenv('MONGO_URI', 'mongodb://localhost:27017')
            db_name = os.getenv('DB_NAME', 'businesses_industry')
            
            # Cria a conexão com o MongoDB
            self.client = MongoClient(mongo_uri)
            self.db = self.client[db_name]
            
            # Verifica se a conexão está funcionando
            self.client.admin.command('ping')
            logger.info(f"Conectado ao MongoDB: {db_name}")
            
        except Exception as e:
            logger.error(f"Erro ao conectar ao MongoDB: {e}")
            # Em caso de erro, configura para usar dados simulados
            self.client = None
            self.db = None
    
    def get_collection(self, collection_name):
        """Retorna uma coleção específica do banco de dados"""
        if self.db:
            return self.db[collection_name]
        else:
            logger.warning(f"Banco de dados não disponível. Retornando None para coleção {collection_name}")
            return None
    
    def is_connected(self):
        """Verifica se a conexão com o banco de dados está ativa"""
        return self.db is not None
    
    def close_connection(self):
        """Fecha a conexão com o MongoDB"""
        if self.client:
            self.client.close()
            logger.info("Conexão com MongoDB fechada")

# Instância global para uso em toda a aplicação
db = Database()

# Nomes das coleções para fácil referência
COLLECTIONS = {
    'industries': 'industries',
    'sectors': 'sectors',
    'countries': 'countries',
    'connections': 'connections'
}
