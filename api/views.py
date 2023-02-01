from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import NewsSerializer
from .models import News
# Create your views here.

class business(ModelViewSet):
    queryset=News.objects.filter(category='business')
    serializer_class=NewsSerializer

class entertainment(ModelViewSet):
    queryset=News.objects.filter(category='entertainment')
    serializer_class=NewsSerializer

class technology(ModelViewSet):
    queryset=News.objects.filter(category='technology')
    serializer_class=NewsSerializer

class country(ModelViewSet):
    queryset=News.objects.filter(category='country')
    serializer_class=NewsSerializer