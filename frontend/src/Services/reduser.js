import {
    FETCH_MACHINES_SUCCESS,
    FETCH_MAINTENANCES_SUCCESS,
    FETCH_RECLAMATIONS_SUCCESS,
    ADD_MACHINE_SUCCESS,
    ADD_MAINTENANCE_SUCCESS,
    ADD_RECLAMATION_SUCCESS,
    FETCH_MACHINE_DETAILS_SUCCESS,
    FETCH_ENGINE_DETAILS_SUCCESS,
    FETCH_EQUIPMENT_MODEL_DETAILS_SUCCESS,
    FETCH_TRANSMISSION_MODEL_DETAILS_SUCCESS,
    FETCH_DRIVE_BRIDGE_MODEL_DETAILS_SUCCESS,
    FETCH_CONTROLLED_BRIDGE_MODEL_DETAILS_SUCCESS,
    FETCH_MAINTENANCE_TYPE_DETAILS_SUCCESS,
    FETCH_REFUSAL_POINT_DETAILS_SUCCESS,
    FETCH_RECOVERY_METHOD_DETAILS_SUCCESS,
  } from './actions';
  
  const initialState = {
    machines: [],
    maintenances: [],
    reclamations: [],
    machineDetails: null,
    engineDetails: null,
    equipmentModelDetails: null,
    transmissionModelDetails: null,
    driveBridgeModelDetails: null,
    controlledBridgeModelDetails: null,
    maintenanceTypeDetails: null,
    refusalPointDetails: null,
    recoveryMethodDetails: null,
  };
  
  const rootReducer = (state = initialState, action) => {
    switch (action.type) {
      case FETCH_MACHINES_SUCCESS:
        return { ...state, machines: action.payload };
      case FETCH_MAINTENANCES_SUCCESS:
        return { ...state, maintenances: action.payload };
      case FETCH_RECLAMATIONS_SUCCESS:
        return { ...state, reclamations: action.payload };
      case ADD_MACHINE_SUCCESS:
        return { ...state, machines: [...state.machines, action.payload] };
      case ADD_MAINTENANCE_SUCCESS:
        return { ...state, maintenances: [...state.maintenances, action.payload] };
      case ADD_RECLAMATION_SUCCESS:
        return { ...state, reclamations: [...state.reclamations, action.payload] };
      case FETCH_MACHINE_DETAILS_SUCCESS:
        return { ...state, machineDetails: action.payload };
      case FETCH_ENGINE_DETAILS_SUCCESS:
        return { ...state, engineDetails: action.payload };
      case FETCH_EQUIPMENT_MODEL_DETAILS_SUCCESS:
        return { ...state, equipmentModelDetails: action.payload };
      case FETCH_TRANSMISSION_MODEL_DETAILS_SUCCESS:
        return { ...state, transmissionModelDetails: action.payload };
      case FETCH_DRIVE_BRIDGE_MODEL_DETAILS_SUCCESS:
        return { ...state, driveBridgeModelDetails: action.payload };
      case FETCH_CONTROLLED_BRIDGE_MODEL_DETAILS_SUCCESS:
        return { ...state, controlledBridgeModelDetails: action.payload };
      case FETCH_MAINTENANCE_TYPE_DETAILS_SUCCESS:
        return { ...state, maintenanceTypeDetails: action.payload };
      case FETCH_REFUSAL_POINT_DETAILS_SUCCESS:
        return { ...state, refusalPointDetails: action.payload };
      case FETCH_RECOVERY_METHOD_DETAILS_SUCCESS:
        return { ...state, recoveryMethodDetails: action.payload };
      default:
        return state;
    }
  };
  
  export default rootReducer;