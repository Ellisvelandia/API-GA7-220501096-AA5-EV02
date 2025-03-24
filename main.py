from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Optional, List
from uuid import UUID, uuid4


app = FastAPI(
    title="Task Management API",
    description="""
    API RESTful para la gestión de tareas del proyecto formativo.
    
    Características principales:
    * Crear tareas con nombre y descripción
    * Listar todas las tareas
    * Obtener una tarea específica
    * Actualizar tareas existentes
    * Eliminar tareas
    * Documentación automática de la API
    """,
    version="1.0.0",
    docs_url="/documentacion",
    redoc_url="/redoc",
    openapi_tags=[{
        "name": "Tasks",
        "description": "Operaciones con tareas: crear, leer, actualizar y eliminar"
    }, {
        "name": "General",
        "description": "Operaciones generales de la API"
    }]
)


class Task(BaseModel):
    """
    Modelo de datos para representar una tarea
    
    Attributes:
        id (UUID): Identificador único de la tarea
        name (str): Nombre de la tarea
        description (str): Descripción detallada de la tarea
        completed (bool): Estado de completitud de la tarea
    """
    id: Optional[UUID] = None
    name: str = Field(..., description="Nombre de la tarea", example="Implementar API")
    description: Optional[str] = Field(None, description="Descripción de la tarea", example="Crear endpoints REST para el proyecto")
    completed: bool = Field(False, description="Estado de la tarea")


#Lista de tareas para almacenar las tareas creadas por el usuario
tasks = []

@app.get("/", tags=["General"])
def read_root():
    """
    Endpoint de bienvenida
    
    Returns:
        dict: Mensaje de bienvenida
    """
    return {"message": "Welcome to the Task API"}


@app.post("/tasks", response_model=Task, tags=["Tasks"])
def create_task(task: Task):
    """
    Crear una nueva tarea
    
    Args:
        task (Task): Datos de la tarea a crear
        
    Returns:
        Task: Tarea creada con su ID generado
        
    Raises:
        HTTPException: Error de validación si los datos son incorrectos
    """
    task.id = uuid4()
    tasks.append(task)
    return task


@app.get("/tasks", response_model=List[Task], tags=["Tasks"])
def read_tasks():
    """
    Obtener todas las tareas
    
    Returns:
        List[Task]: Lista de todas las tareas almacenadas
    """
    return tasks


@app.get("/tasks/{task_id}", response_model=Task, tags=["Tasks"])
def read_task(task_id: UUID):
    """
    Obtener una tarea específica por su ID
    
    Args:
        task_id (UUID): ID de la tarea a buscar
        
    Returns:
        Task: Tarea encontrada
        
    Raises:
        HTTPException: 404 si la tarea no existe
    """
    for task in tasks:
        if task.id == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")


@app.put("/tasks/{task_id}", response_model=Task, tags=["Tasks"])
def update_task(task_id: UUID, task_update: Task):
    """
    Actualizar una tarea existente
    
    Args:
        task_id (UUID): ID de la tarea a actualizar
        task_update (Task): Nuevos datos de la tarea
        
    Returns:
        Task: Tarea actualizada
        
    Raises:
        HTTPException: 404 si la tarea no existe
    """
    for idx, task in enumerate(tasks):
        if task.id == task_id:
            update_task = task.copy(update=task_update.dict(exclude_unset=True))
            tasks[idx] = update_task
            return update_task
    raise HTTPException(status_code=404, detail="Task not found")


@app.delete("/tasks/{task_id}", response_model=Task, tags=["Tasks"])
def delete_task(task_id: UUID):
    """
    Eliminar una tarea
    
    Args:
        task_id (UUID): ID de la tarea a eliminar
        
    Returns:
        Task: Tarea eliminada
        
    Raises:
        HTTPException: 404 si la tarea no existe
    """
    for idx, task in enumerate(tasks):
        if task.id == task_id:
            return tasks.pop(idx)
    raise HTTPException(status_code=404, detail="Task not found")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )
