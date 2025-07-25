# Skin Cancer Detection Backend

A Django-based backend application that allows users to upload images of skin lesions and get predictions indicating whether the lesion is **Benign** or **Malignant** using a pre-trained **ResNet50** deep learning model.

---

## Features

- User authentication via JWT tokens.
- Upload skin lesion images via the `/api/test/` endpoint.
- Predicts cancer type using fine-tuned ResNet50 model.

---

## Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/Skin-Cancer-Detection.git
cd Skin-Cancer-Detection
```
2. **Create a virtual enviroment**
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```
3. **Install dependecies**
```bash
pip install -r requirements.txt
```
4. **Configure environment varibles**
```bash
# .env
SECRET_KEY=your_django_secret_key_here

# MySQL Database Configuration
DB_ENGINE=django.db.backends.mysql
DB_NAME=your_mysql_databse_name
DB_USER=username
DB_PASSWORD=password
DB_HOST=ip_adress
DB_PORT=port

# Email Settings
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.example.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your_email@example.com
EMAIL_HOST_PASSWORD=your_email_password
DEFAULT_FROM_EMAIL=your_email@example.com

# Django
DEFAULT_AUTO_FIELD=django.db.models.BigAutoField
```
5. **Install dependecies**
```bash
pip install -r requirements.txt
```
6. **Set up the database**
```bash
python manage.py makemigrations
python manage.py migrate
``` 
6. **Create a superuser (optional)**
```bash
python manage.py createsuperuser
```
7. **Run the developmnet server**
```bash
python manage.py runserver
```
## Test it
1. **Authenticate**
```bash
curl -X POST http://127.0.0.1:8000/api/token/ \
  -H "Content-Type: application/json" \
  -d '{"email": "user@example.com", "password": "yourpassword"}'
```
2. **Upload & Predict**:
```bash
curl -X POST http://127.0.0.1:8000/api/test/ \
  -H "Authorization: Bearer <your_token>" \
  -F "image=@/path/to/lesion.jpg"
```






