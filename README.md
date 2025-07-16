# 🏥 Patient Record API (Django REST Framework)

A simple Patient Record CRUD API built with Django and Django REST Framework (DRF).

---

## ✨ Features

- Create, Read, Update, and Delete (CRUD) patient records
- Clean RESTful API structure using Django REST Framework
- Automatically generated endpoints using DRF's router system
- SQLite database for simplicity

---

## 🚀 Getting Started

### 🔧 Prerequisites

- Python 3.x
- Git
- (Optional) Virtual environment tool: `venv`, `virtualenv`, or `pipenv`

### 🛠 Installation

1. **Clone the repo**

```bash
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name
2.Create a virtual environment

bash
Copy
Edit
python -m venv venv
source venv/bin/activate        # macOS/Linux
venv\Scripts\activate           # Windows
3.Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
If you don’t have a requirements.txt, install manually:

bash
Copy
Edit
pip install django djangorestframework
Run migrations

bash
Copy
Edit
python manage.py makemigrations
python manage.py migrate
Run the server

bash
Copy
Edit
python manage.py runserver
📡 API Endpoints
Method	URL	Description
GET	/api/patients/	List all patients
POST	/api/patients/	Create a patient
GET	/api/patients/{id}/	Retrieve a patient
PUT	/api/patients/{id}/	Update a patient
PATCH	/api/patients/{id}/	Partially update
DELETE	/api/patients/{id}/	Delete a patient

Example payload (POST/PUT)
json
Copy
Edit
{
  "name": "John Doe",
  "age": 45,
  "diagnosis": "Influenza"
}
