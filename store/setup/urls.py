from django.contrib import admin
from django.urls import path
from .views.home import Index, store
from .views.signup import Signup
from .views.login import Login, logout
from .views.cart import Cart
from .views.checkout import CheckOut
from .views.orders import OrderView
from .views.search import search
from .middlewares.auth import auth_middleware
from .views.product_list import product_list
from .views.waste import waste_list, waste_create, waste_update, waste_delete, waste_purchase

urlpatterns = [
     path('today_market_price', product_list, name='today_market_price'),
     path('', Index.as_view(), name='homepage'),
    
     # ✅ Use a unique path for product list
     path('carts/', Index.as_view(), name='index'),  # ✅ Keep Index as homepage
    path('store/', store, name='store'),
    path('signup', Signup.as_view(), name='signup'),
    path('login', Login.as_view(), name='login'),
    path('logout', logout, name='logout'),
    path('cart', auth_middleware(Cart.as_view()), name='cart'),
    path('check-out', CheckOut.as_view(), name='checkout'),
    path('search', search, name='search'),
    path('orders', auth_middleware(OrderView.as_view()), name='orders'),
     path('waste_list/', waste_list, name='waste_list'),
    path('create/', waste_create, name='waste_create'),
    path('update/<int:id>/', waste_update, name='waste_update'),
    path('delete/<int:id>/', waste_delete, name='waste_delete'),
    path('purchase/<int:id>/', waste_purchase, name='waste_purchase'),
]
