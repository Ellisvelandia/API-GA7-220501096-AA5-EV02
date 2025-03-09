# Task Management API

A RESTful API built with FastAPI for managing tasks. This API allows you to create, read, update, and delete tasks.

## Features

- Create new tasks
- List all tasks
- Get task by ID
- Update existing tasks
- Delete tasks
- Automatic UUID generation for task IDs

## API Endpoints

### Base URL
```
http://127.0.0.1:8000
```

### Endpoints

#### GET /
- Description: Welcome message
- Response: `{"message": "Welcome to the Task API"}`

#### POST /tasks
- Description: Create a new task
- Request Body:
```json
{
    "name": "Task name",
    "description": "Task description",
    "completed": false
}
```
- Response: Created task object with generated ID

#### GET /tasks
- Description: Get all tasks
- Response: Array of task objects

#### GET /tasks/{task_id}
- Description: Get a specific task by ID
- Parameters: task_id (UUID)
- Response: Task object
- Error: 404 if task not found

#### PUT /tasks/{task_id}
- Description: Update a task
- Parameters: task_id (UUID)
- Request Body:
```json
{
    "name": "Updated name",
    "description": "Updated description",
    "completed": true
}
```
- Response: Updated task object
- Error: 404 if task not found

#### DELETE /tasks/{task_id}
- Description: Delete a task
- Parameters: task_id (UUID)
- Response: Deleted task object
- Error: 404 if task not found

## Task Model

```python
{
    "id": "uuid-string",
    "name": "string",
    "description": "string",
    "completed": boolean
}
```

## Running the API

1. Install dependencies:
```bash
pip install fastapi uvicorn
```

2. Run the server:
```bash
python main.py
```
or
```bash
uvicorn main:app --reload
```

3. Access the API documentation:
- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

## Testing with Thunder Client (VS Code)

1. Install Thunder Client extension in VS Code
2. Create new request
3. Use the endpoints above to test the API
4. Set Content-Type header to `application/json` for POST and PUT requests

## Error Handling

- 404: Resource not found
- 422: Validation error (invalid request body)
- 500: Internal server error

## Notes

- All task IDs are UUIDs generated automatically
- The API uses an in-memory list to store tasks (data is lost when server restarts)
- CORS is not enabled by default
