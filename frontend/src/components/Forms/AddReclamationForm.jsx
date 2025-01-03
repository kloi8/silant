import React, { useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { addReclamationList } from '../../Services/actions';
import { useNavigate } from 'react-router-dom';

const AddReclamationForm = () => {
  const [formData, setFormData] = useState({
    refusalDate: '',
    reclamationDevelopment: '',
    refusalPoint: '',
    refusalDescription: '',
    recoveryMethod: '',
    spareParts: '',
    recoveryDate: '',
    machine: '',
    serviceCompany: '',
  });

  const dispatch = useDispatch();
  const navigate = useNavigate();
  const userRole = useSelector((state) => state.auth.userRole);

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (userRole === 'manager') {
      dispatch(addReclamationList(formData));
      navigate('/reclamations');
    } else {
      alert('У вас нет прав для добавления рекламации.');
    }
  };

  return (
    <div>
      <h1>Добавить рекламацию</h1>
      <form onSubmit={handleSubmit}>
        <input
          type="date"
          name="refusalDate"
          placeholder="Дата отказа"
          value={formData.refusalDate}
          onChange={handleChange}
        />
        <input
          type="number"
          name="reclamationDevelopment"
          placeholder="Наработка м/час"
          value={formData.reclamationDevelopment}
          onChange={handleChange}
        />
        <input
          type="text"
          name="refusalPoint"
          placeholder="Узел отказа"
          value={formData.refusalPoint}
          onChange={handleChange}
        />
        <input
          type="text"
          name="refusalDescription"
          placeholder="Описание отказа"
          value={formData.refusalDescription}
          onChange={handleChange}
        />
        <input
          type="text"
          name="recoveryMethod"
          placeholder="Способ восстановления"
          value={formData.recoveryMethod}
          onChange={handleChange}
        />
        <input
          type="text"
          name="spareParts"
          placeholder="Используемые зап.части"
          value={formData.spareParts}
          onChange={handleChange}
        />
        <input
          type="date"
          name="recoveryDate"
          placeholder="Дата восстановления"
          value={formData.recoveryDate}
          onChange={handleChange}
        />
        <input
          type="text"
          name="machine"
          placeholder="Машина"
          value={formData.machine}
          onChange={handleChange}
        />
        <input
          type="text"
          name="serviceCompany"
          placeholder="Сервисная компания"
          value={formData.serviceCompany}
          onChange={handleChange}
        />
        <button type="submit">Добавить рекламацию</button>
      </form>
    </div>
  );
};

export default AddReclamationForm;
