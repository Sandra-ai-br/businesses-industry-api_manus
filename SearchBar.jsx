import React, { useState } from 'react';

const SearchBar = ({ onSearch, sectors = [], isLoading = false }) => {
  const [query, setQuery] = useState('');
  const [selectedSector, setSelectedSector] = useState('');
  const [selectedRegion, setSelectedRegion] = useState('Global');
  
  const regions = [
    'Global',
    'América do Sul',
    'América do Norte',
    'Europa',
    'Ásia',
    'África',
    'Oceania'
  ];

  const handleSubmit = (e) => {
    e.preventDefault();
    onSearch(query, {
      sector: selectedSector,
      region: selectedRegion
    });
  };

  return (
    <form onSubmit={handleSubmit} className="bg-white rounded-lg shadow-md p-6">
      <div className="mb-4">
        <label htmlFor="search-query" className="block text-neutral-dark mb-2">Palavra-chave</label>
        <input
          id="search-query"
          type="text"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          placeholder="Nome, produto ou descrição"
          className="w-full px-4 py-2 border border-neutral-light rounded-md focus:outline-none focus:ring-2 focus:ring-primary"
        />
      </div>
      
      <div className="grid grid-cols-1 md:grid-cols-2 gap-4 mb-6">
        <div>
          <label htmlFor="sector-filter" className="block text-neutral-dark mb-2">Setor</label>
          <select
            id="sector-filter"
            value={selectedSector}
            onChange={(e) => setSelectedSector(e.target.value)}
            className="w-full px-4 py-2 border border-neutral-light rounded-md focus:outline-none focus:ring-2 focus:ring-primary"
          >
            <option value="">Todos os setores</option>
            {sectors.map((sector, index) => (
              <option key={index} value={sector}>{sector}</option>
            ))}
          </select>
        </div>
        
        <div>
          <label htmlFor="region-filter" className="block text-neutral-dark mb-2">Região</label>
          <select
            id="region-filter"
            value={selectedRegion}
            onChange={(e) => setSelectedRegion(e.target.value)}
            className="w-full px-4 py-2 border border-neutral-light rounded-md focus:outline-none focus:ring-2 focus:ring-primary"
          >
            {regions.map((region, index) => (
              <option key={index} value={region}>{region}</option>
            ))}
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
  );
};

export default SearchBar;
