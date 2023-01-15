from django.db import models


class Book(models.Model):
    
    GENRE = (
        ('Action', 'Action'),
        ('Detective', 'Detective'),
        ('Sci-fi', 'Sci-fi'),
        ('Historical', 'Historical'),
        ('Dystopia', 'Dystopia'),
        ('Fantasy', 'Fantasy'),
        ('Romance', 'Romance'),
        ('Western', 'Western'),
        ('Horror', 'Horror'),
        ('Classic', 'Classic'),
        ('Biography', 'Biography'),
    )

    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=255, choices=GENRE)
    raiting = models.DecimalField(max_digits=3, decimal_places=1)
    release = models.IntegerField(default=None)

    def __str__(self) -> str:
        return f'{self.title} | {self.author} | {self.raiting}'
