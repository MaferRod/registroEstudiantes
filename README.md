# Student Registration App

Aplicación para el registro de estudiantes, con backend en Flask y frontend en Django. Permite crear, ver, actualizar y eliminar estudiantes mediante un API REST y una interfaz web.

---

## Tecnologías

- Python 3.11
- Flask
- Django 5.0
- MySQL (o SQLite si prefieres)
- HTML, CSS
- `requests` para integración
- `unittest` y `unittest.mock` para testing


## Instalación

1. Clonar repositorio:

```bash
git clone  https://github.com/MaferRod/registroEstudiantes.git
cd registroEstudiantes
```
2. Crear entorno virtual:
```bash
Crea el entorno virtual (llamado 'venv')
python -m venv venv
```
Activa el entorno virtual:
```bash
Windows: 	bash\venv\Scripts\activate
Linux/macOS:	bashsource venv/bin/activate
```
3. Instalar dependencias:
```bash
   pip install -r requirements.txt
```
## Instalacion de la base de datos
- Crear base de datos
```bash
CREATE DATABASE students_db;
```
- Usar la base de datos
```bash
USE students_db;
```
- Crear tabla de estudiantes
```bash
CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    age INT NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE
);
```
## Uso
### Ejecutar backend (Flask)
```bash
cd flask_backend
venv\Scripts\activate
python routes.py
```
Servidor: http://127.0.0.1:5000

### Ejecutar frontend (Django)
```bash
cd django_frontend
venv\Scripts\activate
python manage.py runserver
```

Servidor: http://127.0.0.1:8000

# Testing
### Backend
```bash
cd flask_backend
python -m unittest discover -s test -p "*.py"
```
### Frontend
```bash
cd django_frontend
python manage.py test students
```
