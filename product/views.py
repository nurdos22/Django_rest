from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Category, Product, Review
from .serializers import (
    CategorySerializer,
    ProductSerializer,
    ReviewSerializer,
    ProductWithReviewsSerializer,
    CategoryWithCountSerializer,
    CategoryValidateSerializer,
    ProductValidateSerializer,
    ReviewValidateSerializer
)
from django.db.models import Count


@api_view(['GET', 'POST'])
def category_with_count_api_view(request):
    if request.method == 'GET':
        categories = Category.objects.annotate(products_count=Count('products'))
        data = CategoryWithCountSerializer(categories, many=True).data
        return Response(data=data)

    elif request.method == 'POST':
        serializer = CategoryValidateSerializer(data=request.data)
        if serializer.is_valid():
            category = Category.objects.create(**serializer.validated_data)
            return Response(data=CategorySerializer(category).data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def category_detail_api_view(request, id):
    try:
        category = Category.objects.get(id=id)
    except Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={'error': 'Category does not exist!'})

    if request.method == 'GET':
        data = CategorySerializer(category).data
        return Response(data=data)

    elif request.method == 'PUT':
        serializer = CategoryValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        category.name = serializer.validated_data.get('name')
        category.save()
        return Response(status=status.HTTP_201_CREATED, data=CategorySerializer(category).data)

    elif request.method == 'DELETE':
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def product_list_api_view(request):
    if request.method == 'GET':
        products = Product.objects.all()
        data = ProductSerializer(products, many=True).data
        return Response(data=data)

    elif request.method == 'POST':
        serializer = ProductValidateSerializer(data=request.data)
        if serializer.is_valid():
            product = Product.objects.create(**serializer.validated_data)
            return Response(data=ProductSerializer(product).data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def product_detail_api_view(request, id):
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={'error': 'Product does not exist!'})

    if request.method == 'GET':
        data = ProductSerializer(product).data
        return Response(data=data)

    elif request.method == 'PUT':
        serializer = ProductValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        product.title = serializer.validated_data.get('title')
        product.description = serializer.validated_data.get('description')
        product.price = serializer.validated_data.get('price')
        product.category = serializer.validated_data.get('category')
        product.save()
        return Response(status=status.HTTP_201_CREATED, data=ProductSerializer(product).data)

    elif request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def product_with_reviews_api_view(request):
    products = Product.objects.all()
    data = ProductWithReviewsSerializer(products, many=True).data
    return Response(data=data)


@api_view(['GET', 'POST'])
def review_list_api_view(request):
    if request.method == 'GET':
        reviews = Review.objects.all()
        data = ReviewSerializer(reviews, many=True).data
        return Response(data=data)

    elif request.method == 'POST':
        serializer = ReviewValidateSerializer(data=request.data)
        if serializer.is_valid():
            review = Review.objects.create(**serializer.validated_data)
            return Response(data=ReviewSerializer(review).data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def review_detail_api_view(request, id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={'error': 'Review does not exist!'})

    if request.method == 'GET':
        data = ReviewSerializer(review).data
        return Response(data=data)

    elif request.method == 'PUT':
        serializer = ReviewValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        review.text = serializer.validated_data.get('text')
        review.stars = serializer.validated_data.get('stars')
        review.product = serializer.validated_data.get('product')
        review.save()
        return Response(status=status.HTTP_201_CREATED, data=ReviewSerializer(review).data)

    elif request.method == 'DELETE':
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)