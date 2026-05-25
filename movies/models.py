from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    publication_year = models.IntegerField()
    synopsis = models.TextField()
    poster = models.ImageField(
        upload_to='movies/',
        default='movies/default.jpg'
    )

    def __str__(self):
        return self.title
    