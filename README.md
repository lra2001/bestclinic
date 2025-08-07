# Best Clinic
A web platform where patients can register, schedule appointments with doctors, and communicate via messages. Admins or doctors can manage appointments and patient data.

---

## Project Setup

### 1. Set Up the Environment
- Initialize a virtual environment:
```bash
python -m venv venv
```
- Activate the virtual environment on Windows:
```bash
venv\Scripts\activate
```
- Install Django:
```bash
python -m pip install Django
```
- Install Gunicorn:
```bash
python -m pip install gunicorn
```
- Update pip:
```bash
python.exe -m pip install --upgrade pip
```
- Create requirements file
```bash
pip freeze > requirements.txt
```

### 2. Start Project
  - Create project:
  ```bash
  django-admin startproject bestclinic /Workspace/bestclinic
  ```
  <!-- This command creates the required folder/files for the project-->
  - Run local development server:
  ```bash
  python manage.py runserver
  ```

### 3. Start App
  - Create App:
  ```bash
  python manage.py startapp bestclinic_app
  ```
  <!-- This command creates the required folder/files for the app -->

## Documentation
[How to install Django on Windows](https://docs.djangoproject.com/en/5.2/howto/windows/)
[Python.gitignore](https://github.com/github/gitignore/blob/main/Python.gitignore)
[VisualStudioCode.gitignore](https://github.com/github/gitignore/blob/main/Global/VisualStudioCode.gitignore)