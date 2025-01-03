import React, { useEffect } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { useParams } from 'react-router-dom';
import { fetchControlledBridgeModelDetails } from '../../Services/actions';
import './ControlledBridgeModelDetails.css';

const ControlledBridgeModelDetails = () => {
  const dispatch = useDispatch();
  const { controlledBridgeModelId } = useParams();
  const controlledBridgeModel = useSelector((state) => state.controlledBridgeModelDetails);

  useEffect(() => {
    dispatch(fetchControlledBridgeModelDetails(controlledBridgeModelId));
  }, [dispatch, controlledBridgeModelId]);

  return (
    <div className="controlled-bridge-model-details">
      <h1>Детали модели управляемого моста</h1>
      <p>Название: {controlledBridgeModel.title}</p>
      <p>Описание: {controlledBridgeModel.description}</p>
    </div>
  );
};

export default ControlledBridgeModelDetails;