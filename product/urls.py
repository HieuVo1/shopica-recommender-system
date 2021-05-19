from django.urls import path
from . import views

urlpatterns = [
    path('<int:userId>/', views.recommendation_list),
]
