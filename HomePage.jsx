import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import API, { Sector, Country } from './api';

const HomePage = () => {
  const navigate = useNavigate();
  const [selectedRegion, setSelectedRegion] = useState('Global');
  const [sectors, setSectors] = useState([]);
  const [countries, setCountries] = useState([]);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);

  // Carregar setores e países ao iniciar o componente
  useEffect(() => {
    const fetchInitialData = async () => {
      setIsLoading(true);
      setError(null);
      try {
        // Verificar se a API está funcionando
        await API.checkApiHealth();
        
        // Carregar setores e países em paralelo
        const [sectorsData, countriesData] = await Promise.all([
          API.getSectors(),
          API.getCountries()
        ]);
        
        setSectors(sectorsData);
        setCountries(countriesData);
      } catch (err) {
        console.error('Erro ao carregar dados iniciais:', err);
        setError('Não foi possível conectar à API. Por favor, tente novamente mais tarde.');
      } finally {
        setIsLoading(false);
      }
    };

    fetchInitialData();
  }, []);

  const handleSearch = async (query, filters) => {
    setIsLoading(true);
    setError(null);
    
    try {
      // Realizar busca na API
      const results = await API.searchIndustries(
        query, 
        filters.sector, 
        filters.region || selectedRegion
      );
      
      // Armazenar resultados no sessionStorage para uso na página de resultados
      sessionStorage.setItem('searchResults', JSON.stringify(results));
      sessionStorage.setItem('searchQuery', JSON.stringify({
        query,
        sector: filters.sector,
        region: filters.region || selectedRegion
      }));
      
      // Navegar para a página de resultados
      navigate('/results');
    } catch (err) {
      console.error('Erro na busca:', err);
      setError('Ocorreu um erro ao realizar a busca. Por favor, tente novamente.');
    } finally {
      setIsLoading(false);
    }
  };

  const handleRegionSelect = (region) => {
    setSelectedRegion(region);
    
    // Filtrar indústrias por região selecionada
    const fetchIndustriesByRegion = async () => {
      setIsLoading(true);
      setError(null);
      
      try {
        // Buscar indústrias da região selecionada
        const results = await API.searchIndustries('', '', region);
        
        // Armazenar resultados no sessionStorage
        sessionStorage.setItem('searchResults', JSON.stringify(results));
        sessionStorage.setItem('searchQuery', JSON.stringify({
          query: '',
          sector: '',
          region: region
        }));
        
        // Navegar para a página de resultados
        navigate('/results');
      } catch (err) {
        console.error('Erro ao buscar por região:', err);
        setError('Ocorreu um erro ao buscar indústrias nesta região. Por favor, tente novamente.');
      } finally {
        setIsLoading(false);
      }
    };
    
    // Se a região não for "Global", buscar indústrias
    if (region !== 'Global') {
      fetchIndustriesByRegion();
    }
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
        <div className="text-center mb-8">
          <h2 className="text-3xl font-bold text-primary mb-2">Conectando Indústrias Globalmente</h2>
          <p className="text-neutral-dark text-lg">Encontre parceiros industriais em qualquer lugar do mundo</p>
        </div>
        
        {error && (
          <div className="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded mb-6">
            <p>{error}</p>
          </div>
        )}
        
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-8 mb-12">
          <div>
            <h3 className="text-xl font-semibold text-primary-light mb-4">Busca Direta</h3>
            <div className="bg-white rounded-lg shadow-md p-6">
              <form onSubmit={(e) => {
                e.preventDefault();
                const query = e.target.query.value;
                const sector = e.target.sector.value;
                const region = e.target.region.value;
                handleSearch(query, { sector, region });
              }}>
                <div className="mb-4">
                  <label htmlFor="search-query" className="block text-neutral-dark mb-2">Palavra-chave</label>
                  <input
                    id="query"
                    name="query"
                    type="text"
                    placeholder="Nome, produto ou descrição"
                    className="w-full px-4 py-2 border border-neutral-light rounded-md focus:outline-none focus:ring-2 focus:ring-primary"
                  />
                </div>
                
                <div className="grid grid-cols-1 md:grid-cols-2 gap-4 mb-6">
                  <div>
                    <label htmlFor="sector" className="block text-neutral-dark mb-2">Setor</label>
                    <select
                      id="sector"
                      name="sector"
                      className="w-full px-4 py-2 border border-neutral-light rounded-md focus:outline-none focus:ring-2 focus:ring-primary"
                    >
                      <option value="">Todos os setores</option>
                      {sectors.map((sector) => (
                        <option key={sector.id} value={sector.name}>{sector.name}</option>
                      ))}
                    </select>
                  </div>
                  
                  <div>
                    <label htmlFor="region" className="block text-neutral-dark mb-2">Região</label>
                    <select
                      id="region"
                      name="region"
                      className="w-full px-4 py-2 border border-neutral-light rounded-md focus:outline-none focus:ring-2 focus:ring-primary"
                    >
                      <option value="Global">Global</option>
                      <option value="América do Sul">América do Sul</option>
                      <option value="América do Norte">América do Norte</option>
                      <option value="Europa">Europa</option>
                      <option value="Ásia">Ásia</option>
                      <option value="África">África</option>
                      <option value="Oceania">Oceania</option>
                    </select>
                  </div>
                </div>
                
                <button
                  type="submit"
                  disabled={isLoading}
                  className={`w-full bg-primary hover:bg-primary-light text-white font-bold py-3 px-4 rounded-md transition-colors ${
                    isLoading ? 'opacity-50 cursor-not-allowed' : ''
                  }`}
                >
                  {isLoading ? 'Buscando...' : 'Buscar Indústrias'}
                </button>
              </form>
            </div>
          </div>
          
          <div>
            <h3 className="text-xl font-semibold text-primary-light mb-4">Navegação Geográfica</h3>
            <div className="bg-white rounded-lg shadow-md p-6 h-64 flex flex-col justify-center items-center">
              <p className="text-center mb-4">Selecione uma região para explorar indústrias:</p>
              <div className="grid grid-cols-2 md:grid-cols-3 gap-3 w-full">
                {['Global', 'América do Sul', 'América do Norte', 'Europa', 'Ásia', 'África', 'Oceania'].map((region) => (
                  <button
                    key={region}
                    onClick={() => handleRegionSelect(region)}
                    disabled={isLoading}
                    className={`px-3 py-2 rounded text-center ${
                      selectedRegion === region 
                        ? 'bg-primary text-white' 
                        : 'bg-neutral-light hover:bg-primary-light hover:text-white'
                    }`}
                  >
                    {region}
                  </button>
                ))}
              </div>
            </div>
          </div>
        </div>
        
        <div className="bg-white rounded-lg shadow-md p-6 mb-8">
          <h3 className="text-xl font-semibold text-primary mb-4">Como Funciona</h3>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
            <div className="text-center p-4">
              <div className="bg-primary-light text-white w-12 h-12 rounded-full flex items-center justify-center mx-auto mb-3">1</div>
              <h4 className="font-medium mb-2">Busque ou Navegue</h4>
              <p className="text-neutral-dark text-sm">Utilize a busca direta ou navegue pelo mapa interativo para encontrar indústrias</p>
            </div>
            <div className="text-center p-4">
              <div className="bg-primary-light text-white w-12 h-12 rounded-full flex items-center justify-center mx-auto mb-3">2</div>
              <h4 className="font-medium mb-2">Explore Detalhes</h4>
              <p className="text-neutral-dark text-sm">Veja informações detalhadas sobre cada indústria e seus produtos</p>
            </div>
            <div className="text-center p-4">
              <div className="bg-primary-light text-white w-12 h-12 rounded-full flex items-center justify-center mx-auto mb-3">3</div>
              <h4 className="font-medium mb-2">Conecte-se</h4>
              <p className="text-neutral-dark text-sm">Estabeleça contato direto com potenciais parceiros comerciais</p>
            </div>
          </div>
        </div>
        
        <div className="text-center">
          <p className="text-neutral-dark mb-2">Businesses of the Industry - Conectando o mundo industrial</p>
          <p className="text-sm text-neutral-dark">Versão Beta - 2025</p>
        </div>
      </main>
    </div>
  );
};

export default HomePage;
