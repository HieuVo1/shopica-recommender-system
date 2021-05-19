from django.urls import path, include

from product.models import Product

urlpatterns = [
    path('predict/', include('product.urls'))
]
