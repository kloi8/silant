import React, { useEffect, useState, useContext} from 'react';
import axios from '../axios'; 
import { useNavigate } from 'react-redux';
import { AuthContext } from '../context/AuthContext';


const Reclamation = () => {
    const [reclamations, setReclamations] = useState([]);
    const [search, setSearch] = useState('');
    const [sortedReclamations, setSortedReclamations] = useState([]);
    const { role } = useContext(AuthContext);
    const navigate = useNavigate();

    useEffect(() => {
        const fetchReclamations = async () => {
            try {
                const response = await axios.get('/api/reclamations/');
                setReclamations(response.data);
            } catch (error) {
                console.error('Error fetching reclamations:', error);
            }
        };
        fetchReclamations();
    }, []);

    useEffect(() => {
        setSortedReclamations(reclamations);
    }, [reclamations]);

    const handleSort = (field) => {
        const sorted = [...sortedReclamations].sort((a, b) => a[field] > b[field] ? 1 : -1);
        setSortedReclamations(sorted);
    };

    const handleSearch = () => {
        const filtered = reclamations.filter((reclamation) =>
            reclamation.workOrderNumber.includes(search)
        );
        setSortedReclamations(filtered);
    };

    return (
        <div>
            <h2>Reclamations</h2>
            {role === 'service' || role === 'manager' ? (
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

            <table>
                <thead>
                    <tr>
                        <th onClick={() => handleSort('refusalDate')}>Refusal Date</th>
                        <th>Дата отказа</th>
                        <th>Наработка м/час</th>
                        <th>Узел отказа</th>
                        <th>Описание отказа</th>
                        <th>Способ восстановления</th>
                        <th>Используемые зап.части</th>
                        <th>Дата восстановления</th>
                        <th>Время простоя техники</th>
                        <th>Машина</th>
                        <th>Сервисная компания</th>
                    </tr>
                </thead>
                <tbody>
                    {sortedReclamations.map((reclamation) => (
                        <tr key={reclamation.id} onClick={() => navigate(`/reclamation/${reclamation.id}`)}>
                            <td>{reclamation.refusalDate}</td>
                            <td>{reclamation.reclamationDevelopment}</td>
                            <td>{reclamation.refusalPoint}</td>
                            <td>{reclamation.refusalDescription}</td>
                            <td>{reclamation.recoveryMethod}</td>
                            <td>{reclamation.spareParts}</td>
                            <td>{reclamation.recoveryDate}</td>
                            <td>{reclamation.machineDowntime}</td>
                            <td>{reclamation.machine}</td>
                            <td>{reclamation.serviceCompany}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
};

export default Reclamation;
