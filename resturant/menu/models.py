from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)


    class Meta:
        verbose_name_plural = "categories"
    

    def __str__(self):
        return self.name
    

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=50, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey(Category, related_name='menu_items', on_delete=models.CASCADE) 
    is_special = models.BooleanField(default=False)
    is_vegetarian = models.BooleanField(default=False)
    is_icy = models.BooleanField(default=False)
    is_coffee = models.BooleanField(default=False)
    image = models.ImageField(upload_to='menu_items/', blank=True, null=True)
    D_model = models.FileField(upload_to='3d_models/', blank=True, null=True)


    def __str__(self):
        return self.name
    