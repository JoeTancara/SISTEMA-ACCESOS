# 🏢 Sistema de Accesos

**Sistema de Accesos** es una aplicación web desarrollada con **Flask** para la gestión y control de accesos a **edificios, pisos y áreas** dentro de una infraestructura. Está diseñado para entornos donde se requiere una administración eficiente y centralizada de espacios físicos.

[![1.jpg](https://i.postimg.cc/MKc4wcHm/1.jpg)](https://postimg.cc/zVrpSGny)

## 🚀 Características

- Gestión completa de **Edificios**, **Pisos** y **Áreas** (CRUD).
- Interfaz moderna con **Bootstrap 4** y **Font Awesome**.
- Uso de **modales** para crear y editar registros sin recargar la página.
- Relaciones jerárquicas entre entidades (Edificios → Pisos → Áreas).
- Selección dinámica de pisos basada en el edificio seleccionado.
- Persistencia de datos con **MySQL**.

## 🗂 Estructura del Proyecto

```
SistemaAccesos/
│
├── app.py                  # Aplicación principal de Flask
├── bd.sql                  # Script para crear las tablas en MySQL
├── requirements.txt        # Dependencias del proyecto
│
├── static/
│   └── css/
│       └── styles.css      # Estilos personalizados
│
└── templates/
    ├── base.html           # Plantilla base con navegación
    ├── edificios.html      # Gestión de edificios
    ├── pisos.html          # Gestión de pisos
    └── areas.html          # Gestión de áreas
```

## 🛠 Instalación

1. **Clona el repositorio** y entra en el directorio del proyecto:

   ```bash
   git clone https://github.com/tuusuario/sistema-accesos.git
   cd sistema-accesos
   ```

2. **Crea un entorno virtual (opcional pero recomendado):**

   ```bash
   python -m venv venv
   source venv/bin/activate 
   ```

3. **Instala las dependencias:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configura la base de datos:**

   - Crea una base de datos en MySQL llamada `accesos`.
   - Ejecuta el archivo `bd.sql` para crear las tablas necesarias.

5. **Configura las credenciales de la base de datos** en `app.py`:
   ```python
   app.config['MYSQL_HOST'] = 'localhost'
   app.config['MYSQL_USER'] = 'tu_usuario'
   app.config['MYSQL_PASSWORD'] = 'tu_contraseña'
   app.config['MYSQL_DB'] = 'accesos'
   ```

6. **Ejecuta la aplicación:**

   ```bash
   python app.py
   ```

7. Accede desde tu navegador a: [http://localhost:5000](http://localhost:5000)

## 🧭 Uso

- Utiliza el menú lateral para navegar entre **Edificios**, **Pisos** y **Áreas**.
- Cada sección permite agregar, editar y eliminar registros.
- Al registrar o editar un área, el listado de pisos se carga dinámicamente según el edificio seleccionado.

## 📦 Dependencias Principales

- [Flask](https://flask.palletsprojects.com/)
- [Flask-MySQLdb](https://github.com/admiralobvious/flask-mysqldb)
- [mysqlclient](https://pypi.org/project/mysqlclient/)
- [Bootstrap 4](https://getbootstrap.com/docs/4.6/getting-started/introduction/) (via CDN)
- [Font Awesome](https://fontawesome.com/) (via CDN)
- [jQuery](https://jquery.com/) (via CDN)

## 📌 Notas

- Este proyecto tiene fines educativos y puede necesitar ajustes para su implementación en entornos productivos (autenticación, validaciones, manejo de errores, etc).

## 👨‍💻 Autor

Desarrollado por **JoeTancara** – [@JoeDev](https://github.com/JoeDev)
