import React, { useEffect } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { useParams } from 'react-router-dom';
import { fetchMaintenanceTypeDetails } from '../../Services/actions';
import './MaintenanceTypeDetails.css';

const MaintenanceTypeDetails = () => {
  const dispatch = useDispatch();
  const { maintenanceTypeId } = useParams();
  const maintenanceType = useSelector((state) => state.maintenanceTypeDetails);

  useEffect(() => {
    dispatch(fetchMaintenanceTypeDetails(maintenanceTypeId));
  }, [dispatch, maintenanceTypeId]);

  return (
    <div className="maintenance-type-details">
      <h1>Детали вида ТО</h1>
      <p>Название: {maintenanceType.title}</p>
      <p>Описание: {maintenanceType.description}</p>
    </div>
  );
};

export default MaintenanceTypeDetails;