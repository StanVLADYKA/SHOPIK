# Generated by Django 4.0.6 on 2022-07-17 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_products_src'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
