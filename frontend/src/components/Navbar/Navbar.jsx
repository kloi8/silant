import React, {useContext} from 'react';
import { useNavigate } from 'react-router-dom';
import { AuthContext } from '../../context/AuthContext';

const Navbar = () => {
    const navigate = useNavigate();
    const { logout } = useContext(AuthContext);

    const handleLogout = () => {
        logout();
        navigate('/login');
    };

    return (
        <nav>
            <button onClick={() => navigate('/machines')}>Machines</button>
            <button onClick={() => navigate('/maintenance')}>Maintenance</button>
            <button onClick={() => navigate('/reclamation')}>Reclamation</button>
            <button onClick={handleLogout}>Logout</button>
        </nav>
    );
};

export default Navbar;
