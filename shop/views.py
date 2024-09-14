from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Category, Order
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from .models import Menge, Comment
from .forms import CommentForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Barcha mahsulotlarni ko'rsatish
def product_list(request):
    # URL'dan kategoriya ID'sini olish
    category_id = request.GET.get('category')
    if category_id:
        # Agar kategoriya tanlangan bo'lsa, mahsulotlarni shu kategoriya bo'yicha filtrlash
        products = Product.objects.filter(category_id=category_id)
    else:
        # Aks holda barcha mahsulotlarni ko'rsatish
        products = Product.objects.all()
    
    categories = Category.objects.all()  # Barcha kategoriyalarni olib kelish
    return render(request, 'product_list.html', {'products': products, 'categories': categories})

# Mahsulot haqida batafsil ma'lumot
def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)  # Mahsulotni topish yoki 404 qaytarish
    return render(request, 'product_detail.html', {'product': product})

# Buyurtma qilish funksiyasi (foydalanuvchi kirgan bo'lishi kerak)
@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    order, created = Order.objects.get_or_create(
        user=request.user,
        product=product,
        status='Pending'
    )
    order.quantity += 1
    order.save()
    return redirect('product_list')

# Buyurtmalar ro'yxatini ko'rsatish (faqat foydalanuvchi uchun)
@login_required
def order_list(request):
    orders = Order.objects.filter(user=request.user)  # Foydalanuvchining barcha buyurtmalarini olish
    return render(request, 'order_list.html', {'orders': orders})



def menge_list(request):
    menge_list = Menge.objects.all()
    return render(request, 'menge_list.html', {'menge_list': menge_list})

def menge_detail(request, menge_id):
    menge = get_object_or_404(Menge, pk=menge_id)
    comments = menge.comments.all()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.menge = menge
            comment.author = request.user
            comment.save()
            return HttpResponseRedirect(reverse('menge_detail', args=[menge_id]))
    else:
        form = CommentForm()

    return render(request, 'menge_detail.html', {
        'menge': menge,
        'comments': comments,
        'form': form
    })

from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('menge_list')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

# Maxsus login view
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('menge_list')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'login.html')

# Maxsus logout view
def logout_view(request):
    logout(request)
    return redirect('login')