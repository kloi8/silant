import React, { useEffect } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { useParams } from 'react-router-dom';
import { fetchRecoveryMethodDetails } from '../../Services/actions';
import './RecoveryMethodDetails.css';

const RecoveryMethodDetails = () => {
  const dispatch = useDispatch();
  const { recoveryMethodId } = useParams();
  const recoveryMethod = useSelector((state) => state.recoveryMethodDetails);

  useEffect(() => {
    dispatch(fetchRecoveryMethodDetails(recoveryMethodId));
  }, [dispatch, recoveryMethodId]);

  return (
    <div className="recovery-method-details">
      <h1>Детали способа восстановления</h1>
      <p>Название: {recoveryMethod.title}</p>
      <p>Описание: {recoveryMethod.description}</p>
    </div>
  );
};

export default RecoveryMethodDetails;