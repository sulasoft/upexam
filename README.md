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
- **POST /users/:** Create a new user.
- **GET /users/<int:pk>/:** Retrieve details of a specific user.
- **PUT /users/<int:pk>/:** Update details of a specific user.
- **DELETE /users/<int:pk>/:** Delete a specific user.

### Profile Endpoints:

- **GET /profiles/:** Retrieve a list of profiles.
- **POST /profiles/:** Create a new profile.
- **GET /profiles/<int:pk>/:** Retrieve details of a specific profile.
- **PUT /profiles/<int:pk>/:** Update details of a specific profile.
- **DELETE /profiles/<int:pk>/:** Delete a specific profile.

## Notes

- The API documentation is available at the root path [http://localhost:8000/](http://localhost:8000/).
- Use the provided requirements file for dependencies.

Feel free to customize the content further to meet your specific needs.
