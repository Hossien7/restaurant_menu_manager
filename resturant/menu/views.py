from django.shortcuts import render, get_object_or_404
from .models import Category
from .models import MenuItem


def menu(request):
    categories = Category.objects.filter(is_active=True)
    return render(request, 'menu/menu.html', {'categories': categories})


def item_detail(request, id):
    item = get_object_or_404(MenuItem, id=id)
    return render(request, 'menu/item_detail.html', {'item': item})


def item_3D_detail(request, id):
    item = get_object_or_404(MenuItem, id=id)
    return render(request, 'menu/item_3D_detail.html', {'item': item})
