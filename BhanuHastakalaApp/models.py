from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_image', null=True)
    market_price = models.PositiveIntegerField()
    selling_price =models.PositiveIntegerField()
    description = models.TextField()
    warrenty =models.CharField(max_length=100,null=True, blank=True)
    return_policy = models.CharField(max_length=100, null=True, blank=True)
    review_count = models.PositiveIntegerField(default=0)
    created_date = models.DateTimeField(auto_now_add=True)
    feathers = models.BooleanField(null=True, blank=True)

    def __str__(self):
        return self.title





