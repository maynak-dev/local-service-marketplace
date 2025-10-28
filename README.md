# 🏙️ Local Service Marketplace

A web-based platform built with **Django** that connects **service providers** and **customers** in a local area.  
This system allows users to post, browse, and manage local services easily, such as electricians, plumbers, cleaners, tutors, and more.

---

## 🚀 Features

- 🔐 **User Authentication** – Register, Login, Logout  
- 👩‍🔧 **Service Provider Dashboard** – Add, edit, and manage offered services  
- 🧑‍💼 **Customer Dashboard** – Browse and book available services  
- 🗺️ **Category-Based Filtering** – Find services by location or category  
- 💬 **Booking & Contact System**  
- 📱 **Responsive UI** with Bootstrap  
- 🗃️ **Admin Panel** for complete control of services and users  

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-------------|
| Frontend | HTML, CSS, Bootstrap |
| Backend | Django (Python) |
| Database | SQLite / PostgreSQL |
| Hosting | Vercel |
| Version Control | Git & GitHub |

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/maynak-dev/local-service-marketplace.git
cd local-service-marketplace
```

### 2️⃣ Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate     # for Mac/Linux
venv\Scripts\activate        # for Windows
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Apply Migrations
```bash
python manage.py migrate
```

### 5️⃣ Create Superuser (optional)
```bash
python manage.py createsuperuser
```

### 6️⃣ Run Server Locally
```bash
python manage.py runserver
```

Visit: **http://127.0.0.1:8000/**

---

## 🌐 Deployment on Vercel

This project is configured for **Vercel** using `vercel.json`.

### vercel.json
```json
{
  "version": 2,
  "builds": [
    { "src": "manage.py", "use": "@vercel/python" }
  ],
  "env": {
    "DJANGO_SETTINGS_MODULE": "local_service_marketplace.settings",
    "PYTHONUNBUFFERED": "1"
  },
  "buildCommand": "pip install -r requirements.txt && python manage.py collectstatic --noinput",
  "routes": [
    { "src": "/static/(.*)", "dest": "/static/$1" },
    { "src": "/(.*)", "dest": "manage.py" }
  ]
}
```

### Deployment Steps
1. Push your latest code to GitHub  
2. Go to [Vercel](https://vercel.com) → **Import Project** → select your repo  
3. Wait for build to finish  
4. Visit your live URL 🎉  

---

## 📸 Screenshots

```
![Homepage Screenshot](assets/homepage.png)
![Service Dashboard](assets/dashboard.png)
```

---

## 🧑‍💻 Author

**Maynak Dey**  
📍 B.Tech CSE |  Django Developer  
🔗 [GitHub](https://github.com/maynak-dev) | [LinkedIn](https://linkedin.com/in/maynak-dey)

---

## 📝 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.
