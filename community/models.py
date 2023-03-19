from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Posts(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    postTitle = models.CharField(max_length=100, null=True)
    postBody = models.TextField(null=True)

    def __str__(self):
        return str(self.user)


class Comments(models.Model):
    post = models.ForeignKey(Posts, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    text = models.TextField()

    def __str__(self):
        return '%s - %s' % (self.post.postTitle, self.user)
