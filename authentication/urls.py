from django.urls import path
from authentication.views import login, logout, create_product_flutter

app_name = 'authentication'

urlpatterns = [
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('create-flutter/', create_product_flutter, name='create_product_flutter'),
]