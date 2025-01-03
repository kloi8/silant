import React, { useEffect } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { useParams } from 'react-router-dom';
import { fetchEngineDetails } from '../../Services/actions';
import './EngineDetails.css';

const EngineDetails = () => {
  const dispatch = useDispatch();
  const { engineId } = useParams();
  const engine = useSelector((state) => state.engineDetails);

  useEffect(() => {
    dispatch(fetchEngineDetails(engineId));
  }, [dispatch, engineId]);

  return (
    <div className="engine-details">
      <h1>Детали двигателя</h1>
      <p>Название: {engine.title}</p>
      <p>Описание: {engine.description}</p>
    </div>
  );
};

export default EngineDetails;
