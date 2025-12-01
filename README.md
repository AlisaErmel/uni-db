# 🎓 University Database Application (Python + Flask + MongoDB)

This project is a Python application using **Flask** and **PyMongo** to manage a University database.  
The database tracks students, courses, and grades, supporting full CRUD operations through a web interface.

---

## 📂 Project Structure

- `app.py` – main Flask application  
- `requirements.txt` – Python dependencies  
- `.env` – environment variables (MongoDB connection URI)  
- `db_operations.py` – database operations module  

---

## 🛠️ Prerequisites

- Python 3.12+  
- MongoDB (local installation or MongoDB Atlas)  
- Git  

---

## 📥 Cloning the Repository

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git
cd YOUR_REPO
```

## 🐍 Using a Virtual Environment (Recommended)
### 1. Create a virtual environment:

```bash
python -m venv venv
```

### 2. Activate the virtual environment:

- Windows (PowerShell):

```bash
.\venv\Scripts\Activate.ps1
```

- Windows (cmd):

```bash
.\venv\Scripts\activate.bat
```

- Linux / macOS:

```bash
source venv/bin/activate
```

### 3. Install dependencies:

```bash
pip install -r requirements.txt
```

### 4. Run the Flask app:

```bash
python app.py
```

## 🌐 Installing Dependencies Globally (Optional)

If you do not want to use a virtual environment, you can install dependencies globally:

```bash
pip install -r requirements.txt
```
> **⚠️ WARNING:** Using global installation is not recommended as it may cause conflicts with other Python projects or packages.

## 🔑 Environment Variables
### 1. Create a **.env** file in the project root.

### 2. Add your MongoDB connection string:

```bash
MONGODB_URI=your_mongodb_connection_string
```

The Flask app and PyMongo will read the connection string from this file.

## 💻 Using the Application
1. Open your browser and navigate to: http://127.0.0.1:5000

2. Use the web interface to:

    - Create, read, update, and delete students, courses, and grades

    - Filter or search records

    - View statistics (if implemented)

## 📝Notes
### - The project uses **PyMongo** to interact with **MongoDB**.

### - All *_id* fields in MongoDB must use *ObjectId* when referencing related documents.

### - It is **recommended** to use a virtual environment to avoid dependency conflicts.

## 📦 Requirements File
### All project dependencies are listed in requirements.txt.

- To create or update the file:

```bash
pip freeze > requirements.txt
```

- To install the dependencies from requirements.txt:

```bash
pip install -r requirements.txt
```