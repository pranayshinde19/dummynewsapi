from django.db import models

# Create your models here.

class News(models.Model):
    title=models.CharField(max_length=250)
    date=models.CharField(max_length=250,default='feb,2023')
    description=models.TextField()
    url=models.CharField(max_length=250,default='to read more...')
    category=models.CharField(max_length=250)
    img=models.ImageField(upload_to='news/',null=True,blank=True)

    def __str__(self):
        return self.title