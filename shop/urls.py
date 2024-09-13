from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),  # Barcha mahsulotlar ro'yxati
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),  # Mahsulot batafsil ko'rish
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),  # Savatchaga mahsulot qo'shish
    path('orders/', views.order_list, name='order_list'),  # Foydalanuvchining buyurtmalari ro'yxati
    path('', views.menge_list, name='menge_list'),  # Bosh sahifa, barcha menge'lar ro'yxati
    path('menge/<int:menge_id>/', views.menge_detail, name='menge_detail'),
    path('', views.menge_list, name='menge_list'),  # Menge ro'yxati sahifasi
    path('menge/<int:menge_id>/', views.menge_detail, name='menge_detail'),  # Menge detal sahifasi

    path('', views.menge_list, name='menge_list'),
    path('menge/<int:menge_id>/', views.menge_detail, name='menge_detail'),

    # Maxsus Auth URLs
    path('login/', views.login_view, name='login'),  # Maxsus login view
    path('logout/', views.logout_view, name='logout'),  # Maxsus logout view
    path('signup/', views.signup, name='signup'),  # Ro'yxatdan o'tish sahifasi
]

