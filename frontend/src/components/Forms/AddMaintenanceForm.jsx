import React, { useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { addMaintenanceList } from '../../Services/actions';
import { useNavigate } from 'react-router-dom';

const AddMaintenanceForm = () => {
  const [formData, setFormData] = useState({
    maintType: '',
    maintDate: '',
    maintDevelopment: '',
    workOrderNumder: '',
    workOrderDate: '',
    maintOrganization: '',
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
      dispatch(addMaintenanceList(formData));
      navigate('/maintenance');
    } else {
      alert('У вас нет прав для добавления ТО.');
    }
  };

  return (
    <div>
      <h1>Добавить ТО</h1>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          name="maintType"
          placeholder="Вид ТО"
          value={formData.maintType}
          onChange={handleChange}
        />
        <input
          type="date"
          name="maintDate"
          placeholder="Дата проведения ТО"
          value={formData.maintDate}
          onChange={handleChange}
        />
        <input
          type="number"
          name="maintDevelopment"
          placeholder="Наработка м/час"
          value={formData.maintDevelopment}
          onChange={handleChange}
        />
        <input
          type="text"
          name="workOrderNumder"
          placeholder="№ заказ-наряда"
          value={formData.workOrderNumder}
          onChange={handleChange}
        />
        <input
          type="date"
          name="workOrderDate"
          placeholder="Дата заказ-наряда"
          value={formData.workOrderDate}
          onChange={handleChange}
        />
        <input
          type="text"
          name="maintOrganization"
          placeholder="Организация, проводившая ТО"
          value={formData.maintOrganization}
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
        <button type="submit">Добавить ТО</button>
      </form>
    </div>
  );
};

export default AddMaintenanceForm;
