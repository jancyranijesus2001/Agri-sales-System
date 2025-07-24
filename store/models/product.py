from django.db import models
from django.utils.timezone import now
from django.db.models.signals import post_save
from django.dispatch import receiver
from .category import Category

class Products(models.Model):
    name = models.CharField(max_length=60)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length=250, default='', blank=True, null=True)
    image = models.ImageField(upload_to='uploads/products/')

    def __str__(self):
        return self.name

    @staticmethod
    def get_products_by_id(ids):
        return Products.objects.filter(id__in=ids)

    @staticmethod
    def get_all_products():
        return Products.objects.all()

    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
            return Products.objects.filter(category=category_id)
        else:
            return Products.get_all_products()


class ProductPriceHistory(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name="price_history")
    price = models.IntegerField()
    date = models.DateField(default=now)

    def __str__(self):
        return f"{self.product.name} - ₹{self.price} ({self.date})"

    @staticmethod
    def update_product_price(product_id, new_price):
        try:
            product = Products.objects.get(id=product_id)
            product.price = new_price
            product.save()

            # Save price history
            return ProductPriceHistory.objects.create(product=product, price=new_price)
        except Products.DoesNotExist:
            return None  # Handle error if product doesn't exist


# Signal to automatically update product price when a new price history record is added
@receiver(post_save, sender=ProductPriceHistory)
def update_product_price_from_history(sender, instance, created, **kwargs):
    if created:  # Ensures only new entries update the product price
        instance.product.price = instance.price
        instance.product.save()
