# Generated by Django 2.1.15 on 2022-03-07 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GetData', '0004_auto_20220303_1249'),
    ]

    operations = [
        migrations.AddField(
            model_name='getdata',
            name='smoke',
            field=models.IntegerField(null=True, verbose_name='烟雾'),
        ),
    ]
