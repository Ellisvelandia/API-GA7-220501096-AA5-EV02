# API de Gestión de Tareas

API RESTful desarrollada con FastAPI para la gestión de tareas del proyecto formativo.

## Características

- CRUD completo para tareas
- Documentación automática con Swagger UI y ReDoc
- Validación de datos con Pydantic
- Identificadores únicos UUID
- Variables de entorno para personalizar el servidor

## Instalación

1. Clonar el repositorio:
```bash
git clone [URL_DEL_REPOSITORIO]
cd api
```

2. Crear y activar un entorno virtual (opcional pero recomendado):
```bash
python -m venv venv
# En Windows:
.\venv\Scripts\activate
# En Linux/MacOS:
source venv/bin/activate
```

3. Instalar dependencias:
```bash
pip install -r requirements.txt
```

4. Ejecutar el servidor:
```bash
# Método 1: Usando uvicorn directamente
uvicorn main:app --reload

# Método 2: Ejecutando el archivo main.py
python main.py
```

El servidor estará disponible en http://localhost:8000

## Documentación

Acceder a la documentación interactiva:
- Swagger UI: http://localhost:8000/documentacion
- ReDoc: http://localhost:8000/redoc

## Endpoints

- `GET /`: Mensaje de bienvenida
- `GET /tasks`: Listar todas las tareas
- `POST /tasks`: Crear nueva tarea
- `GET /tasks/{task_id}`: Obtener tarea específica
- `PUT /tasks/{task_id}`: Actualizar tarea
- `DELETE /tasks/{task_id}`: Eliminar tarea
