import React, { useState, useEffect } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { fetchMachines, fetchMaintenances, fetchReclamations } from '../../Services/actions';
import Header from '../Header/Header';
import Footer from '../Footer/Footer';
import Tabs from '../Tabs/Tabs';
import Table from '../Table/Table';
import './Main.css';

const Main = () => {
  const dispatch = useDispatch();
  const machines = useSelector((state) => state.machines);
  const maintenances = useSelector((state) => state.maintenances);
  const reclamations = useSelector((state) => state.reclamations);
  const userRole = useSelector((state) => state.auth.userRole);
  const [activeTab, setActiveTab] = useState('Машина');
  const [filter, setFilter] = useState('');

  useEffect(() => {
    dispatch(fetchMachines());
    dispatch(fetchMaintenances());
    dispatch(fetchReclamations());
  }, [dispatch]);

  const tabs = ['Машина', 'ТО', 'Рекламации'];

  const handleTabChange = (tab) => {
    setActiveTab(tab);
  };

  const handleRowClick = (row) => {
    // Переход на страницу с деталями
  };

  const getColumns = (tab) => {
    switch (tab) {
      case 'Машина':
        if (!userRole) {
          return [
            { key: 'machineNumber', label: 'Зав. № машины' },
            { key: 'machineModel', label: 'Модель техники' },
            { key: 'engineModel', label: 'Модель двигателя' },
            { key: 'engineNumder', label: 'Зав.№ двигателя' },
            { key: 'transmissionModel', label: 'Модель трансмиссии' },
            { key: 'transmissionNumber', label: 'Зав. № трансмиссии' },
            { key: 'driveBridgeModel', label: 'Модель ведущего моста' },
            { key: 'driveBidgeNumder', label: 'Зав. № ведущего моста' },
            { key: 'controlledBridgeModel', label: 'Модель управляемого моста' },
            { key: 'controlledBridgeNumber', label: 'Зав. № управляемого моста' },
          ];
        } else {
          return [
            { key: 'machineNumber', label: 'Зав. № машины' },
            { key: 'machineModel', label: 'Модель техники' },
            { key: 'engineModel', label: 'Модель двигателя' },
            { key: 'engineNumder', label: 'Зав.№ двигателя' },
            { key: 'transmissionModel', label: 'Модель трансмиссии' },
            { key: 'transmissionNumber', label: 'Зав. № трансмиссии' },
            { key: 'driveBridgeModel', label: 'Модель ведущего моста' },
            { key: 'driveBidgeNumder', label: 'Зав. № ведущего моста' },
            { key: 'controlledBridgeModel', label: 'Модель управляемого моста' },
            { key: 'controlledBridgeNumber', label: 'Зав. № управляемого моста' },
            { key: 'contract', label: 'Договор поставки №, дата' },
            { key: 'shipmentDate', label: 'Дата отгрузки' },
            { key: 'consignee', label: 'Грузополучатель' },
            { key: 'deliveryAdress', label: 'Адрес поставки' },
            { key: 'equipment', label: 'Комплектация' },
            { key: 'client', label: 'Клиент' },
            { key: 'serviceCompany', label: 'Сервисная компания' },
          ];
        }
      case 'ТО':
        return [
          { key: 'maintType', label: 'Вид ТО' },
          { key: 'machine', label: 'Машина' },
          { key: 'serviceCompany', label: 'Сервисная компания' },
        ];
      case 'Рекламации':
        return [
          { key: 'refusalPoint', label: 'Узел отказа' },
          { key: 'recoveryMethod', label: 'Способ восстановления' },
          { key: 'serviceCompany', label: 'Сервисная компания' },
        ];
      default:
        return [];
    }
  };

  const getData = (tab) => {
    switch (tab) {
      case 'Машина':
        return machines.filter((machine) =>
          machine.machineNumber.includes(filter)
        );
      case 'ТО':
        return maintenances.filter((maintenance) =>
          maintenance.machine.machineNumber.includes(filter)
        );
      case 'Рекламации':
        return reclamations.filter((reclamation) =>
          reclamation.machine.machineNumber.includes(filter)
        );
      default:
        return [];
    }
  };

  return (
    <div className="main">
      <Header />
      <div className="user-info">
        <span>Имя пользователя: {userRole}</span>
      </div>
      <div className="info-text">
        <span>Информация о комплектации и технических характеристиках вашей техники</span>
      </div>
      <Tabs tabs={tabs} onTabChange={handleTabChange} />
      <Table
        data={getData(activeTab)}
        columns={getColumns(activeTab)}
        onRowClick={handleRowClick}
      />
      <Footer />
    </div>
  );
};

export default Main;

