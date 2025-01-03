import React, { useEffect } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { useParams } from 'react-router-dom';
import { fetchTransmissionModelDetails } from '../../Services/actions';
import './TransmissionModelDetails.css';

const TransmissionModelDetails = () => {
  const dispatch = useDispatch();
  const { transmissionModelId } = useParams();
  const transmissionModel = useSelector((state) => state.transmissionModelDetails);

  useEffect(() => {
    dispatch(fetchTransmissionModelDetails(transmissionModelId));
  }, [dispatch, transmissionModelId]);

  return (
    <div className="transmission-model-details">
      <h1>Детали модели трансмиссии</h1>
      <p>Название: {transmissionModel.title}</p>
      <p>Описание: {transmissionModel.description}</p>
    </div>
  );
};

export default TransmissionModelDetails;