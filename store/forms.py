from django import forms

class CheckoutForm(forms.Form):
    full_name = forms.CharField(label='الاسم الكامل', max_length=100)
    address = forms.CharField(label='العنوان', widget=forms.Textarea)
    phone = forms.CharField(label='رقم الهاتف', max_length=20)

from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label='الاسم')
    email = forms.EmailField(label='البريد الإلكتروني')
    message = forms.CharField(widget=forms.Textarea, label='الرسالة')

# store/forms.py

from django import forms
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']
