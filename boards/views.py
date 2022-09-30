from django.shortcuts import render
from rest_framework import generics
from .serializers import (BoardSerializer, ListSerializer, ItemSerializer)
from .models import Board, List, Item

# Create your views here.

class BoardList(generics.ListCreateAPIView):
    queryset = Board.objects.all().order_by('id')
    serializer_class = BoardSerializer

class BoardDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Board.objects.all().order_by('id')
    serializer_class = BoardSerializer


class ListList(generics.ListCreateAPIView):
    queryset = List.objects.all().order_by('id')
    serializer_class = ListSerializer

class ListDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = List.objects.all().order_by('id')
    serializer_class = ListSerializer


class ItemList(generics.ListCreateAPIView):
    queryset = Item.objects.all().order_by('id')
    serializer_class = ItemSerializer

class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all().order_by('id')
    serializer_class = ItemSerializer