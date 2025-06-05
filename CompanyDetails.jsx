import React, { useState, useEffect } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import API from './api';

const CompanyDetails = () => {
  const { id } = useParams();
  const navigate = useNavigate();
  const [company, setCompany] = useState(null);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchCompanyDetails = async () => {
      if (!id) {
        setError('ID da empresa não fornecido');
        setIsLoading(false);
        return;
      }

      setIsLoading(true);
      setError(null);
      
      try {
        const companyData = await API.getIndustryDetails(id);
        setCompany(companyData);
      } catch (err) {
        console.error('Erro ao carregar detalhes da empresa:', err);
        setError('Não foi possível carregar os detalhes desta empresa. Por favor, tente novamente.');
      } finally {
        setIsLoading(false);
      }
    };
    
    fetchCompanyDetails();
  }, [id]);

  const handleBackClick = () => {
    navigate(-1);
  };

  const handleWebsiteClick = () => {
    if (company?.website) {
      window.open(company.website, '_blank');
    }
  };

  if (isLoading) {
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
          <div className="text-center py-12">
            <p className="text-neutral-dark">Carregando detalhes da empresa...</p>
          </div>
        </main>
      </div>
    );
  }

  if (error || !company) {
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
          <div className="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded mb-6">
            <p>{error || 'Empresa não encontrada'}</p>
          </div>
          <button 
            onClick={handleBackClick} 
            className="text-primary-light hover:text-primary"
          >
            Voltar à Lista
          </button>
        </main>
      </div>
    );
  }

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
          <h2 className="text-2xl font-bold text-primary">Detalhes da Empresa</h2>
          <button 
            onClick={handleBackClick} 
            className="text-primary-light hover:text-primary"
          >
            Voltar à Lista
          </button>
        </div>
        
        <div className="bg-white rounded-lg shadow-md overflow-hidden mb-8">
          {/* Cabeçalho da empresa */}
          <div className="bg-primary p-6 text-white">
            <div className="flex flex-col md:flex-row md:items-center md:justify-between">
              <div>
                <h1 className="text-2xl font-bold mb-2">{company.name}</h1>
                <div className="flex items-center space-x-4">
                  <span>{company.sector}</span>
                  <span>•</span>
                  <span>{company.address || `${company.country}, ${company.region}`}</span>
                </div>
              </div>
              <div className={`mt-4 md:mt-0 inline-block px-4 py-2 rounded-full text-sm font-medium ${
                company.status.toLowerCase() === 'ativo' ? 'bg-success' : 'bg-warning'
              }`}>
                {company.status.toLowerCase() === 'ativo' ? 'Disponível para Exportação' : 'Buscando Parceiros'}
              </div>
            </div>
          </div>
          
          {/* Conteúdo principal */}
          <div className="p-6">
            <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
              {/* Coluna 1: Informações gerais */}
              <div className="md:col-span-2">
                <section className="mb-8">
                  <h3 className="text-xl font-semibold text-primary mb-4">Sobre a Empresa</h3>
                  <p className="text-neutral-dark mb-4">{company.description}</p>
                  <div className="grid grid-cols-2 gap-4">
                    <div>
                      <p className="text-sm text-neutral-dark">Fundação</p>
                      <p className="font-medium">{company.founded}</p>
                    </div>
                    <div>
                      <p className="text-sm text-neutral-dark">Funcionários</p>
                      <p className="font-medium">{company.employees}</p>
                    </div>
                  </div>
                </section>
                
                <section className="mb-8">
                  <h3 className="text-xl font-semibold text-primary mb-4">Produtos e Serviços</h3>
                  <ul className="list-disc pl-5 text-neutral-dark">
                    {company.products.map((product, index) => (
                      <li key={index} className="mb-1">{product}</li>
                    ))}
                  </ul>
                </section>
                
                <section className="mb-8">
                  <h3 className="text-xl font-semibold text-primary mb-4">Certificações</h3>
                  <div className="flex flex-wrap gap-2">
                    {company.certifications.map((cert, index) => (
                      <span key={index} className="bg-neutral-light px-3 py-1 rounded-full text-sm">{cert}</span>
                    ))}
                  </div>
                </section>
                
                <section className="mb-8">
                  <h3 className="text-xl font-semibold text-primary mb-4">Localização</h3>
                  <div className="h-64 bg-neutral-light rounded-lg overflow-hidden flex items-center justify-center">
                    <p>{company.country}, {company.region}</p>
                  </div>
                </section>
              </div>
              
              {/* Coluna 2: Informações de contato */}
              <div>
                <div className="bg-neutral-light p-6 rounded-lg">
                  <h3 className="text-xl font-semibold text-primary mb-4">Informações de Contato</h3>
                  
                  <div className="space-y-4">
                    <div>
                      <p className="text-sm text-neutral-dark">Email</p>
                      <a href={`mailto:${company.contact_email}`} className="text-primary-light hover:text-primary font-medium">
                        {company.contact_email}
                      </a>
                    </div>
                    
                    <div>
                      <p className="text-sm text-neutral-dark">Website</p>
                      <a 
                        href="#" 
                        onClick={handleWebsiteClick}
                        className="text-primary-light hover:text-primary font-medium"
                      >
                        {company.website.replace('https://', '')}
                      </a>
                    </div>
                    
                    <div>
                      <p className="text-sm text-neutral-dark">Endereço</p>
                      <p className="font-medium">{company.address || `${company.country}, ${company.region}`}</p>
                    </div>
                  </div>
                  
                  <div className="mt-6">
                    <button 
                      className="w-full bg-primary hover:bg-primary-light text-white font-bold py-3 px-4 rounded-md transition-colors"
                      onClick={() => window.location.href = `mailto:${company.contact_email}?subject=Contato via Businesses of the Industry - ${company.name}`}
                    >
                      Conectar com esta Empresa
                    </button>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </main>
    </div>
  );
};

export default CompanyDetails;
