# 🌐 ToDo App API
This is the **Django REST Framework** backend for the React-based ToDo List application. It provides a full-featured REST API for managing tasks—adding, updating, deleting, completing, and undoing tasks.

---
## ⚙️ Features

- ✅ Create tasks
- 📝 Read all tasks (pending and completed)
- ✏️ Update task status (mark as complete or undo)
- 🗑️ Delete tasks
- 📱 Minimal UI
---
## 🛠️ Tech Stack

- **Backend Framework**: Django
- **API Layer**: Django REST Framework (DRF)
- **Database**: PostgreSQL

---
## 📁 Project Structure
```
todo-api/ 
├── venv/
├── src/ 
|    └── todo/
|        ├── api/
|        |   └── v1/
|        |       └── tasks/
|        |       |   ├── serializer.py
|        |       |   └── views.py
|        |       |   └── urls.py
|        ├── tasks/
|        ├── todo/
|        |   ├── urls.py
|        |   └── settings.py
|        ├── manage.py
|        ├── r.txt
```      
---
## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/mohd-yaseen-official/todo-api.git
cd todo-api
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
venv\Scripts\activate  # On Windows
# or
source venv/bin/activate  # On macOS/Linux
```

### 3. Install dependencies

```bash
pip install -r r.txt
```

### 4. Create a `.env` file in the root directory and add:

```env
DJANGO_SECRET_KEY=your-secret-key
DJANGO_DEBUG=True-or-False
DB_NAME=your-db-name
DB_USER=your-db-username
DB_PASSWORD=your-db-password
DB_HOST=your-db-host
DB_PORT=your-db-port
```

### 5. Run database migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create a superuser (optional but recommended)

```bash
python manage.py createsuperuser
```

### 7. Start the development server

```bash
python manage.py runserver
```

Visit [http://127.0.0.1:8000](http://127.0.0.1:8000) to view the app.

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

---

## ✨ Credits

Developed with 💙 by [Mohamed Yaseen](https://github.com/mohd-yaseen-official)
