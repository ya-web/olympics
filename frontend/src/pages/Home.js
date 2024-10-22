import React from 'react';
import Header from '../components/Header';
import Footer from '../components/Footer';
import { Link } from 'react-router-dom';
import { FaRunning } from 'react-icons/fa';
const Home = () => {
  return (
    <div>
      <Header />
      <h1>Bienvenue aux Jeux Olympiques 2024</h1>
      <p className='home_desc'>Les Jeux Olympiques de 2024 se dérouleront à Paris. Venez vivre des moments historiques en assistant aux plus grandes compétitions sportives mondiales.</p>
      
      <h2>Les Épreuves</h2>
      <div className="epreuves">
        <div className="epreuve">
          <h3><FaRunning /> Athlétisme - 100m</h3>
          <p><strong>Date :</strong> 26 juillet 2024</p>
          <p><strong>Lieu :</strong> Stade Olympique</p>
          <button>Réservez vos places</button>
        </div>

        <div className="epreuve">
          <h3><FaRunning /> Athlétisme - 200m</h3>
          <p><strong>Date :</strong> 27 juillet 2024</p>
          <p><strong>Lieu :</strong> Stade Olympique</p>
          <button>Réservez vos places</button>
        </div>

        <div className="epreuve">
          <h3><FaRunning /> Relais 4x100m</h3>
          <p><strong>Date :</strong> 28 juillet 2024</p>
          <p><strong>Lieu :</strong> Stade Olympique</p>
          <button>Réservez vos places</button>
        </div>
      </div>

      <div className="view-all">
        <Link to="/epreuves">
          <button>Voir toutes les épreuves</button>
        </Link>
      </div>

      <Footer />
    </div>
  );
};

export default Home;