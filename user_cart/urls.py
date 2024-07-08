from django.urls import path, re_path

# from rest_framework_simplejwt.views import TokenObtainPairView #, TokenRefreshView
# from . import views

from .views import ProductListView, CartItemListView, CartItemDetailView, UserCreateView, MyTokenObtainPairView, CheckoutView, hello_world

from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    # test
    re_path(r'hello/?$', hello_world, name='hello_world'),

    # project 
    re_path(r'products/?$', ProductListView.as_view(), name='product-list'),
    re_path(r'products/<int:pk>/?$', ProductListView.as_view(), name='product-detail'),
    re_path(r'cart/?$', CartItemListView.as_view(), name='cart-list'),
    re_path(r'cart/<int:pk>/?$', CartItemDetailView.as_view(), name='cart-detail'),
    re_path(r'checkout/?$', CheckoutView.as_view(), name='checkout'),
    re_path(r'register/?$', UserCreateView.as_view(), name='user_register'),
    # path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    re_path(r'token/?$', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    re_path(r'token/refresh/?$', TokenRefreshView.as_view(), name='token_refresh')
]