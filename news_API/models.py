from django.db import models

# Create your models here.

class Tweet(models.Model):
    
    text = models.CharField( max_length=500), 
    username = models.CharField( max_length=50),
    retweet_count = models.IntegerField(),
    favorite_count = models.IntegerField(),
    # tags and named entities will be stored in a string seperated by ":"
    hashtags = models.CharField( max_length=500)
    namedE = models.CharField( max_length=500)
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.name


