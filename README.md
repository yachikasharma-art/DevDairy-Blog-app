# ✍️ DevDiary - A Django Blog Application

![License](https://img.shields.io/badge/License-MIT-purple.svg)
![Python](https://img.shields.io/badge/Python-3.14-blue.svg)
![Django](https://img.shields.io/badge/Django-6.0-green.svg)

> *Where ideas come to life...* — A full-featured blog platform built with Django and Bootstrap.

---

## 🚀 Features

- 🔐 User Registration, Login & Logout
- ✍️ Create blog posts with images
- 📂 Category filtering (Nature, Health, Tech)
- 🔍 Search functionality
- 📱 Fully responsive design with Bootstrap 5
- 🚫 "No results" page for empty searches
- 🛡️ Login-protected post creation

---

## 🛠️ Tech Stack

| Technology | Version |
|------------|---------|
| Python | 3.14 |
| Django | 6.0.5 |
| SQLite | Default |
| Bootstrap | 5.3 |
| Pillow | Latest |

---

## 📸 Screenshots

### Home Page
![Home Page](assets/webhome%20page.png)

### Search Result
![Search Result](assets/result%20after%20searching%20heart.png)

### No Results Found
![No Results](assets/when%20topic%20is%20not%20available.png)

---

## 🎥 Demo

> Watch the demo video: [assets/demo.mp4](assets/demo.mp4)

---

## ⚙️ Setup Instructions

### Prerequisites

- Python 3.x installed
- Git installed

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/yachikadev/DevDairy-Blog-app.git
cd DevDairy-Blog-app
```

2. **Create virtual environment**
```bash
python -m venv venv
venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Run migrations**
```bash
python manage.py migrate
```

5. **Create superuser (for admin)**
```bash
python manage.py createsuperuser
```

6. **Run the server**
```bash
python manage.py runserver
```

7. **Open in browser**

http://127.0.0.1:8000

---

## 📁 Project Structure

```
DevDairy-Blog-app/
├── mysite/
│   ├── settings.py
│   ├── urls.py
├── blog/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── admin.py
│   └── templates/
│       └── blog/
│           ├── base.html
│           ├── post_list.html
│           ├── details.html
│           ├── add_post.html
│           ├── login.html
│           └── register.html
├── assets/
│   ├── webhome page.png
│   ├── result after searching heart.png
│   ├── when topic is not available.png
│   └── demo.mp4
├── requirements.txt
└── README.md
```

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👩‍💻 Author

**Yachika Sharma**
- GitHub: [@yachikadev](https://github.com/yachikadev)
