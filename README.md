````markdown
# Curriculum Data API

An API developed in Python with FastAPI and SQLAlchemy to manage personal information for curriculum purposes.

## Description

This API connects to a database storing information about various individuals, allowing clients (like HTML/JS web applications) to make requests to retrieve data and assemble personalized resumes. It's ideal for integration with portfolio websites, HR systems, and other applications.

---

## Features

* Complete CRUD for individuals and their personal data
* Custom queries to retrieve information and build resumes
* Simple integration with frontends via HTTP requests
* Uses SQLAlchemy for database abstraction
* Automatic documentation via Swagger UI

---

## Technologies

* Python 3.x
* FastAPI
* SQLAlchemy ORM
* Pydantic (validation schemas)
* Uvicorn (ASGI server)

---

## Installation

1.  Clone the repository:

    ```bash
    git clone [https://github.com/blink992/curriculum-data-api.git](https://github.com/blink992/curriculum-data-api.git)
    cd curriculum_data_api
    ```

2.  Create and activate a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate   # Linux/Mac
    venv\Scripts\activate      # Windows
    ```

3.  Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4.  **Database configuration:**
    This project expects a **database** to be running at an accessible address.

    * Create a `.env` file in the project root (if necessary) and define your database URL:
        ```
        DATABASE_URL=http://localhost:8000/database
        ```
    * Ensure the database is running and accessible.

---

## Usage

1.  Start the server:

    ```bash
    uvicorn main:app --reload
    ```

2.  Make requests to the endpoints to create, read, update, and delete individual's information.

---

## License

This project is licensed under the **MIT** license. See the [LICENSE](./LICENSE.md) file for more details.

---

## Contact

Pedro Arthur Gregorio Abreu - [pedro.agb2004@gmail.com](mailto:pedro.agb2004@gmail.com)

GitHub Link: [https://github.com/meiyo-aru/curriculum-data-api](https://github.com/meiyo-aru/curriculum-data-api)

---
