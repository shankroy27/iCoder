from django.db import models

# Create your models here.
class Post(models.Model):
    Sno=models.AutoField(primary_key=True)
    title=models.CharField(max_length=250)
    content=models.TextField()
    author=models.CharField(max_length=13)
    slug = models.CharField(max_length=130,default='')
    timestamp=models.DateTimeField(blank=True)

    def __str__(self):
        return self.title +' by '+self.author
    