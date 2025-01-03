import axios from './axios';

export const login = async (username, password) => {
    try {
        const response = await axios.post('/users/login/', { username, password });
        const { token, role } = response.data;
        localStorage.setItem('token', token);  // Сохраняем токен
        localStorage.setItem('role', role);  // Сохраняем роль
        return { token, role };
    } catch (error) {
        throw new Error('Ошибка при входе. Пожалуйста, проверьте свои данные');
    }
};

export const logout = async () => {
    try {
        await axios.post('/users/logout/');
        localStorage.removeItem('token');
        localStorage.removeItem('role');
    } catch (error) {
        throw new Error('Ошибка при выходе');
    }
}