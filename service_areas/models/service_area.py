from django.contrib.gis.db import models


class ServiceArea(models.Model):
    name = models.CharField(max_length=30)
    price = models.DecimalField(decimal_places=2, max_digits=20)
    provider = models.ForeignKey(
        'providers.Provider',
        on_delete=models.CASCADE
    )
    poly = models.PolygonField()

    def __str__(self):
        return self.name
