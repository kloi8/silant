import React, { useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { addMachineList } from '../../Services/actions';
import { useNavigate } from 'react-router-dom';


const AddMachineForm = () => {
  const [formData, setFormData] = useState({
    machineNumber: '',
    machineModel: '',
    engineModel: '',
    engineNumder: '',
    transmissionModel: '',
    transmissionNumber: '',
    driveBridgeModel: '',
    driveBidgeNumder: '',
    controlledBridgeModel: '',
    controlledBridgeNumber: '',
    contract: '',
    shipmentDate: '',
    consignee: '',
    deliveryAdress: '',
    equipment: '',
    client: '',
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
      dispatch(addMachineList(formData));
      navigate('/machines');
    } else {
      alert('У вас нет прав для добавления машины.');
    }
  };

  return (
    <div>
      <h1>Добавить машину</h1>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          name="machineNumber"
          placeholder="Зав. № машины"
          value={formData.machineNumber}
          onChange={handleChange}
        />
        <input
          type="text"
          name="machineModel"
          placeholder="Модель техники"
          value={formData.machineModel}
          onChange={handleChange}
        />
        <input
          type="text"
          name="engineModel"
          placeholder="Модель двигателя"
          value={formData.engineModel}
          onChange={handleChange}
        />
        <input
          type="text"
          name="engineNumder"
          placeholder="Зав.№ двигателя"
          value={formData.engineNumder}
          onChange={handleChange}
        />
        <input
          type="text"
          name="transmissionModel"
          placeholder="Модель трансмиссии"
          value={formData.transmissionModel}
          onChange={handleChange}
        />
        <input
          type="text"
          name="transmissionNumber"
          placeholder="Зав. № трансмиссии"
          value={formData.transmissionNumber}
          onChange={handleChange}
        />
        <input
          type="text"
          name="driveBridgeModel"
          placeholder="Модель ведущего моста"
          value={formData.driveBridgeModel}
          onChange={handleChange}
        />
        <input
          type="text"
          name="driveBidgeNumder"
          placeholder="Зав. № ведущего моста"
          value={formData.driveBidgeNumder}
          onChange={handleChange}
        />
        <input
          type="text"
          name="controlledBridgeModel"
          placeholder="Модель управляемого моста"
          value={formData.controlledBridgeModel}
          onChange={handleChange}
        />
        <input
          type="text"
          name="controlledBridgeNumber"
          placeholder="Зав. № управляемого моста"
          value={formData.controlledBridgeNumber}
          onChange={handleChange}
        />
        <input
          type="text"
          name="contract"
          placeholder="Договор поставки №, дата"
          value={formData.contract}
          onChange={handleChange}
        />
        <input
          type="date"
          name="shipmentDate"
          placeholder="Дата отгрузки"
          value={formData.shipmentDate}
          onChange={handleChange}
        />
        <input
          type="text"
          name="consignee"
          placeholder="Грузополучатель"
          value={formData.consignee}
          onChange={handleChange}
        />
        <input
          type="text"
          name="deliveryAdress"
          placeholder="Адрес поставки"
          value={formData.deliveryAdress}
          onChange={handleChange}
        />
        <input
          type="text"
          name="equipment"
          placeholder="Комплектация"
          value={formData.equipment}
          onChange={handleChange}
        />
        <input
          type="text"
          name="client"
          placeholder="Клиент"
          value={formData.client}
          onChange={handleChange}
        />
        <input
          type="text"
          name="serviceCompany"
          placeholder="Сервисная компания"
          value={formData.serviceCompany}
          onChange={handleChange}
        />
        <button type="submit">Добавить машину</button>
      </form>
    </div>
  );
};

export default AddMachineForm;