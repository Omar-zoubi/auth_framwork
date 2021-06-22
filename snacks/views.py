from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Snack
from .serializers import SnackSerializer
from .permissions import IsauthorOrReadOnly
from rest_framework.generics import (
ListCreateAPIView,
RetrieveUpdateDestroyAPIView,
)


class SnacksList(ListCreateAPIView):
    permission_classes= (IsAuthenticatedOrReadOnly)
    queryset = Snack.objects.all()
    serializer_class = SnackSerializer

class SnacksDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsauthorOrReadOnly)
    queryset = Snack.objects.all()
    serializer_class = SnackSerializer
 
