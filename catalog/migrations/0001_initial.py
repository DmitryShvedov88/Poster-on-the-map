# Generated by Django 4.0 on 2025-02-10 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True, verbose_name='Место')),
                ('short_description', models.TextField(blank=True, max_length=250, null=True, verbose_name='Короткое описание')),
                ('long_descriptio', models.TextField(blank=True, null=True, verbose_name='Длинное описание')),
                ('lat', models.FloatField(verbose_name='Широта')),
                ('lon', models.FloatField(verbose_name='Долгота')),
            ],
        ),
    ]
