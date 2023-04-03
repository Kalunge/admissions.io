# admissions.io

### College Admission Web App
This is a web app for managing college admissions. Users can apply to colleges, view their application status, and update their information.

#### Installation
- Clone the repository to your local machine.
- Create a virtual environment using pipenv.
- Install the dependencies using pipenv install.
- Set environment variables or create a configuration file with the necessary parameters for the app, such - as the database URL and secret key.
#### Usage
- Activate the virtual environment using pipenv shell.
- run your app in your terminal
#### API Endpoints
###### GET /students
- Returns a list of all students in the database.

Response:

```json
[
  {
    "id": 1,
    "name": "John Smith",
    "email": "john.smith@email.com",
    "GPA": 3.8
  },
  {
    "id": 2,
    "name": "Jane Doe",
    "email": "jane.doe@email.com",
    "GPA": 3.6
  },
  ...
]

```
##### POST /students
- Creates a new student in the database.

Request Body:

```json
{
  "name": "Alice Johnson",
  "email": "alice.johnson@email.com",
  "GPA": 3.9
}
Response:

perl
Copy code
{
  "id": 3,
  "name": "Alice Johnson",
  "email": "alice.johnson@email.com",
  "GPA": 3.9
}
```
##### GET /students/:id
- Returns a specific student by ID.

Response:

```json
{
  "id": 1,
  "name": "John Smith",
  "email": "john.smith@email.com",
  "GPA": 3.8
}
```
##### PUT /students/:id
- Updates a specific student by ID.

Request Body:

```json
{
  "GPA": 4.0
}
Response:

perl
Copy code
{
  "id": 1,
  "name": "John Smith",
  "email": "john.smith@email.com",
  "GPA": 4.0
}
```
##### DELETE /students/:id
- Deletes a specific student by ID.

Response:

```json
{
  "message": "Student deleted successfully."
}
```
##### GET /applications
- Returns a list of all admissions applications in the database.

Response:

```json
[  {    "id": 1,    "application_date": "2022-01-01",    "status": "pending",    "student_id": 1,    "college_id": 1  },  {    "id": 2,    "application_date": "2022-01-02",    "status": "accepted",    "student_id": 2,    "college_id": 2  },  ...]
```
##### POST /applications
- Creates a new admissions application in the database.

Request Body:

```json
{
  "application_date": "2022-01-03",
  "status": "pending",
  "student_id": 3,
  "college_id": 1
}
```
Response:

```json
{
  "id": 3,
  "application_date": "2022-01-03",
  "status": "pending",
  "student_id": 3,
  }
  ```