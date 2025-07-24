# Skin Cancer Detection Backend

A Django-based backend application that allows users to upload images of skin lesions and get predictions indicating whether the lesion is **Benign** or **Malignant** using a pre-trained **ResNet50** deep learning model.

---

## Features

- User authentication via JWT tokens.
- Upload skin lesion images via the `/api/test/` endpoint.
- Predicts cancer type using fine-tuned ResNet50 model.
---


---

## Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/skin-cancer-backend.git
cd skin-cancer-backend
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

# Email Settings
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your_email@example.com
EMAIL_HOST_PASSWORD=your_email_password
DEFAULT_FROM_EMAIL=your_email@example.com

# Django
DEFAULT_AUTO_FIELD=django.db.models.BigAutoField
```






