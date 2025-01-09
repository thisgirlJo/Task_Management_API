Capstone Project: Task Management API

The goal of this project is to design and implement a Task Management API using Django and Django REST Framework.
This API will allow users to manage their tasks by creating, updating, deleting, and marking tasks as complete or incomplete.

API Endpoints:
HTTP        Method_Endpoint                 Description
POST        /register/                      User registration
POST	    /login/                         User login (get tokens)
GET         /users/                         List all tasks under authenticated user
GET         /tasks/                         List all tasks
POST	    /tasks/                         Create a new task
GET         /tasks/<id>/	                Retrieve a specific task
PUT/PATCH	/tasks/<id>/	                Update a specific task
DELETE	    /tasks/<id>/	                Delete a specific task
PATCH	    /tasks/<id>/mark_complete/	    Mark a task as complete
PATCH	    /tasks/<id>/mark_incomplete/	Mark a task as incomplete