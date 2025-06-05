import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import API, { Industry } from './api';

const ResultsPage = () => {
  const navigate = useNavigate();
  const [activeFilter, setActiveFilter] = useState('all');
  const [industries, setIndustries] = useState([]);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState(null);
  const [searchQuery, setSearchQuery] = useState(null);

  // Carregar resultados da busca ao iniciar o componente
  useEffect(() => {
    const loadSearchResults = async () => {
      setIsLoading(true);
      setError(null);
      
      try {
        // Tentar carregar resultados do sessionStorage primeiro
        const storedResults = sessionStorage.getItem('searchResults');
        const storedQuery = sessionStorage.getItem('searchQuery');
        
        if (storedResults && storedQuery) {
          setIndustries(JSON.parse(storedResults));
          setSearchQuery(JSON.parse(storedQuery));
          setIsLoading(false);
          return;
        }
        
        // Se não houver resultados armazenados, buscar todas as indústrias
        const results = await API.getIndustries();
        setIndustries(results);
      } catch (err) {
        console.error('Erro ao carregar resultados:', err);
        setError('Não foi possível carregar os resultados. Por favor, tente novamente.');
      } finally {
        setIsLoading(false);
      }
    };
    
    loadSearchResults();
  }, []);

  // Filtrar indústrias com base no filtro ativo
  const filteredIndustries = activeFilter === 'all' 
    ? industries 
    : industries.filter(industry => industry.status.toLowerCase() === activeFilter);

  const handleCompanyClick = (companyId) => {
    navigate(`/company/${companyId}`);
  };

  return (
    <div className="min-h-screen bg-neutral-light">
      <div className="bg-primary text-white p-4">
        <div className="container mx-auto flex justify-between items-center">
          <h1 className="text-xl font-bold">Businesses of the Industry</h1>
          <nav>
            <ul className="flex space-x-4">
              <li><a href="/" className="hover:text-neutral-light">Início</a></li>
              <li><a href="/results" className="hover:text-neutral-light">Buscar</a></li>
            </ul>
          </nav>
        </div>
      </div>
      
      <main className="container mx-auto px-4 py-8">
        <div className="flex justify-between items-center mb-6">
          <h2 className="text-2xl font-bold text-primary">Resultados da Busca</h2>
          <button 
            onClick={() => navigate('/')} 
            className="text-primary-light hover:text-primary"
          >
            Voltar à Busca
          </button>
        </div>
        
        {searchQuery && (
          <div className="bg-neutral-light p-4 rounded-lg mb-6">
            <h3 className="font-medium mb-2">Filtros aplicados:</h3>
            <div className="flex flex-wrap gap-2">
              {searchQuery.query && (
                <span className="bg-primary-light text-white px-3 py-1 rounded-full text-sm">
                  Termo: {searchQuery.query}
                </span>
              )}
              {searchQuery.sector && (
                <span className="bg-primary-light text-white px-3 py-1 rounded-full text-sm">
                  Setor: {searchQuery.sector}
                </span>
              )}
              {searchQuery.region && searchQuery.region !== 'Global' && (
                <span className="bg-primary-light text-white px-3 py-1 rounded-full text-sm">
                  Região: {searchQuery.region}
                </span>
              )}
            </div>
          </div>
        )}
        
        {error && (
          <div className="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded mb-6">
            <p>{error}</p>
          </div>
        )}
        
        <div className="bg-white rounded-lg shadow-md p-6 mb-8">
          <div className="flex flex-wrap gap-4 mb-6">
            <button 
              className={`px-4 py-2 rounded-full ${activeFilter === 'all' ? 'bg-primary text-white' : 'bg-neutral-light text-neutral-dark'}`}
              onClick={() => setActiveFilter('all')}
            >
              Todas
            </button>
            <button 
              className={`px-4 py-2 rounded-full ${activeFilter === 'ativo' ? 'bg-success text-white' : 'bg-neutral-light text-neutral-dark'}`}
              onClick={() => setActiveFilter('ativo')}
            >
              Disponíveis para Exportação
            </button>
            <button 
              className={`px-4 py-2 rounded-full ${activeFilter === 'seeking' ? 'bg-warning text-white' : 'bg-neutral-light text-neutral-dark'}`}
              onClick={() => setActiveFilter('seeking')}
            >
              Buscando Parceiros
            </button>
          </div>
          
          {isLoading ? (
            <div className="text-center py-8">
              <p className="text-neutral-dark">Carregando resultados...</p>
            </div>
          ) : (
            <div className="overflow-x-auto">
              <div className="inline-flex space-x-4 pb-4 min-w-full">
                {filteredIndustries.map(company => (
                  <div 
                    key={company.id}
                    className="w-80 flex-shrink-0 border border-neutral-light rounded-lg overflow-hidden cursor-pointer hover:shadow-lg transition-shadow"
                    onClick={() => handleCompanyClick(company.id)}
                  >
                    <div className="bg-primary-light text-white p-3">
                      <h3 className="font-semibold truncate">{company.name}</h3>
                    </div>
                    <div className="p-4">
                      <div className="flex justify-between mb-2">
                        <span className="text-sm text-neutral-dark">{company.sector}</span>
                        <span className="text-sm font-medium">{company.country}</span>
                      </div>
                      <p className="text-neutral-dark mb-3 text-sm h-12 overflow-hidden">{company.description}</p>
                      <div className={`inline-block px-3 py-1 rounded-full text-xs font-medium ${
                        company.status.toLowerCase() === 'ativo' ? 'bg-success text-white' : 'bg-warning text-white'
                      }`}>
                        {company.status.toLowerCase() === 'ativo' ? 'Disponível para Exportação' : 'Buscando Parceiros'}
                      </div>
                    </div>
                  </div>
                ))}
              </div>
            </div>
          )}
          
          {!isLoading && filteredIndustries.length === 0 && (
            <div className="text-center py-8">
              <p className="text-neutral-dark">Nenhuma empresa encontrada com os filtros atuais.</p>
            </div>
          )}
        </div>
      </main>
    </div>
  );
};

export default ResultsPage;
