# Generated by Django 4.0.4 on 2022-08-24 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orderprocess', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='futuregflist',
            name='Age',
            field=models.IntegerField(),
        ),
    ]
