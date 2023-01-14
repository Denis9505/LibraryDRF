from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self) -> str:
        return f'{self.title}'
