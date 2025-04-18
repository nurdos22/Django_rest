from django.contrib import admin
from .models import Category, Product, Review

class ReviewInLine(admin.TabularInline):
    model = Review
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    inlines = [ReviewInLine]


admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(Review)
