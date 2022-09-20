# webapp_be-c3MisionTIC
Backend para la aplicación web desarrollada en el marco del ciclo 3 del programa de Misión TIC
### Tecnologías:  
- Python
- Django REST Framework
- Base de datos Postgres
---

## Archivo de configuración
En la carpeta _HospitalizacionEnCasa_ crear el archivo `settings.ini` con la siguiente estructura (reemplazar los interrogantes por la información particular):  
```
[settings]
DEBUG=True       # False cuando se despliegue en producción
SECRET_KEY=???   # Clave secreta generada por el framework
ALLOWED_HOSTS=localhost, 127.0.0.1, ???

DB_HOST=???      # url del servidor de bases de datos
DB_PORT=???      # puerto asociado al servidor de bases de datos
DB_NAME=???      # Nombre de la base de datos en el servidor
DB_USER=???      # Usuario de la base de datos
DB_PASSWORD=???  # Contraseña para el ususario de la base de datos
```
---

### Notas
Para verificar las librerias desactualizadas en el entorno virtual usar `pip list --outdated`, y para actualizarlas a la última versión `pip install -U package_name`.  
Para actualizar el *listado* de librerias instaladas en el entorno virtual usar `pip freeze > requirements.txt`.