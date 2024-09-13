


from django.db import models
from django.contrib.auth.models import User

# Mahsulot kategoriyasi modeli
class Category(models.Model):
    name = models.CharField(max_length=100)  # Kategoriya nomi
    description = models.TextField(blank=True)  # Kategoriya haqida qisqacha ma'lumot

    def __str__(self):
        return self.name

# Mahsulot modeli
class Product(models.Model):
    name = models.CharField(max_length=200)  # Mahsulot nomi
    description = models.TextField(blank=True)  # Mahsulot tavsifi
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Mahsulot narxi
    stock = models.IntegerField()  # Ombordagi mahsulotlar soni
    category = models.ForeignKey(Category, on_delete=models.CASCADE)  # Mahsulot kategoriyasi
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)  # Mahsulot rasmi

    def __str__(self):
        return self.name

# Buyurtma modeli
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Buyurtmani qilgan foydalanuvchi
    product = models.ForeignKey(Product, on_delete=models.CASCADE)  # Buyurtma qilingan mahsulot
    quantity = models.IntegerField(default=1)  # Buyurtma miqdori
    ordered_date = models.DateTimeField(auto_now_add=True)  # Buyurtma qilingan vaqt
    status = models.CharField(
        max_length=50, 
        choices=[('Pending', 'Pending'), ('Shipped', 'Shipped'), ('Delivered', 'Delivered')],
        default='Pending'
    )  # Buyurtma holati

    def __str__(self):
        return f"{self.product.name} ({self.quantity}) by {self.user.username}"
    
from django.db import models
from django.contrib.auth.models import User

class Menge(models.Model):
    # Bu yerda 'menge' uchun kerakli maydonlarni belgilang
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    menge = models.ForeignKey(Menge, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'Comment by {self.author.username} on {self.menge.title}'



class Comment(models.Model):
    menge = models.ForeignKey(Menge, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'Comment by {self.author.username} on {self.menge.title}'
