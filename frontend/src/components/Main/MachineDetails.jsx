import React, { useEffect } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { useParams } from 'react-router-dom';
import { fetchMachineDetails } from '../../Services/actions';
import Table from '../Table/Table';
import './MachineDetails.css';

const MachineDetails = () => {
  const dispatch = useDispatch();
  const { machineId } = useParams();
  const machine = useSelector((state) => state.machineDetails);
  const maintenances = useSelector((state) => state.maintenances);
  const reclamations = useSelector((state) => state.reclamations);
  const userRole = useSelector((state) => state.auth.userRole);

  useEffect(() => {
    dispatch(fetchMachineDetails(machineId));
  }, [dispatch, machineId]);

  const machineMaintenances = maintenances.filter((maintenance) =>
    maintenance.machine.id === machineId
  );

  const machineReclamations = reclamations.filter((reclamation) =>
    reclamation.machine.id === machineId
  );

  const getMachineColumns = () => {
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
  };

  return (
    <div className="machine-details">
      <h1>Детали машины</h1>
      <Table data={[machine]} columns={getMachineColumns()} />
      <h2>ТО для этой машины</h2>
      <Table data={machineMaintenances} columns={[
        { key: 'maintType', label: 'Вид ТО' },
        { key: 'maintDate', label: 'Дата проведения ТО' },
        { key: 'maintDevelopment', label: 'Наработка м/час' },
        { key: 'workOrderNumder', label: '№ заказ-наряда' },
        { key: 'workOrderDate', label: 'Дата заказ-наряда' },
        { key: 'maintOrganization', label: 'Организация, проводившая ТО' },
        { key: 'serviceCompany', label: 'Сервисная компания' },
      ]} />
      <h2>Рекламации для этой машины</h2>
      <Table data={machineReclamations} columns={[
        { key: 'refusalDate', label: 'Дата отказа' },
        { key: 'reclamationDevelopment', label: 'Наработка м/час' },
        { key: 'refusalPoint', label: 'Узел отказа' },
        { key: 'refusalDescription', label: 'Описание отказа' },
        { key: 'recoveryMethod', label: 'Способ восстановления' },
        { key: 'spareParts', label: 'Используемые зап.части' },
        { key: 'recoveryDate', label: 'Дата восстановления' },
        { key: 'machineDowntime', label: 'Время простоя техники' },
        { key: 'serviceCompany', label: 'Сервисная компания' },
      ]} />
    </div>
  );
};

export default MachineDetails;