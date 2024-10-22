import React from 'react';

const BurgerMenu = ({ toggleMenu }) => {
  return (
    <div className="burger-menu" onClick={toggleMenu}>
      <div></div>
      <div></div>
      <div></div>
    </div>
  );
};

export default BurgerMenu;