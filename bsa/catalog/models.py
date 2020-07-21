from django.db import models
from django.urls import reverse # Used to generate URLs by reversing the URL patterns
# Create your models here.
class Genre(models.Model):
    """Model representing a sport genre."""
    name = models.CharField(max_length=200, help_text='Enter a sport genre (e.g. Basketball)')
    
    def __str__(self):
        return self.name



class Author(models.Model):
    full_name = models.CharField(max_length=70)

    def __str__(self):
        return self.full_name

class Article(models.Model):
    pub_date = models.DateField()
    headline = models.CharField(max_length=200)
    content = models.TextField()
    summary = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    genre = models.ManyToManyField(Genre, help_text='Select a genre for this article')
    def __str__(self):
        return self.headline
    def get_absolute_url(self):
        """Returns the url to access a detail record for this article."""
        return reverse('article-detail', args=[str(self.id)])
