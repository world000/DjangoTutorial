from django.db import models

# Create your models here.
class Entry(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=10000)
    pub_date = models.DateTimeField()
    
    def __unicode__(self):
        return self.title
    
    class Meta:
        ordering = ['title']
