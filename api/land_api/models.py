from django.db import models


class Land(models.Model):
    parcel_id = models.CharField(max_length=100)
    plot_number = models.CharField(max_length=100)
    owner_name = models.CharField(max_length=150)
    location = models.TextField()
    area = models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return self.owner_name