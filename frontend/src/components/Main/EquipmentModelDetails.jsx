import React, { useEffect } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { useParams } from 'react-router-dom';
import { fetchEquipmentModelDetails } from '../../Services/actions';
import './EquipmentModelDetails.css';

const EquipmentModelDetails = () => {
  const dispatch = useDispatch();
  const { equipmentModelId } = useParams();
  const equipmentModel = useSelector((state) => state.equipmentModelDetails);

  useEffect(() => {
    dispatch(fetchEquipmentModelDetails(equipmentModelId));
  }, [dispatch, equipmentModelId]);

  return (
    <div className="equipment-model-details">
      <h1>Детали модели техники</h1>
      <p>Название: {equipmentModel.title}</p>
      <p>Описание: {equipmentModel.description}</p>
    </div>
  );
};

export default EquipmentModelDetails;