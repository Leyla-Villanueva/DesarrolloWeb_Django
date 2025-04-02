//WIP
import React, { useState, useEffect } from "react";
import axios from "axios";

const CustomUserForm = () => {
    const [formFields, setFormFields] = useState({});
    const [formData, setFormData] = useState({
        email: "",
        password: "",
        name: "",
        surname: "",
        control_number: "",
        age: "",
        tel: "",
    });

    useEffect(() => {
        axios
            .get("http://127.0.0.1:8000/users/form/")
            .then((response) => {
                console.log(response.data);
                setFormFields(response.data);
            })
            .catch((error) => console.error("Error al obtener los datos", error));
    }, []);

    const handleInputChange = (event) => {
        const { name, value } = event.target;
        setFormData((prevData) => ({
            ...prevData,
            [name]: value || "",
        }));
    };

    const handleSubmit = (event) => {
        event.preventDefault();
        axios
            .post("http://127.0.0.1:8000/users/form/", JSON.stringify(formData), {
                headers: { "Content-Type": "application/json" },
            })
            .then((response) => {
                alert(response.data.message);
            })
            .catch((error) => {
                alert("Hubo un error al crear el usuario.");
                console.error("Error al enviar el formulario", error);
            });
    };

    return (
        <div>
            <h1>Nuevo Usuario</h1>
            <form onSubmit={handleSubmit}>
                {formFields &&
                    Object.entries(formFields).map(([field, fieldData]) => {
                        const { label, input, type } = fieldData;
                        return (
                            <div key={field}>
                                <label htmlFor={field}>{label}</label>
                                <input
                                    {...input}
                                    value={formData[field] || ""}
                                    onChange={handleInputChange}
                                    name={field}
                                    type={type || "text"}
                                />
                                {field === "password" && (
                                    <div>
                                        <p>Al menos un número.</p>
                                        <p>Al menos una letra mayúscula.</p>
                                        <p>Al menos un carácter especial (!#$%&?).</p>
                                        <p>Mínimo de 8 caracteres en total.</p>
                                    </div>
                                )}
                                <br />
                            </div>
                        );
                    })}
                <button type="submit">Enviar</button>
            </form>
        </div>
    );
};

export default CustomUserForm;
