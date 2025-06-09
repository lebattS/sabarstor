
#  SabarStor - Simple E-Commerce Store

*SabarStor* is a modern, Arabic-language e-commerce web application built with Django. It allows users to browse products by category, view detailed product pages, and add products to a shopping cart. Images are uploaded and stored using Cloudinary, and the app is fully responsive and deployed online.

## 🌐 Live Demo

🔗 [https://sabarstor.onrender.com](https://sabarstor.onrender.com)

---

## 🎯 Features

- Arabic RTL interface with modern Bootstrap 5 styling  
- User registration and login system  
- Browse products by category  
- Detailed product pages with image, price, and description  
- Add products to a shopping cart  
- Product images stored via Cloudinary  
- Fully responsive and mobile-friendly  
- Free deployment on Render

---

## 🛠️ Tech Stack

- *Backend:* Django 5.2  
- *Database:* SQLite  
- *Frontend:* HTML, Bootstrap 5 RTL, CSS  
- *Image Hosting:* Cloudinary + django-cloudinary-storage  
- *Deployment:* Render  

---

## ⚙️ Requirements

bash
Python >= 3.10
Django >= 5.2


---

## 🚀 Running the Project Locally

1. *Clone the repository*

bash
git clone https://github.com/lebattS/sabarstor.git
cd sabarstor


2. *Create a virtual environment*

bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\\Scripts\\activate


3. *Install dependencies*

bash
pip install -r requirements.txt


4. *Configure environment variables*

Create a .env file in the root with:

env
SECRET_KEY=your-secret-key
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost

CLOUDINARY_CLOUD_NAME=your-cloud-name
CLOUDINARY_API_KEY=your-api-key
CLOUDINARY_API_SECRET=your-api-secret


5. *Apply migrations and run the development server*

bash
python manage.py migrate
python manage.py runserver


---

## ✅ Testing

Run the test suite to ensure everything is working:

bash
python manage.py test


Tests include:
- Product display on category and detail pages
- Image rendering
- Adding products to cart
- Category URL response

---

## 📂 Project Structure


sabarstor/
│
├── accounts/               # User authentication app
├── store/                  # Store and product catalog
├── templates/              # HTML templates
├── static/                 # CSS, JavaScript, assets
├── media/                  # Media storage (Cloudinary)
├── .env                    # Environment variables
├── requirements.txt        # Python dependencies
├── manage.py
└── README.md


---

## 📝 License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).  
Feel free to use, modify, and distribute with attribution.

---

## 💡 Credits

- Developed by: *Lebatt Sabar*  
- Faculty of РТФ - UrFU
- Design inspiration: Bootstrap RTL  
- Deployment: Render  
- Special thanks to the Django and Cloudinary communities

---

## 📬 Contact

Have questions or suggestions?

- GitHub: [lebattS](https://github.com/lebattS)
- Email: 19237@isms.esp.mr
"""

