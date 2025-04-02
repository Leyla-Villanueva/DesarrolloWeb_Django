import { useState, useEffect } from "react";
import axios from "axios";
import {BrowserRouter as Router, Route, Routes, useLocation} from "react-router-dom";
import Login from "./components/Login";
import Navbar from "./components/Navbar";
import AboutUs from "./pages/AboutUs";
import NotFound from "./pages/404";
import { AnimatePresence } from "framer-motion";
import "bootstrap/dist/css/bootstrap.min.css";

import NewUser from "./components/NewUser.jsx";
import EditUser from "./components/EditUser.jsx";


const AnimatedRoutes = () => {
  const location = useLocation();
  return (
    <AnimatePresence mode="await">
      <Routes location={location} key={location.pathname}>
        <Route path="/login" element={<Login />} />
        <Route path="/about" element={<AboutUs />} />
        <Route path="/register" element={<NewUser />} />
        <Route path="/" element={<Home />} />
        <Route path="*" element={<NotFound />} />
      </Routes>
    </AnimatePresence>
  );
};

function Home(){
  const [data, setData] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [successMessage, setSuccessMessage] = useState(null);
  const [currentPage, setCurrentPage] = useState(1);
  const [itemsPerPage] = useState(5);

  const [userEdit, setUserEdit] = useState(null);
  const [showForm, setShowForm] = useState(false);

  const sesion = localStorage.getItem('accessToken');

  useEffect(() => {
    axios.get('http://127.0.0.1:8000/users/api/')
      .then((response) => {
        setData(response.data);
      })
      .catch((error) => {
        setError("Error al obtener los datos" + error);
      })
      .finally(() => {
        setLoading(false);
      });
  }, []);

  const handleEditar = (item) => {
    setShowForm(true);
    setUserEdit(item);
  };

  const handleSave = () => {
    setShowForm(false);
    setUserEdit(null);
  };

  const handleClose = () => {
    setShowForm(false);
  };

  const handleDelete = (id) => {
    if (!sesion) {
      alert("No estás autenticado.");
      return;
    }

    if (window.confirm("¿Estás seguro de que deseas eliminar este usuario?")) {
      axios
        .delete(`http://127.0.0.1:8000/users/api/${id}/`, {
          headers: {
            Authorization: `Bearer ${sesion}`,
          },
        })
        .then((response) => {
          setData(data.filter((item) => item.id !== id));
          setSuccessMessage("Usuario eliminado con éxito.");
        })
        .catch((error) => {
          if (error.response && error.response.status === 403) {
            setError("No puedes eliminar tu propio usuario.");
          } else {
            setError("Error al eliminar el usuario: " + error.message);
          }
        });
    }
  };

  const indexOfLastUser = currentPage * itemsPerPage;
  const indexOfFirstUser = indexOfLastUser - itemsPerPage;
  const currentUsers = data.slice(indexOfFirstUser, indexOfLastUser);

  const handlePageChange = (pageNumber) => {
    setCurrentPage(pageNumber);
  };

  if (loading) {
    return <div>Cargando...</div>;
  }

  if (error) {
    return <div className="alert alert-danger">{error}</div>;
  }

  const totalPages = Math.ceil(data.length / itemsPerPage);

  return (
    <div>
      <h1>Datos de la API desde Django</h1>
      {successMessage && <div className="alert alert-success">{successMessage}</div>}
      <h2>Usuario: {sesion}</h2>

      {/* Tabla de Usuarios */}
      <table className="table table-striped table-bordered">
        <thead>
          <tr>
            <th>ID</th>
            <th>Nombre</th>
            <th>Apellido</th>
            <th>Control Número</th>
            <th>Edad</th>
            <th>Teléfono</th>
            <th>Correo Electrónico</th>
            <th>Acciones</th>
          </tr>
        </thead>
        <tbody>
          {currentUsers.map((item) => (
            <tr key={item.id}>
              <td>{item.id}</td>
              <td>{item.name}</td>
              <td>{item.surname}</td>
              <td>{item.control_number}</td>
              <td>{item.age}</td>
              <td>{item.tel}</td>
              <td>{item.email}</td>
              
              <td>
                <button
                  onClick={() => handleEditar(item)}
                  className="btn btn-warning"
                >
                  Editar
                </button>
                <button
                  onClick={() => handleDelete(item.id)}
                  className="btn btn-danger"
                >
                  Eliminar
                </button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>

      {showForm && <EditUser userEdit={userEdit} onSave={handleSave} handleClose={handleClose} />}

      {/* Paginación */}
      <nav aria-label="Page navigation">
        <ul className="pagination">
          {[...Array(totalPages)].map((_, index) => (
            <li
              key={index + 1}
              className={`page-item ${currentPage === index + 1 ? "active" : ""}`}
            >
              <button
                className="page-link"
                onClick={() => handlePageChange(index + 1)}
              >
                {index + 1}
              </button>
            </li>
          ))}
        </ul>
      </nav>
    </div>
  );
}

function App(){
  return (
    <Router>
      <Navbar />
      <div className="container mt-4">
        <div className="row">
          <div className="col">
            <AnimatedRoutes />
          </div>
        </div>  
      </div>
    </Router>
  );
}

export default App;