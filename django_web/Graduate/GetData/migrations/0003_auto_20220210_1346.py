# Generated by Django 2.1.15 on 2022-02-10 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GetData', '0002_auto_20220210_1346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='getdata',
            name='date',
            field=models.IntegerField(default=0, primary_key=True, serialize=False, verbose_name='时间'),
        ),
    ]
