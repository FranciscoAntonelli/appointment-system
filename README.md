Appointment System

Sistema de gestión de turnos desarrollado como proyecto personal para practicar y demostrar conocimientos de desarrollo backend con Python.

La aplicación permite gestionar clientes, profesionales, horarios de atención y turnos, aplicando validaciones y reglas de negocio.

Tecnologías
Python
FastAPI
PostgreSQL
Docker / Docker Compose
Pytest
psycopg
Pydantic
Funcionalidades
Gestión de clientes
Gestión de profesionales
Configuración de horarios de atención
Creación de turnos
Validación de disponibilidad
Confirmación y cancelación de turnos
Validaciones de datos
Persistencia en PostgreSQL
Notificación al confirmar un turno
Tests automatizados
Arquitectura

El proyecto utiliza una arquitectura por capas para separar responsabilidades:

src/
├── entities/
├── repositories/
├── services/
├── routers/
├── schemas/
├── validators/
├── exceptions/
├── dependencies/
└── main.py

Las responsabilidades principales son:

Routers: reciben las solicitudes HTTP y devuelven las respuestas de la API.
Services: contienen la lógica de negocio.
Repositories: se encargan de la comunicación con PostgreSQL.
Entities: representan las entidades principales del sistema.
Schemas: definen y validan los datos recibidos por la API.
Validators: contienen reglas específicas de validación.
Exceptions: manejan errores propios de la aplicación.
API

La API está desarrollada con FastAPI y permite realizar operaciones sobre:

/clients
/professionals
/appointments

La documentación interactiva está disponible mediante Swagger UI:

http://localhost:8000/docs
Ejecutar el proyecto con Docker
Requisitos
Docker
Docker Compose
1. Clonar el repositorio
git clone <URL_DEL_REPOSITORIO>
cd appointment-system
2. Configurar las variables de entorno

Crear un archivo .env en la raíz del proyecto:

DB_HOST=db
DB_NAME=appointment_system
DB_USER=postgres
DB_PASSWORD=tu_contraseña
3. Levantar los contenedores
docker compose up -d

Esto inicia:

Un contenedor con la API FastAPI.
Un contenedor con PostgreSQL.

La base de datos se inicializa utilizando el script ubicado en:

database/appointment_system.sql
4. Acceder a la API

Una vez levantados los contenedores:

http://localhost:8000/docs
Tests

El proyecto utiliza Pytest para realizar tests automatizados.

Los tests están organizados según la responsabilidad de cada componente:

tests/
├── repositories/
├── services/
├── validators/
└── routers/

Para ejecutarlos dentro del contenedor de la API:

docker compose exec api pytest -v

Los tests de repositories utilizan PostgreSQL para comprobar la interacción con la base de datos.

Objetivo del proyecto

El objetivo principal del proyecto es aplicar conceptos de desarrollo backend como:

Diseño de APIs REST
Arquitectura por capas
Separación de responsabilidades
Validación de datos
Manejo de excepciones
Persistencia de datos
Testing
Dockerización de aplicaciones
Autor

Francisco Antonelli

Desarrollador Backend Junior

GitHub: FranciscoAntonelli
LinkedIn: Francisco Antonelli