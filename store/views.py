from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Category, Order, OrderItem
from .cart import Cart
from .forms import CheckoutForm
from django.contrib.auth.decorators import login_required

# الصفحة الرئيسية - عرض الفئات فقط
def home(request):
    categories = Category.objects.all()
    products = None  # لا نعرض المنتجات افتراضياً
    return render(request, 'store/home.html', {
        'products': products,
        'categories': categories
    })

# عرض المنتجات حسب الفئة
def products_by_category(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    categories = Category.objects.all()
    return render(request, 'store/home.html', {
        'products': products,
        'categories': categories,
        'selected_category': category
    })

# تفاصيل المنتج
def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'store/product_detail.html', {'product': product})

# عرض محتويات السلة
def cart_detail(request):
    cart = Cart(request)
    return render(request, 'store/cart_detail.html', {'cart': cart})

# إضافة منتج إلى السلة
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart = Cart(request)
    cart.add(product)
    return redirect('cart_detail')

# إزالة منتج من السلة
def remove_from_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart = Cart(request)
    cart.remove(product)
    return redirect('cart_detail')

# زيادة الكمية
def increase_quantity(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart = Cart(request)
    cart.add(product)
    return redirect('cart_detail')

# إنقاص الكمية
def decrease_quantity(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart = Cart(request)
    product_id_str = str(product.id)
    if product_id_str in cart.cart:
        if cart.cart[product_id_str]['quantity'] > 1:
            cart.cart[product_id_str]['quantity'] -= 1
        else:
            del cart.cart[product_id_str]
        cart.save()
    return redirect('cart_detail')

# صفحة الدفع
@login_required(login_url='login')  # عدّل الاسم إذا كان مسار تسجيل الدخول مختلفًا
def checkout(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            order = Order.objects.create(
                user=request.user,
                full_name=form.cleaned_data['full_name'],
                address=form.cleaned_data['address'],
                phone=form.cleaned_data['phone'],
                total_price=cart.get_total_price()
            )
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    quantity=item['quantity'],
                    price=item['price']
                )
            cart.clear()
            return redirect('order_success', order_id=order.id)
    else:
        form = CheckoutForm()
    return render(request, 'store/checkout.html', {'form': form, 'cart': cart})

# صفحة نجاح الطلب
def order_success(request, order_id):
    return render(request, 'store/order_success.html', {'order_id': order_id})
def about(request):
    return render(request, 'store/about.html')
from .forms import ContactForm

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # يمكنك إرسال البريد هنا أو تسجيل البيانات
            return render(request, 'store/contact_success.html', {'name': form.cleaned_data['name']})
    else:
        form = ContactForm()
    return render(request, 'store/templates/contact.html', {'form': form})


# store/views.py
from django.contrib import messages
from .forms import ContactForm

from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "✅ تم إرسال رسالتك بنجاح!")
            return redirect('contact')
    else:
        form = ContactForm()

    for field in form.fields.values():
        field.widget.attrs.update({'class': 'form-control form-control-lg'})

    return render(request, 'contact.html', {'form': form})

import logging
logger = logging.getLogger(__name__)
logger.info("✅ Product list page was viewed.")
logger.error("❌ Something went wrong when retrieving products.")

def home(request):
    logger.info("🏠 Home page viewed.")

def products_by_category(request, category_slug):
    logger.info(f"📂 Category page viewed: {category_slug}")

