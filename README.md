# ONLYFLANS

ONLYFLANS es una aplicación web de ventas de postres creada con Python y Django.

### Tecnologías

- Python 3
- Django 5

### Descripción

ONLYFLANS es una plataforma para vender y comprar postres caseros. Los usuarios pueden navegar por una variedad de postres, agregarlos a su carrito de compras y realizar pedidos.

### Características

- Registro e inicio de sesión de usuarios
- Navegación de postres disponibles
- Postres reservaod a usurios registrados

### Instalación y Configuración

#### Requisitos Previos

- Python 3.12.3
- Pip (gestor de paquetes de Python)
- Virtualenv (opcional, pero recomendado)
- Django==5.0.7


#### Pasos de Instalación

1. Clona el repositorio:

   ```bash
   git clone <URL_DEL_REPOSITORIO>
   cd onlyflans
   ```

2. Crea y activa un entorno virtual:

   ```bash
   virtualenv venv
    -m "
   ```

3. Instala las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

4. Configura las variables de entorno en un archivo `.env` (opcional):

   ```env
   DEBUG=True
   SECRET_KEY=your_secret_key
   DATABASE_URL=sqlite:///db.sqlite3
   ```

5. Realiza las migraciones de la base de datos:

   ```bash
   python manage.py makemigrations
   ```

   ```bash
   python manage.py migrate
   ```

6. Crea un superusuario para acceder al panel de administración:

   ```bash
   python manage.py createsuperuser
   ```

7. Inicia el servidor de desarrollo:
   ```bash
   python manage.py runserver
   ```

### Uso

1. Abre tu navegador web y navega a `http://localhost:8000/` para ver la página de inicio.
2. Usa el panel de administración en `http://localhost:8000/admin/` para gestionar el contenido de la aplicación.

### Rutas

- `/` - Página principal
- `/web` - Página de ejemplo de plantilla

### Estructura del Proyecto

Una descripción rápida de la estructura de directorios principal:

```plaintext
onlyflans/
├── manage.py
├── onlyflans/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
├── web/
│   │__init__.py
│   │── admin.py
│   │── apps.py
│   │── forms.py
│   │── models.py
│   │── views.py
│   ├── urls.py
|   ├── templates/
│       ├── about.html
│       ├── base.html
│       ├── contactus.html
│       ├── detalle.html
│       ├── footer.html
│       ├── header.html
│       ├── index.html
│       ├── navbar.html
│       ├── profile_e.html
│       ├── profile_exito.html
│       ├── profile.html
│       ├── register.html
│       ├── success.html
│       ├── welcome.html
|           ├── registration/
│              ├── logger_out.html
│              ├── login.html
|   ├── static/
│      ├── css/styles.css
│      ├── js/index.js
│      ├── img/OnlyFlans.png
├── ...
```

### Integrantes

- Jorge Rodríguez Oliva
  - https://github.com/JorgeRodriguezOliva/onlyflans
- Rubén Mario Ramírez
  - [GitHub](<enlace github>)

### Contribuir

Si deseas contribuir a este proyecto, por favor sigue los siguientes pasos:

1. Haz un fork del repositorio.
2. Crea una rama con tu nueva característica (`git checkout -b feature/nueva-caracteristica`).
3. Haz commit de tus cambios (`git commit -am 'Añadida nueva característica'`).
4. Empuja tu rama (`git push origin feature/nueva-caracteristica`).
5. Abre un Pull Request.

### Licencia

Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.

### Contacto

Si tienes alguna pregunta o sugerencia, no dudes en contactarnos a través de [jrodriguez.oliva@gmail.com].