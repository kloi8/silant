import React, { useEffect } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { useParams } from 'react-router-dom';
import { fetchRefusalPointDetails } from '../../Services/actions';
import './RefusalPointDetails.css';

const RefusalPointDetails = () => {
  const dispatch = useDispatch();
  const { refusalPointId } = useParams();
  const refusalPoint = useSelector((state) => state.refusalPointDetails);

  useEffect(() => {
    dispatch(fetchRefusalPointDetails(refusalPointId));
  }, [dispatch, refusalPointId]);

  return (
    <div className="refusal-point-details">
      <h1>Детали узла отказа</h1>
      <p>Название: {refusalPoint.title}</p>
      <p>Описание: {refusalPoint.description}</p>
    </div>
  );
};

export default RefusalPointDetails;