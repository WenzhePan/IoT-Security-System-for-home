# Generated by Django 2.1.15 on 2022-04-30 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GetData', '0005_getdata_smoke'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='getdata',
            name='door',
        ),
        migrations.AlterField(
            model_name='getdata',
            name='date',
            field=models.FloatField(default=0, primary_key=True, serialize=False, verbose_name='时间'),
        ),
        migrations.AlterField(
            model_name='getdata',
            name='depth',
            field=models.FloatField(null=True, verbose_name='水深'),
        ),
        migrations.AlterField(
            model_name='getdata',
            name='echo',
            field=models.FloatField(null=True, verbose_name='超声波'),
        ),
        migrations.AlterField(
            model_name='getdata',
            name='humi',
            field=models.FloatField(null=True, verbose_name='湿度'),
        ),
        migrations.AlterField(
            model_name='getdata',
            name='tmp',
            field=models.FloatField(null=True, verbose_name='温度'),
        ),
    ]