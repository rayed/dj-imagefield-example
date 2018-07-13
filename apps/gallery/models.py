from django.db import models

class Image(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='gallery')

    def __str__(self):
        return "%s (ID:%s)" % (self.name, self.id)