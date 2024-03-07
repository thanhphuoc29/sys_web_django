from djongo import models

# Create your models here.

class Category(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True,null = True)
    type_product = models.CharField(max_length=100, null = True)


    def __str__(self):
        return self.name
    
