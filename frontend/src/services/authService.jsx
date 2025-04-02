import axios from 'axios';

const API_URL = 'http://127.0.0.1:8000/users/token/';

export const login = async (email, password) => {
    const response = await axios.post(API_URL, { email, password });
    //console.log('Response from backend:', response);
    if (response.data.access) {
      localStorage.setItem('accessToken', response.data.access);
      localStorage.setItem('refreshToken', response.data.refresh);
    }
    return response.data;
};

export const logout = () => {
  localStorage.removeItem('accessToken');
  localStorage.removeItem('refreshToken');
};

export const refreshAccessToken = async () => {
  const refreshToken = localStorage.getItem('refreshToken');
  
  if (!refreshToken) {
    console.error("No se encontró el refresh token.");
    return null;
  }

  try {
    const response = await axios.post('http://127.0.0.1:8000/users/token/refresh/', { refresh: refreshToken });
    const newAccessToken = response.data.access;
    
    // Guarda el nuevo access token
    localStorage.setItem('accessToken', newAccessToken);
    return newAccessToken;
  } catch (error) {
    console.error('Error al refrescar el access token', error);
    return null;
  }
};


export const setAuthHeader = () => {
  const accessToken = localStorage.getItem('accessToken');
  if (accessToken) {
    return { Authorization: `Bearer ${accessToken}` };
  }
  return {};
};

export const axiosWithAuth = async (config) => {
  let accessToken = localStorage.getItem('accessToken');
  
  // Si no hay access token, intentar refrescarlo
  if (!accessToken) {
    accessToken = await refreshAccessToken();
    if (!accessToken) {
      throw new Error("No se pudo obtener un access token.");
    }
  }

  // Agregar el token al encabezado de la solicitud
  config.headers = { ...config.headers, Authorization: `Bearer ${accessToken}` };

  try {
    return await axios(config);
  } catch (error) {
    if (error.response && error.response.status === 401) {
      // Si el error es 401, el token podría haber expirado
      // Intentamos refrescar el access token y volver a hacer la solicitud
      const newAccessToken = await refreshAccessToken();
      if (newAccessToken) {
        config.headers.Authorization = `Bearer ${newAccessToken}`;
        return await axios(config); // Reintentar la solicitud con el nuevo token
      }
    }
    throw error; // Si no hay solución, lanzamos el error original
  }
};


//To do
//crear un metodo que jale informacion del usuario para fines de react
