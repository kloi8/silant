import React, { createContext, useContext, useState, useEffect } from 'react';

const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
    const [role, setRole] = useState(null);

    const login = (role) => {
        setRole(role);
        localStorage.setItem('role', role); 
    };

    const logout = () => {
        setRole(null);
        localStorage.removeItem('role');
    };

    useEffect(() => {
        const storedRole = localStorage.getItem('role');
        if (storedRole) setRole(storedRole);
    }, []);

    return (
        <AuthContext.Provider value={{ role, login, logout }}>
            {children}
        </AuthContext.Provider>
    );
};

export const useAuth = () => {
    return useContext(AuthContext);
};

export { AuthContext };