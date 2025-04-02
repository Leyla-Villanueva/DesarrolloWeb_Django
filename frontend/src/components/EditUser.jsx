import { useState, useEffect } from 'react';
import axios from 'axios';

import { axiosWithAuth } from './../services/authService';

function EditUser({ userEdit, onSave, handleClose }) {
  const [name, setName] = useState("");
  const [surname, setSurname] = useState("");
  const [control_number, setControlNumber] = useState("");
  const [age, setAge] = useState("");
  const [tel, setTel] = useState("");
  
  const [loading, setLoading] = useState(true);
  const sesion = localStorage.getItem('accessToken');

  // Cuando el usuario a editar cambia, actualizamos los estados
  useEffect(() => {
    if (userEdit) {
      setName(userEdit.name);
      setSurname(userEdit.surname);
      setControlNumber(userEdit.control_number);
      setAge(userEdit.age);
      setTel(userEdit.tel);
      setLoading(false);  // Ya no estamos cargando el usuario
    }
  }, [userEdit]);

  // Manejo del envío del formulario de edición
  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!name || !surname || !control_number || !age || !tel) {
      alert("Por favor, completa todos los campos.");
      return;
    }
  
    const data = { 
      name, 
      surname, 
      control_number, 
      age, 
      tel,
      email: userEdit.email,  // Incluye el email si es necesario
      password: userEdit.password,  // Si el backend requiere password, incluirlo también
    };
  
    try {
      await axiosWithAuth({
        method: 'put',
        url: `http://127.0.0.1:8000/users/api/${userEdit.id}/`,
        data: data,
      });
      alert("Usuario editado correctamente");
      onSave();  // Llama la función para refrescar el estado y cerrar el modal
    } catch (error) {
      if (error.response) {
        console.error('Error de API:', error.response.data);
        alert(`Error al editar el usuario: ${error.response.data.detail || error.message}`);
      } else {
        console.error('Error al hacer la solicitud:', error.message);
        alert("Error al editar el usuario.");
      }
    }
  
    handleClose();  // Cierra el modal después de guardar
  };
  

  if (loading) return <div>Cargando...</div>;

  return (
    <div className="modal fade show" style={{ display: 'block', backgroundColor: 'rgba(0, 0, 0, 0.5)' }}>
      <div className="modal-dialog">
        <div className="modal-content">
          <div className="modal-header">
            <h2>Editar Usuario</h2>
          </div>
          <form onSubmit={handleSubmit}>
            <div className="modal-body">
              {/* Campo Nombre */}
              <div className="form-group">
                <label><b>Nombre</b></label>
                <input
                  type="text"
                  name="name"
                  value={name}
                  onChange={(e) => setName(e.target.value)}
                  className="form-control"
                />
              </div>

              {/* Campo Apellido */}
              <div className="form-group">
                <label><b>Apellido</b></label>
                <input
                  type="text"
                  name="surname"
                  value={surname}
                  onChange={(e) => setSurname(e.target.value)}
                  className="form-control"
                />
              </div>

              {/* Campo Control Número */}
              <div className="form-group">
                <label><b>Control Número</b></label>
                <input
                  type="text"
                  name="control_number"
                  value={control_number}
                  onChange={(e) => setControlNumber(e.target.value)}
                  className="form-control"
                />
              </div>

              {/* Campo Edad */}
              <div className="form-group">
                <label><b>Edad</b></label>
                <input
                  type="number"
                  name="age"
                  value={age}
                  onChange={(e) => setAge(e.target.value)}
                  className="form-control"
                />
              </div>

              {/* Campo Teléfono */}
              <div className="form-group">
                <label><b>Teléfono</b></label>
                <input
                  type="text"
                  name="tel"
                  value={tel}
                  onChange={(e) => setTel(e.target.value)}
                  className="form-control"
                />
              </div>
            </div>

            {/* Botones de acción */}
            <div className="modal-footer">
              <button
                type="button"
                className="btn btn-secondary"
                onClick={handleClose}
              >
                Cancelar
              </button>
              <button
                type="submit"
                className="btn btn-primary"
                disabled={!name || !surname || !control_number || !age || !tel}
              >
                Guardar cambios
              </button>
            </div>
          </form>
        </div>
      </div>
    </div>
  );
}

export default EditUser;
