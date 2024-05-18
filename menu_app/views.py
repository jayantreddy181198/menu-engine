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

    def get(self, request, filter_name=None, filter_data=None):
        if filter_name and filter_data:
            if filter_data.lower() == 'true':
                filter_data = True
            elif filter_data.lower() == 'false':
                filter_data = False
            filter_kwargs = {filter_name: filter_data}
            food_items = FoodItem.objects.filter(**filter_kwargs)
        else:
            food_items = FoodItem.objects.all()
        serializer = FoodItemSerializer(food_items, many=True)
        return Response(serializer.data)

    def put(self, request):
        update_all = request.data.get('Update_All', False)
        update_data = request.data.get('data', [])
        updated_data = []
        if update_all:
            food_items = FoodItem.objects.all()
            for food_item in food_items: 
                serializer = FoodItemSerializer(food_item, data=update_data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    updated_data.append(serializer.data)
                else:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            return Response(updated_data)
        else:
            ids_to_update = [item['id'] for item in update_data]
            food_items = FoodItem.objects.filter(pk__in=ids_to_update)
            for food_item in food_items:
                for update in update_data:
                    if update['id'] == food_item.id:
                        serializer = FoodItemSerializer(food_item, data=update, partial=True)
                        if serializer.is_valid():
                            serializer.save()
                            updated_data.append(serializer.data)
                        else:
                            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            return Response(updated_data)

class BarItemCreateView(APIView):
    def post(self, request):
        serializer = BarItemSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()  # Save the new item to the database
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, filter_name=None, filter_data=None):
        if filter_name and filter_data:
            if filter_data.lower() == 'true':
                filter_data = True
            elif filter_data.lower() == 'false':
                filter_data = False
            filter_kwargs = {filter_name: filter_data}
            bar_items = BarItem.objects.filter(**filter_kwargs)
        else:
            bar_items = BarItem.objects.all()
        serializer = BarItemSerializer(bar_items, many=True)
        return Response(serializer.data)

    def put(self, request):
        update_all = request.data.get('Update_All', False)
        update_data = request.data.get('data', [])
        updated_data = []
        if update_all:
            bar_items = BarItem.objects.all()
            for bar_item in bar_items:
                serializer = BarItemSerializer(bar_item, data=update_data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    updated_data.append(serializer.data)
                else:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            return Response(updated_data)
        else:
            ids_to_update = [item['id'] for item in update_data]
            bar_items = BarItem.objects.filter(pk__in=ids_to_update)
            for bar_item in bar_items:
                for update in update_data:
                    if update['id'] == bar_item.id:
                        serializer = BarItemSerializer(bar_item, data=update, partial=True)
                        if serializer.is_valid():
                            serializer.save()
                            updated_data.append(serializer.data)
                        else:
                            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            return Response(updated_data)