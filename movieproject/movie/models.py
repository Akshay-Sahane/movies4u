from django.db import models

# Create your models here.

class BMovie(models.Model):
    movieId=models.AutoField(primary_key=True)
    movieName=models.CharField(max_length=100)
    movieType=models.CharField(max_length=20)
    movieReleasedate=models.DateField()
    movieDescription=models.TextField()
    movieImage=models.ImageField(upload_to="Bollywoodimages/",default="No-Image.png")
    movieLink=models.CharField(max_length=250)

    def __str__(self):
        return f"{self.movieName}-{self.movieType}-{self.movieReleasedate}-{self.movieDescription}-{self.movieImage}"


class HMovie(models.Model):
    movieId=models.AutoField(primary_key=True)
    movieName=models.CharField(max_length=100)
    movieType=models.CharField(max_length=20)
    movieReleasedate=models.DateField()
    movieDescription=models.TextField()
    movieImage=models.ImageField(upload_to="Hollywoodimages/",default="No-Image.png")
    movieLink=models.CharField(max_length=250)

    def __str__(self):
        return f"{self.movieName}-{self.movieType}-{self.movieReleasedate}-{self.movieDescription}-{self.movieImage}"
        