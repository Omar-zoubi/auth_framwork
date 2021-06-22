from django.urls import path
from .views import SnacksList, SnacksDetail

urlpatterns = [
    path('', SnacksList.as_view(), name='snacks_list'),
    path('<int:pk>/', SnacksDetail.as_view(), name='snacks_detail'),
]