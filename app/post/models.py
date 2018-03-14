from django.conf.global_settings import AUTH_USER_MODEL
from django.db import models

User = AUTH_USER_MODEL


class Post(models.Model):
    title = models.CharField(max_length=255)
    # author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

