# Generated by Django 2.1.15 on 2022-03-03 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GetData', '0003_auto_20220210_1346'),
    ]

    operations = [
        migrations.AddField(
            model_name='getdata',
            name='depth',
            field=models.IntegerField(null=True, verbose_name='水深'),
        ),
        migrations.AddField(
            model_name='getdata',
            name='door',
            field=models.IntegerField(null=True, verbose_name='门'),
        ),
        migrations.AddField(
            model_name='getdata',
            name='echo',
            field=models.IntegerField(null=True, verbose_name='超声波'),
        ),
        migrations.AddField(
            model_name='getdata',
            name='fire',
            field=models.IntegerField(null=True, verbose_name='火灾'),
        ),
    ]
