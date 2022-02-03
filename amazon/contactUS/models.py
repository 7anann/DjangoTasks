from django.db import models

# Create your models here.
class table1(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    
table1.objects.create(name='Hanan')