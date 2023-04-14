from django.db import models

# Create your models here.
class User(models.Model):
    '''用户表'''

    id = models.AutoField('ID',primary_key=True)
    name = models.CharField(max_length=16,unique=False)
    password = models.CharField(max_length=16)


    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']
        verbose_name = '用户'
        verbose_name_plural = '用户'