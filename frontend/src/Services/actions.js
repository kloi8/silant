import {
  getMachines,
  getMaintenances,
  getReclamations,
  addMachineAPI,
  addMaintenanceAPI,
  addReclamationAPI,
  getMachineDetails,
  getEngineDetails,
  getEquipmentModelDetails,
  getTransmissionModelDetails,
  getDriveBridgeModelDetails,
  getControlledBridgeModelDetails,
  getMaintenanceTypeDetails,
  getRefusalPointDetails,
  getRecoveryMethodDetails
} from '../axios';

export const FETCH_MACHINES_SUCCESS = 'FETCH_MACHINES_SUCCESS';
export const FETCH_MAINTENANCES_SUCCESS = 'FETCH_MAINTENANCES_SUCCESS';
export const FETCH_RECLAMATIONS_SUCCESS = 'FETCH_RECLAMATIONS_SUCCESS';
export const ADD_MACHINE_SUCCESS = 'ADD_MACHINE_SUCCESS';
export const ADD_MAINTENANCE_SUCCESS = 'ADD_MAINTENANCE_SUCCESS';
export const ADD_RECLAMATION_SUCCESS = 'ADD_RECLAMATION_SUCCESS';
export const FETCH_MACHINE_DETAILS_SUCCESS = 'FETCH_MACHINE_DETAILS_SUCCESS';
export const FETCH_ENGINE_DETAILS_SUCCESS = 'FETCH_ENGINE_DETAILS_SUCCESS';
export const FETCH_EQUIPMENT_MODEL_DETAILS_SUCCESS = 'FETCH_EQUIPMENT_MODEL_DETAILS_SUCCESS';
export const FETCH_TRANSMISSION_MODEL_DETAILS_SUCCESS = 'FETCH_TRANSMISSION_MODEL_DETAILS_SUCCESS';
export const FETCH_DRIVE_BRIDGE_MODEL_DETAILS_SUCCESS = 'FETCH_DRIVE_BRIDGE_MODEL_DETAILS_SUCCESS';
export const FETCH_CONTROLLED_BRIDGE_MODEL_DETAILS_SUCCESS = 'FETCH_CONTROLLED_BRIDGE_MODEL_DETAILS_SUCCESS';
export const FETCH_MAINTENANCE_TYPE_DETAILS_SUCCESS = 'FETCH_MAINTENANCE_TYPE_DETAILS_SUCCESS';
export const FETCH_REFUSAL_POINT_DETAILS_SUCCESS = 'FETCH_REFUSAL_POINT_DETAILS_SUCCESS';
export const FETCH_RECOVERY_METHOD_DETAILS_SUCCESS = 'FETCH_RECOVERY_METHOD_DETAILS_SUCCESS';

export const fetchMachines = () => async (dispatch) => {
  const response = await getMachines();
  dispatch({ type: FETCH_MACHINES_SUCCESS, payload: response.data });
};

export const fetchMaintenances = () => async (dispatch) => {
  const response = await getMaintenances();
  dispatch({ type: FETCH_MAINTENANCES_SUCCESS, payload: response.data });
};

export const fetchReclamations = () => async (dispatch) => {
  const response = await getReclamations();
  dispatch({ type: FETCH_RECLAMATIONS_SUCCESS, payload: response.data });
};

export const addMachineList = (machineData) => async (dispatch) => {
  const response = addMachineAPI(machineData);
  dispatch({ type: ADD_MACHINE_SUCCESS, payload: response.data });
};

export const addMaintenanceList = (maintenanceData) => async (dispatch) => {
  const response = addMaintenanceAPI(maintenanceData);
  dispatch({ type: ADD_MAINTENANCE_SUCCESS, payload: response.data });
};

export const addReclamationList = (reclamationData) => async (dispatch) => {
  const response = addReclamationAPI(reclamationData);
  dispatch({ type: ADD_RECLAMATION_SUCCESS, payload: response.data });
};

export const fetchMachineDetails = (machineId) => async (dispatch) => {
  const response = await getMachineDetails(machineId);
  dispatch({ type: FETCH_MACHINE_DETAILS_SUCCESS, payload: response.data });
};

export const fetchEngineDetails = (engineId) => async (dispatch) => {
  const response = await getEngineDetails(engineId);
  dispatch({ type: FETCH_ENGINE_DETAILS_SUCCESS, payload: response.data });
};

export const fetchEquipmentModelDetails = (equipmentModelId) => async (dispatch) => {
  const response = await getEquipmentModelDetails(equipmentModelId);
  dispatch({ type: FETCH_EQUIPMENT_MODEL_DETAILS_SUCCESS, payload: response.data });
};

export const fetchTransmissionModelDetails = (transmissionModelId) => async (dispatch) => {
  const response = await getTransmissionModelDetails(transmissionModelId);
  dispatch({ type: FETCH_TRANSMISSION_MODEL_DETAILS_SUCCESS, payload: response.data });
};

export const fetchDriveBridgeModelDetails = (driveBridgeModelId) => async (dispatch) => {
  const response = await getDriveBridgeModelDetails(driveBridgeModelId);
  dispatch({ type: FETCH_DRIVE_BRIDGE_MODEL_DETAILS_SUCCESS, payload: response.data });
};

export const fetchControlledBridgeModelDetails = (controlledBridgeModelId) => async (dispatch) => {
  const response = await getControlledBridgeModelDetails(controlledBridgeModelId);
  dispatch({ type: FETCH_CONTROLLED_BRIDGE_MODEL_DETAILS_SUCCESS, payload: response.data });
};

export const fetchMaintenanceTypeDetails = (maintenanceTypeId) => async (dispatch) => {
  const response = await getMaintenanceTypeDetails(maintenanceTypeId);
  dispatch({ type: FETCH_MAINTENANCE_TYPE_DETAILS_SUCCESS, payload: response.data });
};

export const fetchRefusalPointDetails = (refusalPointId) => async (dispatch) => {
  const response = await getRefusalPointDetails(refusalPointId);
  dispatch({ type: FETCH_REFUSAL_POINT_DETAILS_SUCCESS, payload: response.data });
};

export const fetchRecoveryMethodDetails = (recoveryMethodId) => async (dispatch) => {
  const response = await getRecoveryMethodDetails(recoveryMethodId);
  dispatch({ type: FETCH_RECOVERY_METHOD_DETAILS_SUCCESS, payload: response.data });
};