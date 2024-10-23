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

      <div className="epreuves">
        <h2>Les Épreuves</h2>


        <div className="epreuve">
          <h3><FaRunning /> Athlétisme - 100m</h3>
          <div className="details">
            <span><strong>Date :</strong> 26 juillet 2024</span>
            <span><strong>Lieu :</strong> Stade Olympique</span>
          </div>
          <div className="description">
            Série éliminatoire messieurs, groupe 1
          </div>
          <button>Réserver</button>
        </div>

        <div className="epreuve">
          <h3><FaRunning /> Athlétisme - 200m</h3>
          <div className="details">
            <span><strong>Date :</strong> 27 juillet 2024</span>
            <span><strong>Lieu :</strong> Stade Olympique</span>
          </div>
          <div className="description">
            Demi-finale dames, groupe 1
          </div>
          <button>Réserver</button>
        </div>

        <div className="epreuve">
          <h3><FaRunning /> Relais 4x100m</h3>
          <div className="details">
            <span><strong>Date :</strong> 28 juillet 2024</span>
            <span><strong>Lieu :</strong> Stade Olympique</span>
          </div>
          <div className="description">
            Finale hommes
          </div>
          <button>Réserver</button>
        </div>

        <div className="view-all">
          <Link to="/epreuves">
            <button>Voir toutes les épreuves</button>
          </Link>
        </div>

      </div>

      <Footer />
    </div>
  );
};

export default Home;