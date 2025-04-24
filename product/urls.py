from django.urls import path
from .views import (
    CategoryWithCountAPIView,
    CategoryDetailAPIView,
    ProductListAPIView,
    ProductDetailAPIView,
    ProductWithReviewsAPIView,
    ReviewListAPIView,
    ReviewDetailAPIView
)

urlpatterns = [
    path('v1/categories/', CategoryWithCountAPIView.as_view(), name='category-with-count'),
    path('v1/categories/<int:id>/', CategoryDetailAPIView.as_view(), name='category-detail'),
    path('v1/products/', ProductListAPIView.as_view(), name='product-list'),
    path('v1/products/<int:id>/', ProductDetailAPIView.as_view(), name='product-detail'),
    path('v1/products/reviews/', ProductWithReviewsAPIView.as_view(), name='product-with-reviews'),
    path('v1/reviews/', ReviewListAPIView.as_view(), name='review-list'),
    path('v1/reviews/<int:id>/', ReviewDetailAPIView.as_view(), name='review-detail'),
]

