from django.urls import path

# from rest_framework_simplejwt.views import TokenObtainPairView #, TokenRefreshView
# from . import views

from .views import ProductListView, CartItemListView, CartItemDetailView, UserCreateView, MyTokenObtainPairView, hello_world

from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    # test
    path('hello/', hello_world, name='hello_world'),

    # project 
    path('products/', ProductListView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductListView.as_view(), name='product-detail'),
    path('cart/', CartItemListView.as_view(), name='cart-list'),
    path('cart/<int:pk>/', CartItemDetailView.as_view(), name='cart-detail'),
    path('register/', UserCreateView.as_view(), name='user_register'),
    # path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh')
]