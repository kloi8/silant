import React from 'react';
import './Header.css';

const Header = () => (
  <header className="header">
    <div className="header-left">
      <button>Авторизация</button>
    </div>
    <div className="header-center">
      <span>+7-8352-20-12-09, telegram</span>
      {/* добавить ссылку^^^ */}
    </div>
    <div className="header-right">
      <img src="/logo.png" alt="Логотип" className="logo" />
    </div>
    <div className="header-bottom">
      <h1>Электронная сервисная книжка "Мой Силант"</h1>
    </div>
  </header>
);

export default Header;