import React from 'react';
import { Link } from 'react-router-dom';

const NavLinks = ({ onLinkClick }) => {
  return (
    <ul className="nav-links">
      <li><Link to="/epreuves" onClick={onLinkClick}>Les épreuves</Link></li>
      <li><Link to="/offres" onClick={onLinkClick}>Nos offres</Link></li>
      <li><Link to="/panier" onClick={onLinkClick}>Panier</Link></li>
      <li><Link to="/se-connecter" onClick={onLinkClick}>Se connecter</Link></li>
    </ul>
  );
};

export default NavLinks;