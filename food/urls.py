from django.urls import path
from .views import *
urlpatterns = [
    path('category', CategoryView.as_view()),
    path('category/<int:pk>', CategoryView.as_view()),
    path('food', FoodView.as_view()),
    path('food/<int:pk>', FoodView.as_view()),
    path('order', OrderView.as_view()),
    path('order/<int:pk>', OrderView.as_view()),

]