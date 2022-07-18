# Generated by Django 4.0.6 on 2022-07-17 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('price', models.CharField(max_length=20)),
                ('description', models.TextField()),
            ],
        ),
        migrations.AlterModelOptions(
            name='category',
            options={},
        ),
    ]