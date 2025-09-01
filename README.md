# 🏆 Gold Gallery Management App

A Django-based management system for a gold gallery.  
This app provides **real-time gold price tracking**, **profit calculations**, **customer management**, and more.  
Built with **PostgreSQL**, **Django REST Framework (DRF)**, and **JWT authentication**.

---

## ✨ Features

- 📈 **Real-time Gold Price**
  - Fetches the latest gold price via an external API.
  - Displays live price updates inside the app.

- 💰 **Product Final Price Calculation**
  - Automatically calculates the selling price of gold products based on the current gold rate and making charges.

- 📊 **Profit Tracking**
  - Calculates seller’s profit by filtering transactions within a date range.
  - Tracks how much gold (in grams) has been added or sold = profit.

- 👥 **Customer Management**
  - Keeps a list of customers with purchase history.
  - Identifies **most loyal customers** (based on number/volume of purchases).

- 🗄 **Database**
  - Uses **PostgreSQL** as the primary database.

- 🔒 **Authentication**
  - Implements **JWT (JSON Web Token)** for secure login and API access.

- 🌐 **RESTful API**
  - All views are **class-based views (CBV)** using Django REST Framework.
  - Easy integration with frontend or mobile apps.

---

## 🛠️ Tech Stack

- **Backend:** Django, Django REST Framework (DRF)
- **Database:** PostgreSQL
- **Auth:** JWT (SimpleJWT or djangorestframework-simplejwt)
- **API:** Real-time Gold Price API (configurable)
- **Deployment Ready:** Can be run with Docker / Gunicorn / Nginx (optional)

---

## ⚙️ Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/gold-gallery-management.git
   cd gold-gallery-management
