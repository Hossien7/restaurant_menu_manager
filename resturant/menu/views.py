from django.shortcuts import render
from .models import Category


def menu(request):
    categories = Category.objects.filter(is_active=True)
    return render(request, 'menu/menu.html', {'categories': categories})
