from django.shortcuts import render

from rest_framework import viewsets

from .serializers import HeroSerializer
from .models import Hero, Prodect


class HeroViewSet(viewsets.ModelViewSet):
    queryset = Prodect.objects.all()
    serializer_class = HeroSerializer