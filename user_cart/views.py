from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


from rest_framework import status, generics, permissions
from rest_framework.decorators import api_view, authentication_classes, permission_classes

from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Product, CartItem
from .serializers import ProductSerializer, CartItemSerializer, AddCartItemSerializer, UserSerializer, MyTokenObtainPairSerializer

from rest_framework_simplejwt.views import TokenObtainPairView

#Login User
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
    

class UserCreateView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]


## old product view
# class ProductListView(generics.ListCreateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     permission_classes = [permissions.AllowAny]


class ProductListView(APIView):

    def get_permissions(self):
        # Allow unauthenticated access to the GET request
        if self.request.method == 'GET':
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]

    # @permission_classes([permissions.AllowAny])

    # @api_view(['GET'])
    # @authentication_classes([])
    # @permission_classes([]) 
    def get(self, request):
        queryset = Product.objects.all()
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def patch(self, request, pk):
        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = ProductSerializer(product, data=request.data, partial=True)
        if serializer.is_valid():
            if 'price' in request.data:
                product.price = request.data['price']
                product.save()
                return Response({'price': product.price}, status=status.HTTP_200_OK)
            return Response({'error': 'Price not provided'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class CartItemListView(APIView):
    permission_classes =  [permissions.IsAuthenticated]

    def get(self, request):
        cart_items = CartItem.objects.filter(user=request.user)
        serializer = CartItemSerializer(cart_items, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AddCartItemSerializer(data=request.data)
        if serializer.is_valid():
            cart_item, created = CartItem.objects.get_or_create(
                user=request.user,
                product=serializer.validated_data['product'],
                defaults={'quantity': serializer.validated_data['quantity']}
            )
            if not created:
                cart_item.quantity += serializer.validated_data['quantity']
                cart_item.save()
            return Response(CartItemSerializer(cart_item).data)
        return Response(serializer.errors, status=400)

class CartItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    permission_classes =  [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)


def hello_world(request):
    return HttpResponse("Hello, world!")
