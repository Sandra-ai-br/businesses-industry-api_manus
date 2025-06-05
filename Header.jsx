import React from 'react';

const Header = () => {
  return (
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
  );
};

export default Header;
