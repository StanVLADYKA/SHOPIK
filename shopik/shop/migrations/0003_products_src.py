# Generated by Django 4.0.6 on 2022-07-17 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_products_alter_category_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='src',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
