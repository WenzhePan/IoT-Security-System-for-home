# Generated by Django 2.1.15 on 2022-02-07 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GetData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tmp', models.IntegerField(null=True, verbose_name='温度')),
                ('humi', models.IntegerField(null=True, verbose_name='湿度')),
            ],
        ),
    ]