import React, { useEffect, useState, useContext } from 'react';
import axios from '../axios';
import { useNavigate } from 'react-redux';
import { AuthContext } from '../context/AuthContext';
import AddListsObjects from './AddListsObjects';

const Maintenance = () => {
    const [maintenances, setMaintenances] = useState([]);
    const [search, setSearch] = useState('');
    const [sortedMaintenances, setSortedMaintenances] = useState([]);
    const { role } = useContext(AuthContext);
    const navigate = useNavigate();

    useEffect(() => {
        const fetchMaintenances = async () => {
            try {
                const response = await axios.get('/api/maintenances/');
                setMaintenances(response.data);
            } catch (error) {
                console.error('Error fetching maintenances:', error);
            }
        };
        fetchMaintenances();
    }, []);

    useEffect(() => {
        setSortedMaintenances(maintenances);
    }, [maintenances]);

    const handleSort = (field) => {
        const sorted = [...sortedMaintenances].sort((a, b) => a[field] > b[field] ? 1 : -1);
        setSortedMaintenances(sorted);
    };

    const handleSearch = () => {
        const filtered = maintenances.filter((maintenance) =>
            maintenance.workOrderNumber.includes(search)
        );
        setSortedMaintenances(filtered);
    };

    return (
        <div>
            <h2>Maintenance</h2>
            {role === 'client' || role === 'service' || role === 'manager' ? (
                <div>
                    <input
                        type="text"
                        placeholder="Search by Work Order Number"
                        value={search}
                        onChange={(e) => setSearch(e.target.value)}
                    />
                    <button onClick={handleSearch}>Search</button>
                </div>
            ) : null}
            {role === 'manager' && (
                <div className="list-buttons">
                    <AddListsObjects url={'maintenance-type'} label={'Добавить Вид ТО'} />
                    <AddListsObjects url={'maintenance-organization'} label={'Добавить Организацию, проводившую ТО'} />
                </div>
            )}
            <table>
                <thead>
                    <tr>
                        <th onClick={() => handleSort('maintDate')}>Maintenance Date</th>
                        <th>Вид ТО</th>
                        <th>Дата проведения ТО</th>
                        <th>Наработка м/час</th>
                        <th>№ заказ-наряда</th>
                        <th>Дата заказ-наряда</th>
                        <th>Организация, проводившая ТО</th>
                        <th>Машина</th>
                        <th>Сервисная компания</th>
                    </tr>
                </thead>
                <tbody>
                    {sortedMaintenances.map((maintenance) => (
                            <tr key={maintenance.id} onClick={() => navigate(`/maintenance/${maintenance.id}`)}>
                            <td>{maintenance.maintType}</td>
                            <td>{maintenance.maintDate}</td>
                            <td>{maintenance.maintDevelopment}</td>
                            <td>{maintenance.workOrderNumber}</td>
                            <td>{maintenance.workOrderDate}</td>
                            <td>{maintenance.maintOrganization}</td>
                            <td>{maintenance.machine}</td>
                            <td>{maintenance.serviceCompany}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
};

export default Maintenance;
