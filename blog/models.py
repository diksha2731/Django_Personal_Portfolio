from django.db import models

class Blog (models.Model):
    title = models.CharField (max_length =200) #We can get all this field online from MOdel field Reference
    description = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.title
