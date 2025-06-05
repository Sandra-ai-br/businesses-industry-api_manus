import React from 'react';

const MapLocation = ({ country, region, name }) => {
  return (
    <div className="h-full w-full flex items-center justify-center bg-neutral-light">
      <div className="text-center">
        <p className="font-medium text-primary mb-2">{name}</p>
        <p className="text-neutral-dark">
          {country}, {region}
        </p>
        <p className="text-sm text-neutral-dark mt-2">
          (Visualização de mapa simplificada)
        </p>
      </div>
    </div>
  );
};

export default MapLocation;
