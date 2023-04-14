from django.db import models

# Create your models here.
class GetData(models.Model):
    tmp = models.FloatField(verbose_name='温度', null=True)
    humi = models.FloatField(verbose_name='湿度', null=True)
    date = models.FloatField(verbose_name='时间',primary_key=True,default=0)
    echo = models.FloatField(verbose_name='超声波',null=True)
    depth = models.FloatField(verbose_name='水深',null=True)
    fire = models.IntegerField(verbose_name='火灾',null=True)
    smoke = models.IntegerField(verbose_name='烟雾',null=True)

    class Meta:
        db_table = 'sensor_data'

