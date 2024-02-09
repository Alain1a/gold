from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.CharField(max_length=100)
    pub_date = models.DateTimeField(auto_now_add=True)
    state = models.CharField(max_length=100, default="visible")

    def __str__(self):
        return self.title
 