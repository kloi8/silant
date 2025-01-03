import React from 'react';

import { BrowserRouter as Router, Route, Routes } from 'react-router-dom'

import Header from './components/Header/Header';
import Footer from './components/Footer/Footer';

import MachineDetails from './components/Main/MachineDetails';
import EngineDetails from './components/Main/EngineDetails';
import EquipmentModelDetails from './components/Main/EquipmentModelDetails';
import TransmissionModelDetails from './components/Main/TransmissionModelDetails';
import DriveBridgeModelDetails from './components/Main/DriveBridgeModelDetails';
import ControlledBridgeModelDetails from './components/Main/ControlledBridgeModelDetails';
import MaintenanceTypeDetails from './components/Main/MaintenanceTypeDetails';
import RefusalPointDetails from './components/Main/RefusalPointDetails';
import RecoveryMethodDetails from './components/Main/RecoveryMethodDetails';
import AddMachineForm from './components/Forms/AddMachineForm';
import AddMaintenanceForm from './components/Forms/AddMaintenanceForm';
import AddReclamationForm from './components/Forms/AddReclamationForm';


import Login from './components/Main/LoginComponent'
import Main from './components/Main/Main'
import { AuthProvider } from './context/AuthContext';


function App() {

  return (
    <AuthProvider>
            <Router>
              <Header />

        <Routes>
          <Route path = "/login" element={<Login />}/>
          <Route path="/" element={<Main />} />
          {/* <Route path="/machines" element={<Machines />} /> */}
          <Route path="/machine/:machineId" element={<MachineDetails />} />
        <Route path="/engine/:engineId" element={<EngineDetails />} />
        <Route path="/equipment-model/:equipmentModelId" element={<EquipmentModelDetails />} />
        <Route path="/transmission-model/:transmissionModelId" element={<TransmissionModelDetails />} />
        <Route path="/drive-bridge-model/:driveBridgeModelId" element={<DriveBridgeModelDetails />} />
        <Route path="/controlled-bridge-model/:controlledBridgeModelId" element={<ControlledBridgeModelDetails />} />
        <Route path="/maintenance-type/:maintenanceTypeId" element={<MaintenanceTypeDetails />} />
        <Route path="/refusal-point/:refusalPointId" element={<RefusalPointDetails />} />
        <Route path="/recovery-method/:recoveryMethodId" element={<RecoveryMethodDetails />} />
        <Route path="/add-machine" element={<AddMachineForm />} />
        <Route path="/add-maintenance" element={<AddMaintenanceForm />} />
        <Route path="/add-reclamation" element={<AddReclamationForm />} />

        </Routes>
      <Footer />
      </Router>
    </AuthProvider>

  );
}

export default App;


