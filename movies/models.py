from django.db import models

class Movie(models.Model):
    
    name = models.CharField(max_length=100, null=False)
    Id = models.AutoField(primary_key=True)
    genre = models.CharField(max_length=50, null=False)
    director = models.CharField(max_length=100, null=False)
    year = models.IntegerField(null=False)
    synopsis = models.TextField(null=False)
    picture = models.ImageField(upload_to='movies_images', null=True)  # Allows for image uploads

    def __str__(self):
        return self.name