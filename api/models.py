from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField(null=True,blank=True)
    id_author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="Post")
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True,verbose_name="Fecha de creación")
    updated_at = models.DateTimeField(auto_now=True,verbose_name="Fecha de actualizacion")

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="Comment")
    id_author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="Comment")
    content = models.TextField(null=True,blank=True)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True,verbose_name="Fecha de creación")
    updated_at = models.DateTimeField(auto_now=True,verbose_name="Fecha de actualizacion")



