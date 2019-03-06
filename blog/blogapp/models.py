from django.db import models
from django.conf import settings
from django.utils import timezone
# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=200)
    text=models.TextField()
    author=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    date_created=models.DateTimeField(default=timezone.now)
    date_published=models.DateTimeField(blank=True,null=True)

    def publish(self):
        self.date_published = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)    


class Comment(models.Model):    #creating comment blog model
    comment_text = models.TextField()
    # pub_date = models.DateTimeField(blank=True,null=True)
    author = models.CharField(max_length=200)
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def __str__(self):
        return self.comment_text

    def approve(self):
        self.approved_comment=True
        self.save()
