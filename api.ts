// API Service para o Businesses of the Industry
// Este serviço centraliza todas as chamadas à API

// URL base da API em produção no Render
const API_BASE_URL = 'https://businesses-industry-api-manus.onrender.com';

// Interfaces para tipagem dos dados
export interface Industry {
  id: string;
  name: string;
  description: string;
  sector: string;
  country: string;
  region: string;
  founded: number;
  employees: number;
  revenue: string;
  status: string;
  website: string;
  contact_email: string;
  address: string;
  certifications: string[];
  products: string[];
}

export interface Sector {
  id: string;
  name: string;
}

export interface Country {
  id: string;
  name: string;
  region: string;
}

export interface SearchFilters {
  sector?: string;
  region?: string;
  country?: string;
  status?: string;
}

// Funções de API

// Verificar saúde da API
export const checkApiHealth = async (): Promise<{ status: string; message: string }> => {
  try {
    const response = await fetch(`${API_BASE_URL}/api/health`);
    if (!response.ok) throw new Error('API health check failed');
    return await response.json();
  } catch (error) {
    console.error('API Health Check Error:', error);
    throw error;
  }
};

// Buscar todas as indústrias com filtros opcionais
export const getIndustries = async (filters?: SearchFilters): Promise<Industry[]> => {
  try {
    let url = `${API_BASE_URL}/api/industries`;
    
    // Adicionar filtros à URL se fornecidos
    if (filters) {
      const queryParams = new URLSearchParams();
      if (filters.sector) queryParams.append('sector', filters.sector);
      if (filters.country) queryParams.append('country', filters.country);
      if (filters.status) queryParams.append('status', filters.status);
      
      if (queryParams.toString()) {
        url += `?${queryParams.toString()}`;
      }
    }
    
    const response = await fetch(url);
    if (!response.ok) throw new Error('Failed to fetch industries');
    
    const data = await response.json();
    return data.data;
  } catch (error) {
    console.error('Get Industries Error:', error);
    throw error;
  }
};

// Buscar detalhes de uma indústria específica
export const getIndustryDetails = async (id: string): Promise<Industry> => {
  try {
    const response = await fetch(`${API_BASE_URL}/api/industries/${id}`);
    if (!response.ok) throw new Error(`Failed to fetch industry with ID: ${id}`);
    
    const data = await response.json();
    return data.data;
  } catch (error) {
    console.error('Get Industry Details Error:', error);
    throw error;
  }
};

// Busca avançada de indústrias
export const searchIndustries = async (query: string, sector?: string, region?: string): Promise<Industry[]> => {
  try {
    const queryParams = new URLSearchParams();
    if (query) queryParams.append('q', query);
    if (sector) queryParams.append('sector', sector);
    if (region) queryParams.append('region', region);
    
    const response = await fetch(`${API_BASE_URL}/api/industries/search?${queryParams.toString()}`);
    if (!response.ok) throw new Error('Search failed');
    
    const data = await response.json();
    return data.data;
  } catch (error) {
    console.error('Search Industries Error:', error);
    throw error;
  }
};

// Buscar todos os setores
export const getSectors = async (): Promise<Sector[]> => {
  try {
    const response = await fetch(`${API_BASE_URL}/api/sectors`);
    if (!response.ok) throw new Error('Failed to fetch sectors');
    
    const data = await response.json();
    return data.data;
  } catch (error) {
    console.error('Get Sectors Error:', error);
    throw error;
  }
};

// Buscar todos os países
export const getCountries = async (): Promise<Country[]> => {
  try {
    const response = await fetch(`${API_BASE_URL}/api/countries`);
    if (!response.ok) throw new Error('Failed to fetch countries');
    
    const data = await response.json();
    return data.data;
  } catch (error) {
    console.error('Get Countries Error:', error);
    throw error;
  }
};

// Exportar todas as funções como um objeto API
const API = {
  checkApiHealth,
  getIndustries,
  getIndustryDetails,
  searchIndustries,
  getSectors,
  getCountries
};

export default API;
