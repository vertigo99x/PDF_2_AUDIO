from django.db import models

# Create your models here.

class PDF(models.Model):
    pdf = models.FileField(upload_to='pdfs/', null=False)
    created = models.DateTimeField(auto_now_add=True)
    
    
    class Meta:
        ordering=['-created']
    
    
class Audios(models.Model):
    audio = models.FileField(upload_to='audios/', null=False)
    created = models.DateTimeField(auto_now_add=True)
    
    
    class Meta:
        ordering=['-created']