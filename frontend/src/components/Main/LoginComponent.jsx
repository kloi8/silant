// import React, { useState, useContext } from 'react';
// import axios from '../axios';
// import { useNavigate } from 'react-router-dom';
// import { AuthContext } from '../context/AuthContext';

// const Login = () => {
//     const [username, setUsername] = useState('');
//     const [password, setPassword] = useState('');
//     const [message, setMessage] = useState('');
//     const navigate = useNavigate();
//     const { login } = useContext(AuthContext);

//     const handleLogin = async () => {
//         try {
//             const response = await axios.post('/api/users/login/', { username, password });
//             login(response.data.role);
//             navigate('/machines');
//         } catch (error) {
//             setMessage(error.response.data.message);
//         }
//     };

//     return (
//         <div>
//             <h2>Login</h2>
//             <input type="text" placeholder="Username" value={username} onChange={(e) => setUsername(e.target.value)} />
//             <input type="password" placeholder="Password" value={password} onChange={(e) => setPassword(e.target.value)} />
//             <button onClick={handleLogin}>Login</button>
//             {message && <p>{message}</p>}
//         </div>
//     );
// };

// export default Login;



import React, { useState } from "react";
import { useRole } from "../../context/RoleContext";
import "../Main/LoginComponent.css";

const Login = () => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const { setRole } = useRole();

  const handleLogin = () => {
    // Replace with actual authentication logic
    if (username === "client") setRole("client");
    else if (username === "service") setRole("service");
    else if (username === "manager") setRole("manager");
  };

  return (
    <div className="login-container">
      <h1>Авторизация</h1>
      <input
        type="text"
        placeholder="Логин"
        value={username}
        onChange={(e) => setUsername(e.target.value)}
      />
      <input
        type="password"
        placeholder="Пароль"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
      />
      <button onClick={handleLogin}>Войти</button>
    </div>
  );
};

export default Login;

