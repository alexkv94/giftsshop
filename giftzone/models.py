from django.db import models


# Create your models here.

class Categories(models.Model):
    name = models.CharField(max_length=100)
    lowerValue = models.DecimalField(max_digits=5, decimal_places=2)
    upperValue = models.DecimalField(max_digits=5, decimal_places=2)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Products(models.Model):
    category = models.ForeignKey(Categories, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d',blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id','slug'),)

    def __str__(self):
        self.title


class OrderItems(models.Model):
    pass

    def __str__(self):
        self.title


class Orders(models.Model):
    pass

    def __str__(self):
        self.title

