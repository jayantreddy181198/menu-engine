from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import FoodItemSerializer, BarItemSerializer
from .models import FoodItem, BarItem

class FoodItemCreateView(APIView):
    def post(self, request):
        serializer = FoodItemSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()  # Save the new item to the database
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, category=None):
        if category:
            food_items = FoodItem.objects.filter(category=category)
        else:
            food_items = FoodItem.objects.all()
        serializer = FoodItemSerializer(food_items, many=True)
        return Response(serializer.data)

class BarItemCreateView(APIView):
    def post(self, request):
        serializer = BarItemSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()  # Save the new item to the database
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, category=None):
        if category:
            bar_items = BarItem.objects.filter(category=category)
        else:
            bar_items = BarItem.objects.all()
        serializer = BarItemSerializer(bar_items, many=True)
        return Response(serializer.data)
