from django.db import models


class Ob(models.Model):
    title = models.CharField(max_length=50)
<<<<<<< HEAD
    image = models.ImageField(null=True)
    content = models.TextField(null=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
        
=======
    image = models.ImageField(null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    update_at = models.DateTimeField(auto_now=True) 
>>>>>>> 4add3c4a8e1ced17788c1f06ae43396bb5e18afc
