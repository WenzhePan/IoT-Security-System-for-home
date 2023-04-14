from django.db import models

# Create your models here.
class Door(models.Model):
    door = models.IntegerField(verbose_name='门',null=True)
    date = models.CharField(verbose_name='时间',max_length=40,null=True)
