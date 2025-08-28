from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import menu, item_detail, item_3D_detail

app_name = 'menu'
urlpatterns =[
    path('', menu, name='menu'),
    path('item/<int:id>/', item_detail, name='item_detail'),
    path('item_3D/<int:id>/', item_3D_detail, name='item_3D_detail'),
    # Add other menu-related URLs here if needed
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
