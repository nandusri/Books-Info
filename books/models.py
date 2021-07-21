from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    author = models.CharField(max_length=250)

    def __str__(self):
        return self.title