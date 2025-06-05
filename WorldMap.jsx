import React from 'react';

const WorldMap = ({ onRegionSelect, isLoading }) => {
  const regions = [
    'Global',
    'América do Sul',
    'América do Norte',
    'Europa',
    'Ásia',
    'África',
    'Oceania'
  ];

  return (
    <div className="bg-white rounded-lg shadow-md p-6 h-64 flex flex-col justify-center items-center">
      <p className="text-center mb-4">Selecione uma região para explorar indústrias:</p>
      <div className="grid grid-cols-2 md:grid-cols-3 gap-3 w-full">
        {regions.map((region) => (
          <button
            key={region}
            onClick={() => onRegionSelect(region)}
            disabled={isLoading}
            className={`px-3 py-2 rounded text-center ${
              region === 'Global' 
                ? 'bg-primary text-white' 
                : 'bg-neutral-light hover:bg-primary-light hover:text-white'
            }`}
          >
            {region}
          </button>
        ))}
      </div>
    </div>
  );
};

export default WorldMap;
