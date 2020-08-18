from django.db import models

# Create your models here.

class Ob(models.Model):
    title = models.CharField(max_length = 50)
    image = models.ImageField(upload_to = 'images/')
    content = models.TextField()
    update_at = models.DateTimeField(auto_now=True)
    # admin 등록시 등록된 이름으로 나오게 하는 법
    
    def __str__(self):
        
        return self.name

    def __str__(self):
        
        return self.title