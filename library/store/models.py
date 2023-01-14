from django.db import models


class Book(models.Model):
    
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    author = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f'Id:{self.id} {self.title}'
