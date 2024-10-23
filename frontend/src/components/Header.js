import React, { useState } from 'react';
import NavLinks from './NavLinks';
import BurgerMenu from './BurgerMenu';

const Header = () => {
  const [menuOpen, setMenuOpen] = useState(false);

  const toggleMenu = () => {
    setMenuOpen(!menuOpen);
  };

  return (
    <header className="header">
      <div className="logo">🏅 JO 2024</div>

      <nav>
        <NavLinks />

        <BurgerMenu toggleMenu={toggleMenu} />

        <div className={`mobile-nav ${menuOpen ? "open" : ""}`}>
          <NavLinks onLinkClick={toggleMenu} />
        </div>
      </nav>
    </header>
  );
};

export default Header;