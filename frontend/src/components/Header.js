import React from 'react';
import { Link } from 'react-router-dom';

const Header = () => {
  return (
    <header className="header">
      <div className="logo">JO 2024</div>
      <nav>
        <ul className="nav-links">
          <li><Link to="/epreuves">Les épreuves</Link></li>
          <li><Link to="/offres">Nos offres</Link></li>
          <li><Link to="/panier">Panier</Link></li>
          <li><Link to="/se-connecter">Se connecter</Link></li>
        </ul>
      </nav>
    </header>
  );
};

export default Header;