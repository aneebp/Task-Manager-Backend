# Task Manager Application - Backend (Django)

This is the backend of the **Task Manager Application**, built using **Django** and **Django REST Framework**. It provides APIs for task management (CRUD operations) and handles user authentication via **JWT**.

## Features

- User Registration and JWT Authentication
- **Task Management:** Create, view, update, delete tasks
- **Task Filtering::** Filter tasks by completion status (completed/pending)
- **Task Search:** Search tasks by title
- **Pagination:** Paginate tasks to improve performance for large datasets

## Setup Instructions

### 1. Clone the Repository
```bash
git clone <repository_url>
cd <repository_directory>
```

### 2. Create a Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Apply Migrations
```bash
python manage.py migrate
```

### 5. Run the Server
```bash
python manage.py runserver
```

## API Endpoints


- **Tasks**: 
  - `GET /api/tasks/` - List all tasks
  - `POST /api/tasks/` - Create a new task
  
- **Task Detail**: 
  - `GET /api/tasks/<id>/` - Retrieve a specific task
  - `PUT /api/tasks/<id>/` - Update a task
  - `DELETE /api/tasks/<id>/` - Delete a task

- **User Registration**: 
  - `POST /api/register/` - Register a new user

- **User Login**: 
  - `POST /api/login/` - Log in and get JWT tokens

- **Token Refresh**: 
  - `POST /api/token/refresh/` - Refresh the JWT access token



## Additional Information

### CORS
The app uses **CORS** to allow cross-origin requests from the frontend (React). By default, all origins are allowed in development. This can be modified in `settings.py` under the `CORS_ALLOW_ALL_ORIGINS` setting.

### JWT Authentication
The app uses **JWT (JSON Web Tokens)** for authentication. Users must log in to obtain an access token, which is required to interact with the task management endpoints.


