# Generated by Django 2.0.5 on 2018-06-01 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='created_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
