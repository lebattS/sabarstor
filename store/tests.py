from django.test import TestCase
from django.urls import reverse
from .models import Product, Category
from django.core.files.uploadedfile import SimpleUploadedFile

class ProductDisplayTests(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="الكتب", slug="books")
        image = SimpleUploadedFile(name='book_1.jpg', content=b'fake image content', content_type='image/jpeg')
        self.product = Product.objects.create(
            name="رواية الخيميائي",
            slug="the-alchemist-novel",
            description="رواية مشهورة جداً مترجمة.",
            price=13000,
            category=self.category,
            image=image
        )

    def test_product_shows_in_category_page(self):
        """✅ يظهر المنتج في صفحة الفئة"""
        url = reverse('products_by_category', args=[self.category.slug])
        response = self.client.get(url)
        self.assertContains(response, "رواية الخيميائي")

    def test_product_has_image(self):
        """✅ المنتج يحتوي على صورة"""
        self.assertTrue(self.product.image)

    def test_category_link_works(self):
        """✅ رابط الفئة يعمل"""
        url = reverse('products_by_category', args=[self.category.slug])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)


from django.test import TestCase
from django.urls import reverse
from store.models import Product, Category
from django.core.files.uploadedfile import SimpleUploadedFile

class AlchemistProductTests(TestCase):
    def setUp(self):
        # إنشاء فئة
        self.category = Category.objects.create(name="الكتب", slug="books")

        # رفع صورة وهمية تمثل book_1.jpg
        self.image = SimpleUploadedFile(
            name='book_1.jpg',
            content=open('media/product_images/book_1.jpg', 'rb').read(),
            content_type='image/jpeg'
        )

        # إنشاء المنتج
        self.product = Product.objects.create(
            name="رواية الخيميائي",
            slug="TheAlchemistnovel",
            description="رواية شهيرة لباولو كويلو",
            price=1200,
            category=self.category,
            image=self.image
        )

    def test_product_display_on_detail_page(self):
        """✅ يظهر المنتج بشكل صحيح في صفحة التفاصيل"""
        url = reverse('product_detail', args=[self.product.slug])
        response = self.client.get(url)
        self.assertContains(response, self.product.name)
        self.assertContains(response, self.product.description)
        self.assertContains(response, self.product.price)

    def test_product_image_displayed(self):
        """✅ صورة المنتج تظهر في صفحة التفاصيل"""
        url = reverse('product_detail', args=[self.product.slug])
        response = self.client.get(url)
        self.assertContains(response, self.product.image.url)

    def test_add_to_cart_for_product(self):
        """✅ يمكن إضافة المنتج إلى السلة"""
        url = reverse('add_to_cart', args=[self.product.id])
        response = self.client.get(url)
        session = self.client.session
        cart = session.get('cart', {})
        self.assertIn(str(self.product.id), cart)
