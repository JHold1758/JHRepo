# blog/models.py
from django.db import models
from django.urls import reverse #

# Our table will be called "appname_modelname"
class Post(models.Model): # A Blog has a title, author, and body. 
    
    # Title Column -> CharField()
    title = models.CharField(max_length=200) 
 
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE, 
    
    )

    # Body Column -> TextField()
    body = models.TextField()


    def __str__(self):
        return self.title[:75]


    def get_absolute_url(self):

        return reverse('post_detail', args=[str(self.id)])

    