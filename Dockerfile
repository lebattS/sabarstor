# استخدم صورة Python الرسمية
FROM python:3.10-slim
# تعيين مجلد العمل داخل الحاوية
WORKDIR /app
# نسخ وتثبيت الحزم
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# نسخ باقي ملفات المشروع
COPY . .
# إعداد متغيرات البيئة
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# جمع الملفات الثابتة وتشغيل الترحيلات
RUN python manage.py collectstatic --noinput
RUN python manage.py migrate

# فتح المنفذ
EXPOSE 8000

# الأمر الافتراضي لتشغيل الخادم
CMD ["sh", "-c", "python manage.py migrate && gunicorn sabarstor.wsgi:application --bind 0.0.0.0:8000"]