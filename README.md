# THE ONLINE SHOPPING - USER CART MODULE


## Used Framework 

[Django>=3.2,<4.0](https://www.djangoproject.com/)


## Packages

djangorestframework>=3.12.0
djangorestframework-simplejwt>=4.7.2

## Database 
### Postgres

## Tables

### products

| ID   | Name           | Price |  Image |
|------|----------------|-------|--------|
| 1    | Hand Blender   |  500  |        |
| 2    | Micro-wave     |  2000 |        |

### cart

| id | quantity | product_id | user_id | status |
|----|----------|------------|---------|--------|
|  1 |    2     |      2     |    1    |   0    |


## Blocks of code  | CONNECTION POOLING


```
from django.contrib.auth.models import User
from django.db import models



class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name

class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    status = models.IntegerField(default=0)  # 0 for not checked out, 1 for checked out

    @property
    def total_price(self):
        return self.quantity * self.product.price

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"
```


## Requests

#### 1. List Products
  ``` 
       curl -X GET http://127.0.0.1:8001/api/v1/products/
  ```

#### 2. User Register 
    => curl -X POST \
```  
  http://localhost:8001/api/v1/register/ \
  -H 'Content-Type: application/json' \
  -d '{
    "username": "saeed",
    "email": "saeed@damen.com.eg",
    "password": "saeed"
  }'
```
#### 3. Login
```
   curl -X POST http://127.0.0.1:8001/api/v1/token/ -H "Content-Type: application/json" -d '{"username": "saeed", "password": "saeed"}'

```
For other requests check .http file

## Run Locally Using Docker compose 


```

$ cd deployments

## For The First Time to migrate the database run command

$ docker compose up -d --build

later use can only use 

$ docker compose up -d

## Upcoming
- Products to be only added using authorized admin / super user
- list all user paid products with its counts & price


