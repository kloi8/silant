// const api = axios.create({
//     baseURL: 'http://localhost:8000/api/',  // указываем сервер
//   });
  

  
//   api.interceptors.request.use(
//     (config) => {
//       const token = localStorage.getItem('token');  // Получаем токен
//       if (token) {
//         config.headers.Authorization = `Token ${token}`;  // Добавляем токен в заголовок
//       }
//       return config;
//     },
//     (error) => Promise.reject(error)
//   );
  
//   export default api;


import axios from 'axios';

const API_URL = 'http://localhost:8000/api/';

const api = axios.create({
  baseURL: API_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

api.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem('token');  // Получаем токен из localStorage
    if (token) {
      config.headers.Authorization = `Token ${token}`;  // Добавляем токен в заголовок
    }
    return config;
  },
  (error) => Promise.reject(error)
);

export const getMachines = () => api.get('main/');
export const getMaintenances = () => api.get('maintenances/');
export const getReclamations = () => api.get('reclamations/');
export const addMachineAPI = (machineData) => api.post('machines/', machineData);
export const addMaintenanceAPI = (maintenanceData) => api.post('maintenances/', maintenanceData);
export const addReclamationAPI = (reclamationData) => api.post('reclamations/', reclamationData);
export const getMachineDetails = (machineId) => api.get(`machines/${machineId}/`);
export const getEngineDetails = (engineId) => api.get(`engine-models/${engineId}/`);
export const getEquipmentModelDetails = (equipmentModelId) => api.get(`equipment-models/${equipmentModelId}/`);
export const getTransmissionModelDetails = (transmissionModelId) => api.get(`transmission-models/${transmissionModelId}/`);
export const getDriveBridgeModelDetails = (driveBridgeModelId) => api.get(`drive-bridge-models/${driveBridgeModelId}/`);
export const getControlledBridgeModelDetails = (controlledBridgeModelId) => api.get(`controlled-bridge-models/${controlledBridgeModelId}/`);
export const getMaintenanceTypeDetails = (maintenanceTypeId) => api.get(`maintenance-types/${maintenanceTypeId}/`);
export const getRefusalPointDetails = (refusalPointId) => api.get(`refusal-points/${refusalPointId}/`);
export const getRecoveryMethodDetails = (recoveryMethodId) => api.get(`recovery-methods/${recoveryMethodId}/`);

export default api;