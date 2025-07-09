# Basic FastAPI CRUD APP

Here I have a created a simple FastAPI based CRUD app where I am dealing with student records.<br>
I am managing the students records by creating a new student record, getting any student record from their student id, updating any student record and deleting a student record.

## Project Structure

Exercise_2_FastAPI_CRUD_APP/<br>
├── pycache/<br>
├── main.py<br>
├── notes.md<br>
├── requirements.txt<br>
├── README.md<br>

## WorkFlow

I have created four different endpoints named as @app.post(), @app.get(), @app.put(), @app.delete()<br>
in order to create a new student record, get any student record, update any student record and delete<br>
any student record in main.py.

## Setup Instructions

1. Clone the repository

    `git clone https://github.com/saimanasreen001/Exercise_2_FastAPI_CRUD_APP.git`<br>
    `cd Exercise_2_FastAPI_CRUD_APP`

2. Create a python virtual environment and activate it.

    `python -m venv venv`<br>
    `source bin/venv/activate`

3. Install the required dependencies

    `pip install -r requirements.txt`

4. Run the app

    `uvicorn main:app --reload`<br>
    Open the URL `http://127.0.0.1:8000/docs` to access the Swagger UI.


