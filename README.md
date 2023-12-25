# UpExam Django API

This is a Django REST Framework (DRF) API project that manages user profiles.

## Getting Started

1. **Clone this repository:**

    ```bash
    git clone https://github.com/sulasoft/upexam.git
    ```

2. **Navigate to the project directory:**

    ```bash
    cd upexam
    ```

3. **Create a virtual environment and activate it:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

4. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

5. **Create migrations:**

    ```bash
    python manage.py makemigrations
    ```

6. **Apply migrations:**

    ```bash
    python manage.py migrate
    ```

7. **Run the development server:**

    ```bash
    python manage.py runserver
    ```

8. **Access the API documentation at [http://localhost:8000/](http://localhost:8000/).**

## API Endpoints

### User Endpoints:

- **GET /users/:** Retrieve a list of users.
  ```bash
  curl http://localhost:8000/users/
  ```
  
- **POST /users/:** Create a new user.
    ```bash
    curl -X POST http://localhost:8000/users/ -H "Content-Type: application/json" -d 
    '{   
        "email": "johnn_updated@example.com"
    }'
    ```

- **GET /users/<int:pk>/:** Retrieve details of a specific user.
    ```bash
    curl http://localhost:8000/users/1/
    ```

- **PUT /users/<int:pk>/:** Update details of a specific user.
    ```bash
    curl -X PUT http://localhost:8000/users/3/ -H "Content-Type: application/json" -d 
    '{  
        "favorite_profiles": [2,3]
    }'
    ```

- **DELETE /users/<int:pk>/:** Delete a specific user.
    ```bash
    curl -X DELETE http://localhost:8000/users/1/
    ```

### Profile Endpoints:

- **GET /profiles/:** Retrieve a list of profiles.
    ```bash
    curl http://localhost:8000/profiles/
    ```

- **POST /profiles/:** Create a new profile.
    ```bash
        curl -X POST http://localhost:8000/profiles/ -H "Content-Type: application/json" -d
        '{
            "name": "Profile Example",
            "description": "This is an example", "user": 2
        }'
    ```

- **GET /profiles/<int:pk>/:** Retrieve details of a specific profile.
    ```bash
        curl http://localhost:8000/profiles/1/
    ```

- **PUT /profiles/<int:pk>/:** Update details of a specific profile.
    ```bash
        curl -X PUT http://localhost:8000/profiles/3/ -H "Content-Type: application/json" -d 
        '{  
            "name": "Updated Profile",
            "description": "Updated description"
        }'
    ```

- **DELETE /profiles/<int:pk>/:** Delete a specific profile.
    ```bash
        curl -X DELETE http://localhost:8000/profiles/1/
    ```
## Notes

- The API documentation is available at the root path [http://localhost:8000/](http://localhost:8000/).

- Use the provided requirements file for dependencies.

- Use the provided requirements file for dependencies.

