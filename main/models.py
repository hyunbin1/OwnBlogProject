from django.db import models


class Ob(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/')
    content = models.TextField(null=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title