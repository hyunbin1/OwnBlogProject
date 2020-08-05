from django.db import models



# 게시물
class Ob(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(null=True)
    content = models.TextField(null=True)
    update_at = models.DateTimeField(auto_now=True)
