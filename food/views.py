from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from .permissions import Komissar
from .serializer import *

# Create your views here.


class CategoryView(APIView):
    permission_classes = [Komissar]
    def get(self, request: Request, pk=None) -> Response:
        if pk:
            category = Category.objects.get(pk=pk)
            serializer = CategorySerializer(category)
            return Response(serializer.data)
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    def post(self, request: Request) -> Response:
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def put(self, request: Request, pk: int) -> Response:
        category = Category.objects.get(pk=pk)
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def delete(self, request: Request, pk: int) -> Response:
        category = Category.objects.get(pk=pk)
        category.delete()
        return Response(status=204)


class FoodView(APIView):
    permission_classes = [Komissar]
    def get(self, request: Request, pk=None) -> Response:
        if pk:
            food = Food.objects.get(pk=pk)
            serializer = FoodSerializer(food)
            return Response(serializer.data)

        foods = Food.objects.all()
        serializer = FoodSerializer(foods, many=True)
        return Response(serializer.data)


    def post(self, request: Request) -> Response:
        serializer = FoodSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


    def put(self, request: Request, pk: int) -> Response:
        food = Food.objects.get(pk=pk)
        serializer = FoodSerializer(food, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


    def delete(self, request: Request, pk: int):
        food = Food.objects.get(pk=pk)
        food.delete()
        return Response(status=204)


class OrderView(APIView):
    permission_classes = [Komissar]
    def get(self, request: Request, pk=None):
        if pk:
            order = Order.objects.get(pk=pk)
            serializer = OrderSerializer(order)
            return Response(serializer.data, status=200)

        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data, status=200)

    def post(self, request: Request):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def put(self, request: Request, pk: int):
        order = Order.objects.get(pk=pk)
        serializer = OrderSerializer(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def delete(self, request: Request, pk: int):
        order = Order.objects.get(pk=pk)
        order.delete()
        return Response(status=204)
