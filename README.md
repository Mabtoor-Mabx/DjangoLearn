# DjangoLearn

A simple Django project built with **Function-Based Views (FBV)** to demonstrate core Django features like ORM, Aggregation, Annotation, Pagination, Custom User Model, Model Managers, Signals, and Bootstrap integration.

---

## 🚀 Features

* **Custom User Model** (extends `AbstractUser`)
* **Post model** with custom manager (`popular()` method)
* **Django ORM** queries with Aggregation & Annotation
* **Pagination** for post listings
* **Django Signals** (`post_save` hook on Post)
* **Function-Based Views** (clean and beginner-friendly)
* **Bootstrap 5** styling
* **Post Create + List + Detail Views**

---

## 📂 Project Structure

```
DjangoLearn/
│── DjangoLearn/        # Project settings
│── blog/               # Main app
│   ├── models.py       # CustomUser + Post model
│   ├── managers.py     # Custom manager
│   ├── signals.py      # Signals for Post
│   ├── views.py        # Function-based views
│   ├── urls.py         # App URLs
│   ├── forms.py        # Post form
│   └── templates/blog/ # HTML templates (Bootstrap)
│── manage.py
```

---

## ⚙️ Installation

1. Clone the repo:

   ```bash
   git clone https://github.com/your-username/DjangoLearn.git
   cd DjangoLearn
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate   # macOS/Linux
   venv\Scripts\activate      # Windows
   ```

3. Install dependencies:

   ```bash
   pip install django
   ```

4. Run migrations:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Create superuser (for admin panel):

   ```bash
   python manage.py createsuperuser
   ```

6. Run the server:

   ```bash
   python manage.py runserver
   ```

---

## 📌 Usage

* Visit `http://127.0.0.1:8000/` → View posts (paginated, annotated, aggregated).
* Click **+ Add Post** → Create a new post.
* Visit `http://127.0.0.1:8000/admin/` → Manage posts and users.

---

## 🎨 UI

* Integrated with **Bootstrap 5**
* Responsive navigation bar
* Styled forms, buttons, and list views

---

## 🧩 Tech Stack

* **Backend:** Django 5+
* **Database:** SQLite (default, can switch to PostgreSQL/MySQL)
* **Frontend:** Bootstrap 5

---

## 📖 Learning Outcomes

This project helps you understand:

* How to use Django ORM for queries
* Aggregations and Annotations
* Custom User Models and Managers
* Pagination in function-based views
* Django signals for event handling
* Bootstrap integration for styling

---

## 📜 License

This project is for educational purposes. Free to use and modify.

