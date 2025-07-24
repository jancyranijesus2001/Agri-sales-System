from django.db import models

class Waste(models.Model):
    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)
    waste_category = models.CharField(max_length=100)
    total_kg = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='waste_images/')
    status = models.CharField(max_length=20, choices=[('Available', 'Available'), ('Purchased', 'Purchased')], default='Available')

    def __str__(self):
        return f"{self.name} - {self.waste_category}"
