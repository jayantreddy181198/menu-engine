from django.urls import path
from .views import FoodItemCreateView, BarItemCreateView

urlpatterns = [
    path('api/food/create', FoodItemCreateView.as_view(), name='food-item-create'),
    path('api/food/getall', FoodItemCreateView.as_view(), name='food-item-list'),
    path('api/food/update', FoodItemCreateView.as_view(), name='food-item-update'),
    path('api/food/getall/<str:filter_name>/<str:filter_data>', FoodItemCreateView.as_view(), name='food-item-list'),
    path('api/bar/create', BarItemCreateView.as_view(), name='bar-item-create'),
    path('api/bar/getall', BarItemCreateView.as_view(), name='bar-item-list'),
    path('api/bar/getall/<str:filter_name>/<str:filter_data>', BarItemCreateView.as_view(), name='bar-item-list'),
    path('api/bar/update', BarItemCreateView.as_view(), name='bar-item-update')
]
