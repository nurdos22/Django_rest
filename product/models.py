from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return  self.name

class Product(models.Model):
    title = models.CharField(max_length=230)
    description = models.TextField()
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


    def __str__(self):
        return self.title


class Review(models.Model):
    text = models.TextField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.text
