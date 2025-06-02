from django.contrib import admin
from django.urls import path, include
from accounts.views import CustomLoginView, CustomLogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('accounts/', include('accounts.urls')),
    path('', include('store.urls')),
]

# ✅ لعرض الصور أثناء التطوير
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
