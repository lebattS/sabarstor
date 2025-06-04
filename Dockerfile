# استخدم صورة Python الرسمية
FROM python:3.10-slim

# تعيين مجلد العمل داخل الحاوية
WORKDIR /app

# نسخ الملفات المطلوبة
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --upgrade pip
# نسخ باقي ملفات المشروع
COPY . .

# إعداد متغير البيئة
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# تشغيل التهيئة وجمع الملفات الثابتة
RUN pip install django-cloudinary-storage cloudinary

RUN python manage.py collectstatic --noinput
RUN python manage.py migrate

# فتح المنفذ 8000
EXPOSE 8000

# الأمر الافتراضي لتشغيل الخادم
CMD ["gunicorn", "sabarstor.wsgi:application", "--bind", "0.0.0.0:8000"]

