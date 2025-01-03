import React, { useEffect } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { useParams } from 'react-router-dom';
import { fetchDriveBridgeModelDetails } from '../../Services/actions';
import './DriveBridgeModelDetails.css';

const DriveBridgeModelDetails = () => {
  const dispatch = useDispatch();
  const { driveBridgeModelId } = useParams();
  const driveBridgeModel = useSelector((state) => state.driveBridgeModelDetails);

  useEffect(() => {
    dispatch(fetchDriveBridgeModelDetails(driveBridgeModelId));
  }, [dispatch, driveBridgeModelId]);

  return (
    <div className="drive-bridge-model-details">
      <h1>Детали модели ведущего моста</h1>
      <p>Название: {driveBridgeModel.title}</p>
      <p>Описание: {driveBridgeModel.description}</p>
    </div>
  );
};

export default DriveBridgeModelDetails;